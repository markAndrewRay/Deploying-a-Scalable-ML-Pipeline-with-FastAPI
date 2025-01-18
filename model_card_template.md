# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model Developed By Mark Ray
January 2025
Version 1.0
Decision Tree Classifier
The model uses the decision tree algorithm for classification based on socioeconomic factors.

## Intended Use
The model's intended use is to predict an individual's income based on on the features of the census data.
The model is intended to be used by researchers for the purpose of analyzing income inequality.
The model is not intended to be used to provide personal financial advice.

## Training Data
The training data "census.csv" was derived from census data and encoded using OneHotEncoder.

## Evaluation Data
The data was evaluated based on the following features:
        age
    workclass
    education
    education-num
    marital-status
    occupation
    relationship
    race
    sex
    capital-gain
    capital-loss
    hours-per-week
    native-country

## Metrics
Precision: 0.6244 
Recall: 0.6454 
F1: 0.6347

## Ethical Considerations
The model should be evaluated to ensure that it does not discriminate based on gender, race, age related, or educational biases.

## Caveats and Recommendations
Data used in conjunciton with this model should be assessed for relevance, with th eknowledge that it may perform differently on census datasets from countries outside of the United States. The model may contain the potential for bias based on gender, race, age, and educational level. The model may be too simplistic to fully explore the minutiae of real world regional context.
The model should for this reason be continually updated and audited to determine bias. The model's reaction to contextual change should be monitored and the model should also be held to ethical review.