from flask import flask , render_template  request
import joblib

app=Flask(_name_)

@app.route("/user")
def user_details():
    return render_template('index.html')

@app.route("/prediction",methods=['GET','POST'])
def details():
    if request.method == 'POST':
        data = request.from 
        job = int(data['job'])
        marital = int(data['marital'])
        default = int(data['default'])
        balance = int(data['balance'])
        hosuing = int(data['housing'])
        month = int(data['month'])
        age_category = int(data['age_category'])

        parameters=[['job', 'marital', 'default', 'balance', 'housing', 'loan', 'month',
       'age_category']]

       result = model.predict(parameters)[0]

       if result == 1:
            return prediction is 1
        else: 
            return prediction is 0

if __name__ == "__main__":
    app.run() 