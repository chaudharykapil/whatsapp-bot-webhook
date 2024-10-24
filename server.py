from  flask import Flask,request
import requests
app = Flask(__name__)

@app.route("/")
def home():
    return "hello"

@app.route("/send-message")
def sendmessage():
    url = "https://graph.facebook.com/v20.0/457050044159442/messages"
    headers = {
        "Authorization": "Bearer EAAVRIGpZBvUQBOZCr38PVJCIULCZBS0BUbqWHesURg5xkyQsEWTqdx002O1ryxGxdDpkZBiFQqg5QXDcFrgQvLJWy5MuhcZAmseDpz3YJJdqNG5MU2yJZCcAleS41F5BfYyKUVObtECyxSTSebPUOd1sXPG0nSWWfX3cxZAKsBrAWLGtmtc8h01RrrZAgTWCnCLps3UGIESZBDgAZCe5K1YqRhmHhhtY0ZD",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": "918279636156",
        "type": "template",
        "template": {
            "name": "mytemplate",
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

@app.route("/callback")
def callback():
    CHALLENGE = request.args.get("hub.challenge")
    return CHALLENGE
#app.run(debug=True)