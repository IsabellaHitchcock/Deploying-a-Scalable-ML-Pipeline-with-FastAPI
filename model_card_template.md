# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was created by Isabella Hitchcock. It is a linear regression model made with sklearn. Default parameters were used. 
## Intended Use
This regression is intended to predict the binary output of income (above, or below 50k) based on census data provided by Udacity.
## Training Data
Training data is 80% of the original dataset. 
## Evaluation Data
The model was evaluated by using a subset of the original database of 10% to determine precision, recall, and f1-score
## Metrics
The model was evaluated using precision, recall, and F1 score. Precision: 0.7611, Recall 0.2812, F1 0.4107. The low recall leads to a slightly poorly balanced model, which may bias analysis. 

## Ethical Considerations
This model, as with all models, is sucepitible to bias based on bias in the data. Census data can reflect societal biases, risking unfair predictions. Addressing these biases is important to ensure ethical model outcomes.
## Caveats and Recommendations
The low recall and F1 scores suggest this model may perform poorly in critical analyses. For recall-sensitive use cases, consider avoiding this model or fine-tuning its hyperparameters.