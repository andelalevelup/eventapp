
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template, jsonify
import random


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data():
    name = request.form['name']
    email = request.form['email']

    ticketnumber = str(random.randint(1000000, 9999999))
    # write signups to a file
    with open("signups.txt", 'a') as f:
        f.write(name + ' ' + email + ' ' + ticketnumber + '\n')

    return "Your ticket number is " + str(ticketnumber)


@app.route('/api/number', methods=['GET'])
def number():
    # read a file
    with open("signups.txt", 'r') as f:
        users = f.readlines()

    num_users = str(len(users))
    return num_users


@app.route('/api/signups', methods=['GET'])
def signups():
    # read a file
    with open("signups.txt", 'r') as f:
        users = f.readlines()

    users = [user.split() for user in users]
    users_dic = {'signups': users}

    return jsonify(users_dic)



