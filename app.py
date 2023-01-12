from wsgiref import simple_server
from flask import Flask, request,render_template
from flask import Response
from flask_cors import CORS
from flask_cors import cross_origin
from logistic_deploy import predObj
import numpy as np

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True


class ClientApi:

    def __init__(self):
        self.predObj = predObj()
        print('Here 3')

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():

    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predictRoute():
    try:
        print('Here 4')

        #if request.json['data'] is not None:
        limit_bal = float(request.form['Limit_bal'])
        male = float(request.form['male'])
        female = float(request.form['female'])
        grad_school = float(request.form['grad_school'])
        university = float(request.form['university'])
        high_school = float(request.form['high_school'])
        edu_others = float(request.form['edu_others'])
        married = float(request.form['married'])
        single = float(request.form['single'])
        marriage_others = float(request.form['marriage_others'])
        age = float(request.form['age'])
        pay_1 = float(request.form['pay_1'])
        pay_2 = float(request.form['pay_2'])
        pay_3 = float(request.form['pay_3'])
        pay_4 = float(request.form['pay_4'])
        pay_5 = float(request.form['pay_5'])
        pay_6 = float(request.form['pay_6'])
        bill_amt_1 = float(request.form['bill_amt_1'])
        bill_amt_2 = float(request.form['bill_amt_2'])
        bill_amt_3 = float(request.form['bill_amt_3'])
        bill_amt_4 = float(request.form['bill_amt_4'])
        bill_amt_5 = float(request.form['bill_amt_5'])
        bill_amt_6 = float(request.form['bill_amt_6'])
        pay_amt_1 = float(request.form['pay_amt_1'])
        pay_amt_2 = float(request.form['pay_amt_2'])
        pay_amt_3 = float(request.form['pay_amt_3'])
        pay_amt_4 = float(request.form['pay_amt_4'])
        pay_amt_5 = float(request.form['pay_amt_5'])
        pay_amt_6 = float(request.form['pay_amt_6'])

       
        print('Here 5')
        # data = request.json['data']
        data = {'limit_bal':limit_bal,'male':male,'female':female,'grad_school':grad_school,'university':university,'high_school':high_school,'edu_others':edu_others,
                'married':married,'single':single,'marriage_others':marriage_others,'age':age,
                'pay_1':pay_1,'pay_2':pay_2,'pay_3':pay_3,'pay_4':pay_4,'pay_5':pay_5,
                'pay_6':pay_6,'bill_amt_1':bill_amt_1,
                'bill_amt_2':bill_amt_2,'bill_amt_3':bill_amt_3,'bill_amt_4':bill_amt_4,'bill_amt_5':bill_amt_5,'bill_amt_6':bill_amt_6,
                'pay_amt_1':pay_amt_1,'pay_amt_2':pay_amt_2,
                'pay_amt_3':pay_amt_3,'pay_amt_4':pay_amt_4,'pay_amt_5':pay_amt_5,'pay_amt_6':pay_amt_6}
        print('data is:     ', data)
        pred=predObj()
        res = pred.predict_log(data)

        #result = clntApp.predObj.predict_log(data)
        print('result is        ',res)
        return render_template('results.html',result=res)
    except ValueError:
        return Response("Value not found")
    except Exception as e:
        print('exception is   ',e)
        return Response(e)


if __name__ == "__main__":
    #print('Here 1')
    clntApp = ClientApi()
    #print('Here 2')
    # host = '0.0.0.0'
    # port = 5000
    app.run(debug=True)
    # httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    # httpd.serve_forever()
