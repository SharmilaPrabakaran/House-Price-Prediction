# House-Price-Prediction

Predicting house prices using Regression.
This project applies machine learning concepts on King County houseprice dataset to predict the selling price of a new home.

Software and Libraries
This project uses the following libraries:
* Python
* Flask
* pandas
* scikit-learn

# Installation

pip install -r requirements.txt

# To run this project:

1. Run model.py that loads the dataset available within the repository and then fits the dataset onto the model. The model is saved using the pickle library - used for serializing and de-serializing python object.

2. Run server.py in command prompt to start webserver. Client (browser) communicates with server using REST API. REST API is written using flask framework. 

3. Finally, open the web-browser and go to http://localhost:8080/index to get index.html running.
