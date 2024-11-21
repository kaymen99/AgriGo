import os
import pickle
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def get_model(path):
    model = load_model(path, compile=False)
    return model

def img_predict(path, crop):
    data = load_img(path, target_size=(224, 224, 3))
    data = np.asarray(data).reshape((-1, 224, 224, 3))
    data = data * 1.0 / 255
    model = get_model(os.path.join(BASE_DIR, 'models', 'DL_models', f'{crop}_model.h5'))
    if len(crop_diseases_classes[crop]) > 2:
        predicted = np.argmax(model.predict(data)[0])
    else:
        p = model.predict(data)[0]
        predicted = int(np.round(p)[0])
    return predicted

def get_diseases_classes(crop, prediction):
    crop_classes = crop_diseases_classes[crop]
    return crop_classes[prediction][1].replace("_", " ")

def get_crop_recommendation(item):
    scaler_path = os.path.join(BASE_DIR, 'models', 'ML_models', 'crop_scaler.pkl')
    model_path = os.path.join(BASE_DIR, 'models', 'ML_models', 'crop_model.pkl')

    with open(scaler_path, 'rb') as f:
        crop_scaler = pickle.load(f)
    with open(model_path, 'rb') as f:
        crop_model = pickle.load(f)

    scaled_item = crop_scaler.transform(np.array(item).reshape(-1, len(item)))
    prediction = crop_model.predict(scaled_item)[0]
    return crops[prediction]

def get_fertilizer_recommendation(num_features, cat_features):
    scaler_path = os.path.join(BASE_DIR, 'models', 'ML_models', 'fertilizer_scaler.pkl')
    model_path = os.path.join(BASE_DIR, 'models', 'ML_models', 'fertilizer_model.pkl')
    
    with open(scaler_path, 'rb') as f:
        fertilizer_scaler = pickle.load(f)
    with open(model_path, 'rb') as f:
        fertilizer_model = pickle.load(f)

    scaled_features = fertilizer_scaler.transform(np.array(num_features).reshape(-1, len(num_features)))
    cat_features = np.array(cat_features).reshape(-1, len(cat_features))
    item = np.concatenate([scaled_features, cat_features], axis=1)
    prediction = fertilizer_model.predict(item)[0]
    return fertilizer_classes[prediction]

crop_diseases_classes = {'strawberry': [(0, 'Leaf_scorch'), (1, 'healthy')],

			   'patato': [(0, 'Early_blight'),
				 (1, 'Late_blight'),
				 (2, 'healthy')],

			   'corn': [(0, 'Cercospora_leaf_spot Gray_leaf_spot'),
				 (1, 'Common_rust_'),
				 (2, 'Northern_Leaf_Blight'),
				 (3, 'healthy')],

			   'apple': [(0, 'Apple_scab'),
				 (1, 'Black_rot'),
				 (2, 'Cedar_apple_rust'),
				 (3, 'healthy')],

			   'cherry': [(0, 'Powdery_mildew'),
				 (1, 'healthy')],

			   'grape': [(0, 'Black_rot'),
				 (1, 'Esca_(Black_Measles)'),
				 (2, 'Leaf_blight_(Isariopsis_Leaf_Spot)'),
				 (3, 'healthy')],

			   'peach': [(0, 'Bacterial_spot'), (1, 'healthy')],

			   'pepper': [(0, 'Bacterial_spot'),
				 (1, 'healthy')],
				
			   'tomato': [(0, 'Bacterial_spot'),
				 (1, 'Early_blight'),
				 (2, 'Late_blight'),
				 (3, 'Leaf_Mold'),
				 (4, 'Septoria_leaf_spot'),
				 (5, 'Spider_mites Two-spotted_spider_mite'),
				 (6, 'Target_Spot'),
				 (7, 'Tomato_Yellow_Leaf_Curl_Virus'),
				 (8, 'Tomato_mosaic_virus'),
				 (9, 'healthy')]}

crop_list = list(crop_diseases_classes.keys())


crops = {'apple': 1, 'banana': 2, 'blackgram': 3, 'chickpea': 4, 'coconut': 5, 'coffee': 6, 'cotton': 7, 'grapes': 8, 'jute': 9, 'kidneybeans': 10, 'lentil': 11, 'maize': 12, 'mango': 13, 'mothbeans': 14, 'mungbean': 15, 'muskmelon': 16, 'orange': 17, 'papaya': 18, 'pigeonpeas': 19, 'pomegranate': 20, 'rice': 21, 'watermelon': 22}

crops = list(crops.keys())

soil_types = ['Black', 'Clayey', 'Loamy', 'Red', 'Sandy']
Crop_types = ['Barley', 'Cotton', 'Ground Nuts', 'Maize', 'Millets', 'Oil seeds', 'Paddy', 'Pulses', 'Sugarcane', 'Tobacco', 'Wheat']

fertilizer_classes = ['10-26-26', '14-35-14', '17-17-17', '20-20', '28-28', 'DAP', 'Urea']
