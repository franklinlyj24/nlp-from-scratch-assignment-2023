.PHONY: all uninstall venv setup install create_folder

all: clean venv setup install create_folder

venv:
    @echo "Creating a virtual environment"
    python3 -m venv venv

setup:
    @echo "Activating the virtual environment"
    source venv/bin/activate

install:
    @echo "Installing dependencies"
    pip install -r requirements.txt

create_folder:
    @echo "Creating a save folder if missing"
    mkdir -p save

clean:
    @echo "Removing the virtual environment and save folder"
    rm -rf venv
    rm -rf save