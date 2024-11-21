<div id="top"></div>

# AgriGo

![AgriGo Logo](https://user-images.githubusercontent.com/83681204/159978827-fccf752e-2d36-4dc3-a15a-ce3a57e90165.png)

---

## Introduction

Agriculture faces a host of challenges, from unpredictable weather conditions to soil degradation and plant diseases. These issues can reduce crop yields, increase costs, and impact food security. **AgriGo** is a web application designed to bridge the gap between modern agricultural practices and advanced technologies like machine learning and deep learning. By providing tools for crop disease detection, fertilizer recommendations, and crop selection advice, AgriGo empowers farmers to make data-driven decisions and optimize their farming processes.

---

## The Problem

Farming is becoming increasingly complex due to:
- **Limited access to expert advice** for small-scale farmers.
- **Inefficiency in crop selection** based on soil and environmental conditions.
- **Lack of knowledge about fertilizers** to use for specific soil and crop types.
- **Crop diseases going undetected**, leading to reduced productivity.

AgriGo addresses these challenges with an easy-to-use platform that integrates scientific analysis into daily agricultural practices.

---

## Features

![AgriGo Screenshot](https://user-images.githubusercontent.com/83681204/159989052-08ae92b6-015d-4c63-b9d5-9fcb0579caeb.png)

### 1. Crop Recommendation  
AgriGo analyzes soil properties like nitrogen, phosphorus, potassium (NPK) levels, moisture, temperature, and rainfall to suggest the most suitable crops for your farm. This ensures optimized crop selection tailored to your unique environmental conditions.

### 2. Fertilizer Suggestions  
Using data such as soil type, pH, temperature, and the selected crop, AgriGo provides precise fertilizer recommendations. These suggestions help maintain soil health, improve crop growth, and maximize overall yield efficiency.

### 3. Crop Disease Detection  
With just an uploaded image of your crop, AgriGo’s AI-powered image recognition system identifies diseases and evaluates plant health. This allows for quick interventions to protect your crops and prevent widespread damage.

![Disease Detection](https://user-images.githubusercontent.com/83681204/159994252-6e44cd8e-4d20-4dcb-9e22-c0e35756fe1c.png) 

![Crop Recommendation](https://user-images.githubusercontent.com/83681204/159994452-d6a14dc9-d94f-4beb-8778-6ecdfe48f453.png)

---

## How to Use

### Clone the Repository

```bash
git clone https://github.com/kaymen99/AgriGo.git
cd AgriGo
```

### Run Locally with Python (v3.8)

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server**:
   ```bash
   python app.py
   ```

Visit the app at [http://localhost:5000](http://localhost:5000).

---

### Run with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t agrigo-webapp .
   ```

2. **Run the container**:
   ```bash
   docker run -p 5000:5000 agrigo-webapp
   ```

Visit the app at [http://localhost:5000](http://localhost:5000).

---

## Dataset

The datasets used for this project are sourced from Kaggle:

- [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
- [Fertilizer Recommendation Dataset](https://www.kaggle.com/datasets/gdabhishek/fertilizer-prediction)
- [Crop Disease Image Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

---

## Built With

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [TensorFlow](https://www.tensorflow.org)
- [scikit-learn](https://scikit-learn.org/stable/)
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

---

## Contact

For questions or support, please contact me: [aymenMir1001@gmail.com](mailto:aymenMir1001@gmail.com)

---

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.