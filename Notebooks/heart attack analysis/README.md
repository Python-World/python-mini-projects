# Heart Attack Analysis & Prediction  

# Dataset Information

Heart attacks result in severe medical conditions that may be fatal if not handled correctly. Due to the current lifestyle, heart attacks are much more often than in the past. With the help of modern-day technologies and the capacity of storing the data, we can create a heart attack prediction mechanism that would allow us to measure the chances of having a heart attack on a person.

### Attribute Information:

Input variables: \
1 - Age : Age of the patient \
2 - Sex : Sex of the patient \
3 - exang: exercise induced angina (1 = yes; 0 = no) \
4 - ca: number of major vessels (0-3) \
5 - cp : Chest Pain type chest pain type \
<ul>
  <li> Value 1: typical angina </li>
  <li> Value 2: atypical angina </li>
  <li> Value 3: non-anginal pain </li>
  <li> Value 4: asymptomatic </li>
</ul>

6 - trtbps : resting blood pressure (in mm Hg) \
7 - chol : cholestoral in mg/dl fetched via BMI sensor \
8 - Trihalomethanes-> Amount of Trihalomethanes in μg/L \
9 - fbs : (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false) \
10 - est_ecg : resting electrocardiographic results
<ul>
  <li> Value 0: normal </li>
<li> Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) </li>
  <li> Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria </li>
</ul>
11 - thalach : maximum heart rate achieved

Output variable (based on sensory data): \
10 - target : 0= less chance of heart attack 1= more chance of heart attack


# Libraries


<li>pandas
<li>matplotlib
<li>seaborn
<li>plotly
<li>scikit-learn
<li>xgboost
  
# Algorithm
<li>XGBoost</li>
  
  <br>
  
**Model Accuracy:** 80.00

