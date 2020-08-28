from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def Tools():
	return render_template('index.html')
@app.route("/Binary")	
def Binary():
	return render_template('Binary.html')
@app.route("/Password")	
def Password():
	return render_template('Password.html')

if __name__ == "__main__":
	app.run()
	
	
