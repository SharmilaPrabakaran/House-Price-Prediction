from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

model = pickle.load(open('model.pkl','rb'))

@app.route('/price', methods = ['POST'])
def predict():
    data = int(request.form['sqft'])
    prediction = model.predict([[np.array(data)]])
    output = prediction[0]
    return render_template('result.html',prediction = output)

if __name__ == '__main__':
    #app.debug = True
    app.run()
