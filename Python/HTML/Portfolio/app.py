from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def Home():
	return render_template('Home.html')

@app.route("/Python")
def Home_Python():
	return render_template('Home|Python.html')

@app.route("/Javascript")
def Home_Javascript():
	return render_template('Home|Javascript.html')

@app.route("/Python/Binary")
def Home_Python_Binary():
	return render_template('Home|Python|Binary.html')

if __name__ == "__main__":
	app.run(host= '0.0.0.0')
    


    
	
	
