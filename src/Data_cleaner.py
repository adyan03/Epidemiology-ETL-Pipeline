import pandas as pd
from pathlib import Path
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("="*50)
print("Hantavirus Data Preprocessing Pipeline")
print("="*50)

# 1. Define File Paths
# Using .parent.parent because this script is inside the 'src' folder
BASE_DIR = Path(__file__).resolve().parent.parent 
RAW_DATA_PATH = BASE_DIR / 'data' / 'raw' / 'global_hantavirus_surveillance_dataset_2026.csv'
PROCESSED_DATA_PATH = BASE_DIR / 'data' / 'processed' / 'Hanta_Virus_clean.csv'

# 2. Load Raw Data
print("\n[1] Loading raw dataset...")
try:
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"    ✅ Successfully loaded {len(df)} rows.")
except FileNotFoundError:
    print("    ❌ ERROR: Raw CSV file not found. Please check the directory structure.")
    exit()

# 3. Detect Missing Values
print("\n[2] Scanning for missing values...")
missing_data = df.isnull().sum()
missing_columns = missing_data[missing_data > 0]

if not missing_columns.empty:
    print("    Found missing values in the following columns:")
    print(missing_columns)
else:
    print("    No missing values detected.")

# 4. Data Cleaning (Imputation Strategy)
print("\n[3] Executing data imputation process...")
if df['recovery_days'].isnull().any():
    mean_value = df['recovery_days'].mean()
    df['recovery_days'] = df['recovery_days'].fillna(mean_value)
    print("    ✅ Missing values in 'recovery_days' successfully filled with column mean.")
else:
    print("    ✅ 'recovery_days' column is already clean.")

# 5. Export Cleaned Data
print("\n[4] Exporting processed data...")
PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True) 

df.to_csv(PROCESSED_DATA_PATH, index=False)
print(f"\n✅ PIPELINE COMPLETED! Cleaned dataset saved to: {PROCESSED_DATA_PATH.name}")