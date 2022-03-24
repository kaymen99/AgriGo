<div id="top"></div>

# AgriGo

![Capture d’écran 2022-03-23 à 23 56 34](https://user-images.githubusercontent.com/83681204/159978827-fccf752e-2d36-4dc3-a15a-ce3a57e90165.png)

<!-- ABOUT THE PROJECT -->


This is a web application based on machine/deep learning models for crop disease detection and fertilizer/crop recommendation

### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Tensorflow](https://www.tensorflow.org)
* [scikit-learn](https://scikit-learn.org/stable/)
* [bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#motivation">Motivation</a></li>
    <li><a href="#motivation">Features</a></li>
    <li><a href="#how-to-use">How to use</a></li>
    <li><a href="#dataset">Dataset</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- Motivation -->
## Motivation




<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Features -->
## Features

<div style="display:flex;align-items:center;">
  <img src="https://user-images.githubusercontent.com/83681204/159989052-08ae92b6-015d-4c63-b9d5-9fcb0579caeb.png" width="700px" heigth="500px">
</div>

<br/>
<ul>
  <li><b>Crop recommendation: </b></li>
    By using the soil data such as: NPK ratios, moisture, temperature and amount of rainfall in the field region the model can recommend the best crop to grow
  
  <li></b>Fertilizer recommendation: </b></li>
    With the given soil data(type, temparture, Ph,...) and NPK ratios and the crop type, the app allow the user to know the best fertilzer to use for ensuring the good health of crops and thus maximazing the global yield of the field

  <li></b>Crop diseases detection: </b></li>
    The user need to give the crop image and it's type and the image recognition models will predict if the plant is healthy or not.
  
</ul>

<br/>
<div style="display:flex;align-items:center;">
  <img src="https://user-images.githubusercontent.com/83681204/159994252-6e44cd8e-4d20-4dcb-9e22-c0e35756fe1c.png" width="500px" heigth="300px">
 
  <img src="https://user-images.githubusercontent.com/83681204/159994452-d6a14dc9-d94f-4beb-8778-6ecdfe48f453.png" width="500px" heigth="300px">
  
</div>

<br/>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE  -->
## How to Use

To use this project you need to follow this steps:

* Make sure python3 is installed if not you can get it [here](https://www.python.org/downloads/)

* Clone this repository:
   ```sh
   git clone https://github.com/Aymen1001/AgriGo.git
   cd AgriGo/AgriGo
   ```

* Install all the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
* And finally run this command:
   ```sh
   python app.py
   ```   
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- data -->
## Dataset

The datasets used for this project are from kaggle:

* [Crop Recommendation](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
* [Fertilizer Recommendation](https://www.kaggle.com/datasets/gdabhishek/fertilizer-prediction)
* [Crop Diseases images dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

   
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Contact -->
## Contact

If you have any question or problem running this project just contact me: aymenMir1001@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

