from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    amount = data['amount']
    from_currency = data['from']
    to_currency = data['to']

    # Call Frankfurter API
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    result = response.json()
    
    return jsonify({
        'converted': result['rates'][to_currency]
    })

if __name__ == '__main__':
    app.run(debug=True)
