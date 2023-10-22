# Submission

We will have two test sets that you will need to submit your models’ predictions on on Kaggle. Both test sets are drawn from the same distribution: paragraphs from ACL, NAACL, and EMNLP papers from 2022 and 2023. 

- A public test set. We’ve released this at [invitation link](https://www.kaggle.com/t/1e5394aefd694a3695cb9ccaa732f948)
- A “private” test set. We will be releasing this ~48 hours before the assignment’s due date, i.e. on Wed Oct 25th.

 Both test sets are unlabelled; we’ll compare your model predictions on these sets to a hidden set of labels (that we’ve annotated ourselves). 

 

## Notes
- Evaluation is very slow (takes 5-10 minutes)
- In `test.csv`, each example is separated by the `Null` value (i.e. ‘’, or take a look at Row 36)
- Even though the provided `test.csv` separates different examples with `‘’`, students’ csv files for the submission should separate different examples with some random string like “X” that is not Null. 

# Evaluation

The level-of-performance component of your grade will be based on your performance on *both* sets. It will be computed as follows:

```score = (public_F1 + private_F1) / 2```

10 points for level of performance. We’ll compute this as 

```
if score < 0.2:
    points = round(30 * score) 
else:
    points = student_score_quartile() + 6

```

So, up to an average F1 score of 0.2, it’s steps up to 6 points. Then, above that the bottom quartile of students gets 7, second quartile gets 8, third quartile gets 9, and then top quartile gets 10.

Note that these points are only 10% of the assignment points in total. The remaining 90% are for other things such as creating data, making sure you have all the required info in the report, etc. So if you do a good job on the other parts you should be able to get a good grade on the assignment overall.
