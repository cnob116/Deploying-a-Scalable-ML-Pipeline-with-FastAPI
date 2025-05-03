# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model uses US Census Data to predict if someone's salary is greater than $50,000 a year. It does this by using RandomForestClassifier and the scikit-learn library. 
## Intended Use
The intended use is to predict whether someone's salary is greater than $50,000 a year.
## Training Data
The training data came from the US Census Bureau.
The features used in this dataset are age, workclass, fnlgt, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, salary. Salary is set up to be less than or equal to $50,000 or greater than 50,000.
## Evaluation Data
From the original dataset I splt it into two and 20% of it was used as evaluation data.
## Metrics
_Please include the metrics used and your model's performance on those metrics._
This performances of this model are:
Precision: 0.7353
Recall: 0.6368
F1: 0.6831

## Ethical Considerations
There are no biases towards specific groups of people. Because of that it's fair to use to predict whether or not someone makes over $50,000 a year.
## Caveats and Recommendations
The caveat to this model is that the data is from 1994 so it is outdated. A more recent dataset would be better to use. I would recommend using a more recent dataset for more accurate salary predictions that are reflective of the current time.