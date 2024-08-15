from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_prime_numbers(count=5):
    #prime numbers
    primes = []
    num = 2
    while len(primes) < count:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def generate_fibonacci_numbers(count=5):
    #fibnocci numbers
    fibs = [0, 1]
    for _ in range(2, count):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:count]

def generate_even_numbers(count=5):
    #even numbers
    return [i for i in range(2, 2 * count + 1, 2)]

def generate_random_numbers(count=5):
    #random numbers
    return [random.randint(1, 100) for _ in range(count)]

@app.route('/numbers/p', methods=['GET'])
def get_prime_numbers():
    numbers = generate_prime_numbers()
    return jsonify({"numbers": numbers})

@app.route('/numbers/f', methods=['GET'])
def get_fibonacci_numbers():
    numbers = generate_fibonacci_numbers()
    return jsonify({"numbers": numbers})

@app.route('/numbers/e', methods=['GET'])
def get_even_numbers():
    numbers = generate_even_numbers()
    return jsonify({"numbers": numbers})

@app.route('/numbers/r', methods=['GET'])
def get_random_numbers():
    numbers = generate_random_numbers()
    return jsonify({"numbers": numbers})

if __name__ == '__main__':
    app.run(port=5001, debug=True)

