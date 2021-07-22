from flask import Flask, json, jsonify, request

app = Flask(__name__)
contacts = [
    {
        'id' : 1,
        'name' : 'Lataksh',
        'contact' : '9754612134',
        'done' : False
    },
    {
        'id' : 2,
        'name' : 'Vijay',
        'contact' : '5421346714',
        'done' : False
    },
    {
        'id' : 3,
        'name' : 'Kiran',
        'contact' : '2431674558',
        'done' : False
    }]

@app.route("/addTask", methods = ["POST"])

def addTask():
    if not request.json:
        return jsonify({
            "status" : "Error",
            "message" : "Errr! Please provide the data"
        }, 400)
    
    task = {
        'id' : contacts[-1]['id'] + 1,
        'name' : request.json['name'],
        'contact' : request.json.get('contact', ""),
        'done' : False
    }

    contacts.append(task)
    
    return jsonify({
        "status" : "Success",
        "message": "Task Added Sucessfully"
    })

@app.route("/getcontacts")

def getcontacts():
    return jsonify({
        "data" : contacts
    })





# Running the Code below
if __name__ == "__main__":
    app.run(debug=True)