from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def Porfolio():
	return render_template('Portfolio.html')

@app.route("/Python")
def Python():
	return render_template('Python.html')
if __name__ == "__main__":
	app.run()
	
	
