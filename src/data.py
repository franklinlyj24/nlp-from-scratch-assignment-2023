import urllib.request
import requests
import os
from tqdm import tqdm
import PyPDF2
import spacy
import time
from bs4 import BeautifulSoup

MAX = 50
# venues = {
#     'acl': [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
#     'cl': [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
#     'conll': [22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
#     'emnlp': [22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
#     'iwslt': [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
# }
venues = {
        'acl': [22, 21, 20, 19, 18],
        'cl': [22, 21, 20, 19, 18],
        'conll': [22, 21, 20, 19, 18],
        'emnlp': [22, 21, 20, 19, 18],
        'iwslt': [22, 21, 20, 19, 18]
    }


def has_show_abstract_title(tag):
    return tag.name == 'span' and tag.find('a', title='Show Abstract')

def download():
    for venue in venues:
        for year in venues[venue]:
            print(f'[venue] {venue} [year] {year}')
            path_dir = f'../data/pdfs/{venue}/{year}'
            os.makedirs(path_dir, exist_ok=True)
            
            ### Load HTML
            url = f'https://aclanthology.org/events/{venue}-20{year}/'
            response  = requests.get(url)
            if response.status_code == 200:
                html = response.text
            else:
                print(f"Failed to retrieve the HTML. Status code: {response.status_code}")
            
            ### Parse HTML
            i = 0
            soup = BeautifulSoup(html, 'html.parser')
            # A paper has abstract. Otherwise, it may be erratum, orbituary, full concatenation of all pdfs, etc
            span_elements = soup.find_all(has_show_abstract_title)
            for span in span_elements:
                # A paper should have title 'Open PDF' in <a>. Otherwise it can be Supplementary, Presentation, etc
                a_elements = span.find_all('a', title='Open PDF')
                for e in a_elements:
                    pdf_url = e.get('href')
                    response = requests.get(pdf_url)
                    
                    file_name = pdf_url.split('/')[-1]
                    path_pdf = os.path.join(path_dir, file_name)
                    
                    if response.status_code == 200:
                        with open(path_pdf, 'wb') as f:
                            f.write(response.content)
                        print(f"PDF downloaded as {path_pdf}")
                    else:
                        print(f"Failed to download PDF. Status code: {response.status_code}")
                    
                    i += 1
                    if i >= MAX:
                        break
                if i >= MAX:
                    break

def extract(path_data):
    nlp = spacy.load("en_core_web_sm")
    venues = os.listdir(path_data)
    
    for venue in venues:
        path_venue = os.path.join(path_data, venue)
        years = os.listdir(path_venue)
        
        for year in years:
            path_pdfs = os.path.join(path_data, venue, year)
            pdfs = os.listdir(path_pdfs)
            
            for pdf in pdfs:
                path_pdf = os.path.join(path_data, venue, year, pdf)
                
                dir_txt = os.path.join('../data/texts', venue, year)
                os.makedirs(dir_txt, exist_ok=True)
                path_txt = os.path.join(dir_txt, pdf[:-3] + 'txt')
                print(path_txt)
                ftxt = open(path_txt, 'w')
                
                with open(path_pdf, 'rb') as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    
                    for page_number in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_number]
                        # Rare errors about IndirectObject may occur
                        # They don't seem to affect the extract text much
                        try:
                            text = page.extract_text()
                        except:
                            print('An error occurred while parsing pdf')
                        text = text.replace('\n', ' ')
                        
                        sentences = nlp(text).sents
                        for sentence in sentences:
                            line = []
                            for token in sentence:
                                line.append(token.text)
                            line = " ".join(line)
                            ftxt.write(line + '\n')            
                ftxt.close()
                
    
if __name__ == "__main__":
    # download()
    extract('../data/pdfs')