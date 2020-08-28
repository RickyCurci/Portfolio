from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def Angelini():
	return render_template('index.html')
	
@app.route("/img")
def Angelini_Img():
	return render_template('img.html')
if __name__ == "__main__":
	app.run()
	
