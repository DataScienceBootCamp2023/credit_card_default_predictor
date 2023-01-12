import os
from wsgiref import simple_server
from flask import Flask, request,render_template, jsonify
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

@app.route('/',methods=['GET'])	 # route to display the home page
@cross_origin()
def homePage():

	return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predictRoute():
	try:
		if request.is_json:
			data = request.form
			try:
				limit_bal = float(data['limit_bal'])
				male = float(data['male'])
				female = float(data['female'])
				grad_school = float(data['grad_school'])
				university = float(data['university'])
				high_school = float(data['high_school'])
				edu_others = float(data['edu_others'])
				married = float(data['married'])
				single = float(data['single'])
				marriage_others = float(data['marriage_others'])
				age = float(data['age'])
				pay_1 = float(data['pay_1'])
				pay_2 = float(data['pay_2'])
				pay_3 = float(data['pay_3'])
				pay_4 = float(data['pay_4'])
				pay_5 = float(data['pay_5'])
				pay_6 = float(data['pay_6'])
				bill_amt_1 = float(data['bill_amt_1'])
				bill_amt_2 = float(data['bill_amt_2'])
				bill_amt_3 = float(data['bill_amt_3'])
				bill_amt_4 = float(data['bill_amt_4'])
				bill_amt_5 = float(data['bill_amt_5'])
				bill_amt_6 = float(data['bill_amt_6'])
				pay_amt_1 = float(data['pay_amt_1'])
				pay_amt_2 = float(data['pay_amt_2'])
				pay_amt_3 = float(data['pay_amt_3'])
				pay_amt_4 = float(data['pay_amt_4'])
				pay_amt_5 = float(data['pay_amt_5'])
				pay_amt_6 = float(data['pay_amt_6'])				
				# Prepare the input data in the format required by the model
				# data = request.json['input_data']                    


				input_data = {'limit_bal':limit_bal,'male':male,'female':female,'grad_school':grad_school,'university':university,'high_school':high_school,'edu_others':edu_others,'married':married,'single':single,'marriage_others':marriage_others,'age':age,'pay_1':pay_1,'pay_2':pay_2,'pay_3':pay_3,'pay_4':pay_4,'pay_5':pay_5,'pay_6':pay_6,'bill_amt_1':bill_amt_1,'bill_amt_2':bill_amt_2,'bill_amt_3':bill_amt_3,'bill_amt_4':bill_amt_4,'bill_amt_5':bill_amt_5,'bill_amt_6':bill_amt_6,'pay_amt_1':pay_amt_1,'pay_amt_2':pay_amt_2,'pay_amt_3':pay_amt_3,'pay_amt_4':pay_amt_4,'pay_amt_5':pay_amt_5,'pay_amt_6':pay_amt_6}
				print('Input data is:     ', input_data)

						# Make the prediction using the model
				pred=predObj()
				prediction = pred.predict_log(input_data)
				#result = clntApp.predObj.predict_log(data)
				print('result is        ',prediction)
				return render_template('results.html',result=prediction)				
						# Prepare the response to be returned to the client
				#response = jsonify({'prediction': prediction})				
				# Return the response
				#return response
			except ValueError:
				return jsonify({'error': 'Invalid input data. Please check your input and try again.'})
		else:
		    return jsonify({'error': 'Expected a JSON request'})        
	except Exception as e:
		return jsonify({'error': str(e)})

#Create an instance of the ClientApi class
api = ClientApi()

#Run the application
if __name__ == '__main__': 
	port = int(os.environ.get("PORT", 5000)) 
	app.run(host='0.0.0.0', port=port)
