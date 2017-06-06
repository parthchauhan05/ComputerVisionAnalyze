from flask import *
import requests, json

base = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze'

app = Flask(__name__)

@app.route('/analyze',methods=['GET'])
def home():
	url = request.args['image_url']
	body = {
		'url' : url
	}
	headers = { 
				'Ocp-Apim-Subscription-Key': '3b01d6256271471091453ed6239d61f4',
				'Content-Type' : 'application/json'
	}
	response = requests.post(base,headers = headers,json = body)
	return response.text

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', debug=True, port=8000)
