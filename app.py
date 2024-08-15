from flask import Flask, jsonify, request
import requests
import time

app = Flask(__name__)

WINDOW_SIZE = 10
WINDOW = []

def fetch_numbers(number_id):
    url = f"http://127.0.0.1:5001/numbers/{number_id}"
    try:
        response = requests.get(url, timeout=0.5)  
        if response.status_code == 200:
            numbers = response.json().get('numbers', [])
            return numbers
        else:
            return []
    except requests.exceptions.Timeout:
        return []

def is_unique(number):
    return number not in WINDOW

def update_window(new_numbers):
    global WINDOW
    for number in new_numbers:
        if is_unique(number):
            if len(WINDOW) >= WINDOW_SIZE:
                WINDOW.pop(0) 
            WINDOW.append(number)

def calculate_average():
    if len(WINDOW) == 0:
        return 0
    return sum(WINDOW) / len(WINDOW)

# API Route
@app.route('/numbers/<number_id>', methods=['GET'])
def get_average(number_id):
    prev_window_state = WINDOW.copy()
    
    new_numbers = fetch_numbers(number_id)
    update_window(new_numbers)
    avg = calculate_average()
    response = {
        "windowPrevState": prev_window_state,
        "windowCurrState": WINDOW,
        "numbers": new_numbers,
        "avg": round(avg, 2)
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)