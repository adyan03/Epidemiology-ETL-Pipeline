# Hantavirus Data Preprocessing Pipeline

This repository contains an automated data cleaning script for a global Hantavirus surveillance dataset. 

In the real world, datasets often contain missing or empty values. This script is designed to automatically detect and fix these missing values so the data is ready for further analysis or Machine Learning modeling.

## 📊 Data Source
The raw dataset used in this project is obtained from Kaggle. You can access the original dataset here: [https://www.kaggle.com/datasets/deepeshkansotia/hantavirus-transmission-and-risk-dataset]

## Folder Structure

This project is structured to strictly separate raw data from cleaned data to ensure the original dataset remains safe and unaltered:

```text
├── data/
│   ├── raw/                 # Stores the original, uncleaned dataset
│   └── processed/           # Stores the cleaned dataset output
├── src/
│   └── Data_cleaner.py      # Main Python script for data cleaning
└── README.md
```
Key Features:
1. Automated Missing Value Detection: The system automatically scans for columns with missing values (NaN/Null).

2. Automated Data Imputation: Fills in the missing values in the recovery_days column using the mean (average) of the existing data.

3. Safe Storage: Automatically saves the cleaned data into the processed folder without overwriting or destroying the original raw file.
