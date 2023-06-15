from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/greetings/', methods=['GET', 'POST'])
def greetings():
    if request.method == 'GET':
        # create the response
        response = {'message': f'Hello {name.capitalize()}'}
        # return the response as JSON
        return jsonify(response)

    elif request.method == 'POST':
        # get the data from the request
        data = request.get_json()
        print(data['name'])
        # return the response as JSON
        return jsonify({'message': 'Hello ' + data['name'].capitalize()})


if __name__ == '__main__':
    app.run(debug=True)
