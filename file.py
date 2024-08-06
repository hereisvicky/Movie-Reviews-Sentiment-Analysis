

# link https://www.kaggle.com/code/payamamanat/imdb-movies
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
import re
pd.set_option('display.max_columns' , None)
import warnings
warnings.filterwarnings('ignore')



dataset = pd.read_csv('IMBD.csv.zip')
df = pd.DataFrame(dataset)
print('View of dataset:')
df.sample(7)

class color :
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
df.describe(include='all')
df.info()
def dataset_details(dataset):
    feature = []
    dtype = []
    unique =[]
    count = []
    missing_values=[]
    missing_percentage = []

    for column in df.columns :
        feature.append(column)
        dtype.append(df[column].dtype)
        unique.append(df[column].unique())
        count.append(len(df[column]))
        missing_values.append(df[column].isnull().sum())
        missing_percentage.append(round((df[column].isnull().sum()/len(df))*100 , 2))
    # The following line was incorrectly indented, it should be at the same level as the 'for' loop
    details = pd.DataFrame({
        'Feature' : feature ,
        'Type' : dtype ,
        'Count' : count ,
        'Unique' : unique ,
        "Missed Values" : missing_values,
        'Missed Percent%' : missing_percentage,

    })

    return details



dataset_details(df)

df.duplicated().sum()
sns.set(style="darkgrid",font_scale=1.5)
plt.figure(figsize=(14,8))
sns.heatmap(df.isnull(),cmap="summer")
plt.xlabel('Features')
plt.title('Missing values')
plt.show()
df.fillna('NAN' , inplace=True)
# df['year'] = df['year'].apply(lambda x : x.split('(')[1].split(')')[0])
df['year'] = df['year'].apply(lambda x : re.sub('[^0-9NAN-]' , ' ' ,x))
df['year'] = df['year'].apply(lambda x : re.sub(r'[ ]+' , ' ' , x))
df.head(6)
print(f'{color.BOLD}Unique years is :  ' , len(df.year.unique()))
print('*' * 30)
df.year.unique()
hist = px.histogram(df['year'] , x='year' , title='Year distribution',color='year' , height=700 , width=900)
hist.show()
print(f'{color.BOLD}Most repeated certificate')
print('*' * 30)
df.certificate.value_counts().to_frame().style.highlight_max(color='red')
c_hist = px.histogram(df['certificate'],x='certificate' ,title='Certificate Districution' ,  color='certificate')
c_hist.show()
print(f'{color.BLUE}The len of unique duration is : {color.END}{len(df.duration.unique())}')
print('***' * 30)
df['duration'].unique()
df['duration'] = df['duration'].apply(lambda x : x.split(' ')[0])
df.rename(columns={'duration' : 'duration(min)'} , inplace=True )
df['duration(min)'].replace({'NAN': 0} , inplace=True)
df['duration(min)']=df['duration(min)'].astype(int)
D_hist = px.histogram(df['duration(min)'] , x='duration(min)' , title='Duration' , color='duration(min)')
D_hist.show()
print(f'{color.BOLD}The number of movies with less duration that 60 minuts : ', len(df[df['duration(min)']<60]))
print('***' * 30)
df[df['duration(min)']<60]
most_duration = df.sort_values(by='duration(min)' , ascending=False)[['title','duration(min)']][:20]
plt.figure(figsize=(15,15))
sns.barplot(x=most_duration['duration(min)'], y=most_duration['title'])
plt.title('Highest duration' , color='gray' ,size=30)
plt.show()
G_hist = px.histogram(df['genre'] , x='genre' , title='Genre' , color='genre' , height=600 , width=2000)
G_hist.show()
df['rating'].replace({'NAN':0} , inplace=True)
df['rating'] = df['rating'].astype(float)
print(f'{color.BOLD}Ordered based on highest rating')
print('**' * 30)
df.sort_values(by='rating' , ascending=False)
df.sort_values(by='rating' , ascending=False)[['title' , 'rating']].head(10).plot(kind='bar',
                                                                                  x='title' , y='rating',
                                                                                  figsize=(10,5),
                                                                                  title='Hieghest 10 rating',
                                                                                 )
plt.xlabel('Movie' , c='gray')
plt.ylabel('Score' , c='gray')
plt.xticks(rotation = 80 , color='k')
plt.show()
df.sort_values(by='rating' , ascending=False)[['title' , 'rating' , 'description']].head(10)
dataset["stars"]= dataset["stars"].apply(lambda x : re.sub('[^a-zA-Z]' ,',' ,x))
dataset['stars']= dataset['stars'].apply(lambda x : re.sub(r'\,+' , ',' , x))
dataset.sort_values(by='rating' , ascending=False)[['title' , 'rating' , 'stars']][:20]
df['votes'].replace({'NAN':'0'} , inplace=True)
df['votes'] = df['votes'].apply(lambda x : re.sub('[^0-9]', '' , x))
df['votes'] = df['votes'].astype(int)
df.sort_values(by='votes' , ascending=False)[['title' , 'rating' , 'votes']][:20].plot(kind='bar' ,
                                                                                       x='title' ,
                                                                                       y='votes',
                                                                                     color='pink')
plt.xlabel('Movies')
plt.ylabel('votes')
plt.title('Most votes', size=20)
plt.show()
