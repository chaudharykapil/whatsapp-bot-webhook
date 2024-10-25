from  flask import Flask,request
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app=app)
@app.route("/")
def home():
    print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return "hello"

@app.route("/send-message")
def sendmessage():
    url = "https://graph.facebook.com/v20.0/457050044159442/messages"
    headers = {
        "Authorization": "Bearer EAAVRIGpZBvUQBOZBouFqYe8x11ZAGAzbpZCoZClzx7pGWx60zbiIbMfmabG2wMkFjWPYOSTcm0fZCxrqulG3VceE5t6tFVJHi0DEm7BnJDINgEHoGZCZBnMWdJZAAHHLkHX8KXUioJ2EanVasAh1Jef5WZCOy0i3eIZA50ZA3JJ2YnS1wldkiXQbqqucrdnWSpim0hz44DhYlS1RQbLjabr7SybsRNeu6gAZD",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": "918279636156",
        "type": "template",
        "template": {
            "name": "mytemplate2",
            "language": {
                "code": "en"
            },
            "components":[
                {
                    "type":"body",
                    "parameters":[
                        {
                        "type":"text",
                        "text":"Kapil Chaudhary"
                        }
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=data)

    # Print response status and body
    print(response.status_code)
    return response.text

@app.route("/callback",methods = ["GET"])
def callback():
    CHALLENGE = request.args.get("hub.challenge")
    return CHALLENGE

@app.route("/callback",methods = ["POST"])
def callbackPOST():
    print(request.json)
    return "Hii"
#app.run(debug=True)