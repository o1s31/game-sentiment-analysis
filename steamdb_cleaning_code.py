import pandas as pd
import os
import numpy as np

#Write your folder name in the Terminal
game_folder = input("What is the data folder name? ")
#Write your file name in the Terminal
file_name = input("What is the data file name? (with .csv) ")
file_path = os.path.join(game_folder, file_name)

if not os.path.exists(file_path):
    print("File does not exist. Please check the folder and file name.")
    exit()

with open(file_path, 'r', encoding='utf-8') as file:
    df = pd.read_csv(file)
    print("Data loaded successfully.")
    print(df.head())

df.columns = [c.strip().replace(" ", "_").lower() for c in df.columns]
print("Columns after cleaning:", df.columns.tolist())

datetime_col = next((c for c in df.columns if "date" in c or "time" in c), None)
players_col = next((c for c in df.columns if "player" in c and "average" not in c), None)
avg_col = next((c for c in df.columns if "average" in c), None)

if datetime_col is None or players_col is None:
    print("Missing DateTime or Players column. Check your CSV format.")
    exit()

df[datetime_col] = pd.to_datetime(df[datetime_col], errors='coerce')
df = df.dropna(subset=[datetime_col]).sort_values(by=datetime_col).reset_index(drop=True)

df[players_col] = (
    df[players_col]
    .astype(str)
    .str.replace(',', '', regex=False)
    .replace('', '0')
)
df[players_col] = pd.to_numeric(df[players_col], errors='coerce').fillna(0)

if avg_col:
    df[avg_col] = (
        df[avg_col]
        .astype(str)
        .str.replace(',', '', regex=False)
        .replace('', '0')
    )
    df[avg_col] = pd.to_numeric(df[avg_col], errors='coerce').fillna(0)

df = df.dropna(subset=[players_col])
print(f"Data after cleaning has {len(df)} rows.")

df_cleaned = df[[datetime_col, players_col, avg_col]].copy()
df_cleaned = df_cleaned.reset_index(drop=True)

earliest_date = df_cleaned[datetime_col].min()
latest_date = df_cleaned[datetime_col].max()
total_days_span = (latest_date - earliest_date).days
print(f"Data covers {earliest_date.date()} to {latest_date.date()} ({total_days_span} days).")

data_range_input = input("Enter the date range (e.g., 2025.01.01-2025.09.09): ")
try:
    start_str, end_str = [s.strip().replace('.', '-') for s in data_range_input.split('-')]
    start_date = pd.to_datetime(start_str)
    end_date = pd.to_datetime(end_str)
except ValueError:
    print("Invalid date format. Please use YYYY.MM.DD format.")
    exit()

if start_date < earliest_date:
    print(f"Start date {start_date.date()} is before the earliest data date {earliest_date.date()}. Adjusting start date.")
    start_date = earliest_date
if end_date > latest_date:
    print(f"End date {end_date.date()} is after the latest data date {latest_date.date()}. Adjusting end date.")
    end_date = latest_date
if start_date >= end_date:
    print("Start date must be before end date.")
    exit()

df_cleaned = df_cleaned[
    (df_cleaned[datetime_col] >= start_date) & (df_cleaned[datetime_col] <= end_date)
].reset_index(drop=True)

print(f"Data from {start_date.date()} to {end_date.date()} included. {len(df_cleaned)} rows remain.")

cleaned_file_name = f"cleaned_{file_name.replace('.csv', f'_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}_full.csv')}"
df_cleaned.to_csv(os.path.join(game_folder, cleaned_file_name), index=False)
print(f"Cleaned full data saved to {cleaned_file_name}")
