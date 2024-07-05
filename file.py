# imdb_movies_analysis/scripts/data_loader.py

import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

# imdb_movies_analysis/scripts/visualization.py

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def plot_missing_values(df):
    sns.set(style="darkgrid", font_scale=1.5)
    plt.figure(figsize=(14, 8))
    sns.heatmap(df.isnull(), cmap="summer")
    plt.xlabel('Features')
    plt.title('Missing values')
    plt.show()

def plot_histogram(df, column, title, color, height=700, width=900):
    hist = px.histogram(df[column], x=column, title=title, color=color, height=height, width=width)
    hist.show()

# imdb_movies_analysis/scripts/analysis.py

import pandas as pd
import re

class Color:
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def dataset_details(df):
    feature = []
    dtype = []
    unique = []
    count = []
    missing_values = []
    missing_percentage = []

    for column in df.columns:
        feature.append(column)
        dtype.append(df[column].dtype)
        unique.append(df[column].unique())
        count.append(len(df[column]))
        missing_values.append(df[column].isnull().sum())
        missing_percentage.append(round((df[column].isnull().sum() / len(df)) * 100, 2))
    
    details = pd.DataFrame({
        'Feature': feature,
        'Type': dtype,
        'Count': count,
        'Unique': unique,
        'Missed Values': missing_values,
        'Missed Percent%': missing_percentage,
    })

    return details

def preprocess_data(df):
    df.fillna('NAN', inplace=True)
    df['year'] = df['year'].apply(lambda x: re.sub('[^0-9NAN-]', ' ', x))
    df['year'] = df['year'].apply(lambda x: re.sub(r'[ ]+', ' ', x))
    df['duration'] = df['duration'].apply(lambda x: x.split(' ')[0])
    df.rename(columns={'duration': 'duration(min)'}, inplace=True)
    df['duration(min)'].replace({'NAN': 0}, inplace=True)
    df['duration(min)'] = df['duration(min)'].astype(int)
    df['rating'].replace({'NAN': 0}, inplace=True)
    df['rating'] = df['rating'].astype(float)
    df['votes'].replace({'NAN': '0'}, inplace=True)
    df['votes'] = df['votes'].apply(lambda x: re.sub('[^0-9]', '', x))
    df['votes'] = df['votes'].astype(int)
    return df

# imdb_movies_analysis/requirements.txt

pandas
numpy
seaborn
matplotlib
plotly

# IMDb Movies Analysis

This project analyzes the IMDb movies dataset.

## Structure

- `data/`: Contains the dataset.
- `notebooks/`: Contains Jupyter notebooks.
- `scripts/`: Contains Python scripts for data loading, analysis, and visualization.
- `requirements.txt`: Lists the project dependencies.

## Setup

1. Clone the repository.
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the Jupyter notebook in `notebooks/imdb_analysis.ipynb`.

## Scripts

- `data_loader.py`: Functions to load the dataset.
- `visualization.py`: Functions to visualize the data.
- `analysis.py`: Functions to analyze and preprocess the data.
