import flask
import forms
import numpy as np
import tensorflow
from tensorflow import keras
from flask import Flask
from flask import render_template,url_for,flash,redirect
from forms import askForm
app = Flask(__name__)
app.config['SECRET_KEY']='bigbossisshit'

months=['January','February','March','April','May','June','July','August','September','October','November','December']
@app.route('/',methods=['GET', 'POST'])
def index():
    form = askForm()
    return render_template('index.html',form=form)

@app.route('/predict',methods=['GET', 'POST'])
def predict():
    form = askForm()
    if form.validate_on_submit():
        x_new = []
        x_new.append(float(form.year.data))
        x_new = np.array(x_new)/100
        path = 'states/'+form.state.data
        model = keras.models.load_model(path)
        ls  =   model.predict(x_new)*280
        ls = ['{:.2f}'.format(x) for x in ls[0]] #to show only 2 decimal places
    else:
        flash(f'Please Enter a year between 1850 to 2050','error')
        return redirect(url_for('index'))

    return render_template('predict.html',ls = ls,months=months,year=form.year.data,state = form.state.data)


if __name__=='__main__':
    app.run(debug=True)