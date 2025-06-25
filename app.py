from flask import Flask, render_template, request, jsonify
from responses import get_bot_response

app=Flask(__name__)

@app.route("/chatbot")
def chatbot():
    return render_template("index.html")


@app.route("/chat",methods=["POST"])
def chat():
    user_input=request.json["message"]
    response = get_bot_response(user_input)
    return jsonify({"response":response})

if __name__=="__main__":
    app.run(debug=True)

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
