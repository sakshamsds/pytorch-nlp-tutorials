from bottle import route, run
from predict import *

@route('/<input_line>')
def index(input_line):
    result = predict(input_line, 10)
    print(result.item())
    print(result)
    return {'result': result}

run(host='localhost', port=5534)