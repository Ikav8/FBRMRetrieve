from flask import Flask
import GetData
app = Flask(__name__)
@app.route('/')
def index():
	return GetData.getDataFromFBRM()
if __name__ == "__main__":
	app.run()