from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/greetings/<name>', methods=['GET', 'POST'])
def greetings(name):
    if request.method == 'GET':
        # create the response
        response = {'message': f'Hello {name.capitalize()}'}
        # return the response as JSON
        return jsonify(response)

    elif request.method == 'POST':
        return jsonify({'message': 'Hello World'})


if __name__ == '__main__':
    app.run(debug=True)
