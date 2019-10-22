import json
from marshmallow import Schema, fields
from flask import Flask, make_response, jsonify
app = Flask(__name__)


class Person:
    def __init__(self, name, age, cool):
        self.name = name
        self.age = age
        self.cool = cool


class PersonSchema(Schema):
    name = fields.Str()
    age = fields.Integer()
    cool = fields.Boolean()


@app.route("/test")
def test():
    people = []

    person = Person(name="Franco", age=23, cool=True)
    person2 = Person(name="Lucas", age=26, cool=True)

    people.append(person)
    people.append(person2)

    schema = PersonSchema(many=True)
    result = schema.dump(people)

    return make_response(jsonify(result), 200)


if __name__ == '__main__':
    app.run(debug=True)
