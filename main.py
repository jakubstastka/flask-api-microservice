from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})


@app.route("/hello/<string:name>/")
def hello(name):
    return jsonify({"message": f"Hello there, {name.capitalize()}!"})


@app.route("/numbers/", methods=["POST"])
def numbers():
    nums = request.json
    return jsonify({"sum": sum(nums), "average": sum(nums)/len(nums), "max": max(nums), "min": min(nums)})


@app.route("/dict2list/", methods=["POST"])
def dict2list():
    request_dict = request.json
    return jsonify({"result": [item for item in request_dict.values()]})


@app.route("/storytime/", methods=["POST"])
def storytime():
    person_info = request.json

    try:
        fullname = f"{person_info['name'].capitalize()} {person_info['lastname'].capitalize()}"
        person_year = datetime.datetime.now().year - person_info["age"]

        storytime = f"{fullname} was born around {person_year}, and has {len(person_info['favourite_animals'])} favourite animals: {', '.join(person_info['favourite_animals'])}."

    except KeyError as error:
        return jsonify({"error": f"Cannot complete storytime, because this was not provided: {error}"})

    return jsonify({"storytime": storytime})


if __name__ == '__main__':
    app.run()
