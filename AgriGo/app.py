from flask import Flask, render_template, request, send_from_directory
import random, os
from werkzeug.utils import secure_filename
from functions import img_predict, get_diseases_classes, get_crop_recommendation, get_fertilizer_recommendation, soil_types, Crop_types, crop_list


app = Flask(__name__)
random.seed(0)
app.config['SECRET_KEY'] = os.urandom(24)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

dir_path = os.path.dirname(os.path.realpath(__file__))

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/crop-recommendation', methods=['GET', 'POST'])
def crop_recommendation():
	if request.method == "POST":
		to_predict_list = request.form.to_dict()
		to_predict_list = list(to_predict_list.values())
		to_predict_list = list(map(float, to_predict_list))
		result = get_crop_recommendation(to_predict_list)
		return render_template("recommend_result.html", result=result)
	else:
		return render_template('crop-recommend.html')

@app.route('/fertilizer-recommendation', methods=['GET', 'POST'])
def fertilizer_recommendation():
	if request.method == "POST":
		to_predict_list = request.form.to_dict()
		to_predict_list = list(to_predict_list.values())
		to_predict_list = list(map(float, to_predict_list))
		result = get_fertilizer_recommendation(
			num_features=to_predict_list[:-2],
			cat_features=to_predict_list[-2:]
		)
		return render_template("recommend_result.html", result=result)
	else:
		return render_template(
			'fertilizer-recommend.html', 
			soil_types=enumerate(soil_types),
			crop_types=enumerate(Crop_types)
		)

	
@app.route('/crop-disease', methods=['POST','GET'])
def find_crop_disease():
	if request.method=="GET":
		return render_template('crop-disease.html', crops=crop_list)
	else:
		file = request.files["file"]
		crop = request.form["crop"]

		basepath = os.path.dirname(__file__)
		file_path = os.path.join(basepath,'uploads',  secure_filename(file.filename))
		file.save(file_path)
		prediction = img_predict(file_path, crop)
		result = get_diseases_classes(crop, prediction)

		return render_template('disease-prediction-result.html', image_file_name=file.filename, result=result)

@app.route('/uploads/<filename>')
def send_file(filename):
	return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
	app.run(debug=True)