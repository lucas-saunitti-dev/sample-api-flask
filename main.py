from application import myApp
from flask import Flask, request

app = Flask(__name__)
my_application = myApp()

@app.route('/reset/', methods=['POST'])
def reset():
    my_application.reset()
    return "OK", 200

@app.route('/balance/', methods=['GET'])
def balance():
    if response := my_application.balance(account_id=request.args.get('account_id')):
        return response, 200

    return "0", 404

@app.route('/event/', methods=['POST'])
def event():
    if response := my_application.event(data=request.json):
        return response, 201
    return "0", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
