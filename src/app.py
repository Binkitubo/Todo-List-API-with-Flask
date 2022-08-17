#To create a server, we need to add the following two lines to any python file
from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request.data)

    print("Incoming request with the following body", request_body)    
    todos.append(decoded_object)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    print("This is the position to delete: ", position)    
    todos.pop(position)
    return jsonify(todos)


#These two lines should always be at the very end of your file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)