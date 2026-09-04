from flask import Flask,jsonify,request
app = Flask(__name__)

tasks_list = [
    {"Serial No.": 1, "Title": "Complete DST Assignment", "Completed": False},
    {"Serial No.": 2, "Title": "Revise Statistics", "Completed": False},
    {"Serial No.": 3, "Title": "Submit Documents", "Completed": False}
]

@app.route('/')
def home():
	return jsonify({"Message":"The Backend is working"})

@app.route('/tasks',methods=["GET"])
def get_tasks():
	return jsonify(tasks_list)

@app.route('/tasks', methods =["POST"])
def add_task():
	data = request.get_json()
	new_task = {
			"Serial No.":len(tasks_list) + 1,
			"Title" :data["Title"],
			"Completed": False
		   }

	tasks_list.append(new_task)	
	return jsonify(new_task),201
if __name__ == "__main__":
	app.run(host= "0.0.0.0", port = 5000)

