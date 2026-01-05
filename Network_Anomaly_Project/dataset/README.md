# Network Traffic Anomaly Detection Using Machine Learning

## Project Overview
This project detects abnormal or suspicious network traffic using machine learning techniques. 
The model learns normal network behavior and identifies deviations as anomalies.

## Dataset
- KDD Cup 99 (10% subset)
- Network intrusion detection dataset

## Methodology
- Data cleaning and preprocessing
- Feature scaling using StandardScaler
- Anomaly detection using Isolation Forest
- Visualization of detected anomalies

## Tools & Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## How to Run the Project
1. Install required libraries:
   pip install -r requirements.txt

2. Run the project:
   python anomaly_detection.py

## Output
- Identifies normal and anomalous network traffic
- Displays anomaly distribution graph

## Use Case
- Cybersecurity monitoring
- Network intrusion detection
- Digital forensics analysis

## Dataset Access
Due to GitHub file size limitations, the dataset is not included in this repository.

Dataset Name: KDD Cup 99 (10% subset)

Download Link:
https://www.kaggle.com/datasets/galaxyh/kdd-cup-1999-data

After downloading, place the file as:
dataset/kddcup.csv

