import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("SpotifyFeatures.csv")
def function1():

    df = pd.read_csv("SpotifyFeatures.csv")
    print(df.head)

    # null values
    print(pd.isnull(df).sum())
#function1()

def function2():
    print("Information about df: \n")
    print(df.info())
    print("Description: \n")
    print(df.describe())
#function2()

# 10 songs with least popularity:
def function3():
    sorted = df.sort_values("popularity",ascending=True).head(10)
    print(sorted)
#function3()

# Descriptive statistics:
#print(df.describe().transpose())

# Top 10 songs with popularity greater than 90:
def function4():
    popular = df.query("popularity>90",inplace = False).sort_values("popularity",ascending = False)
    print(popular[:10])
#function4()

# Artist at 18th row:
#print(df[["artist_name"]].iloc[18])

# Change the duration_ms to duration in seconds:
def function5():
    df["duration"] = df["duration_ms"].apply(lambda x: round(x/1000))
    df.drop("duration_ms", inplace = True, axis=1)
    print(df.head())
function5()

def fun():
    sample_df= df.sample(int(0.004*len(df)))
    print(len(sample_df))
#fun()

#Energy VS Loudness
def funtion7():
    sample_df= df.sample(int(0.004*len(df)))
    plt.figure(figsize=(10,6))
    sns.regplot(data=sample_df,y="loudness", x="energy").set(title="Energy VS Loudness")
    plt.show()
#funtion7()

#Acousticness VS Popularity
def funtion8():
    sample_df= df.sample(int(0.004*len(df)))
    plt.figure(figsize=(10,6))
    sns.regplot(data=sample_df,y="popularity", x="acousticness").set(title="Acousticness VS Popularity")
    plt.show()
#funtion8()

# first five rows:
#df.head()

# duration VS genre:

def fun10():
    plt.title("Duration of songs in different genres")
    sns.color_palette("rocket", as_cmap= True)
    sns.barplot(y = "genre", x= "duration", data=df)
    plt.xlabel("Duration in millisecond")
    plt.ylabel("Genre")
    plt.xticks(rotation=90)
    plt.show()
#fun10()

# Top 5 genres by popularity:
def fun11():
    sns.set_style(style = "darkgrid")
    plt.figure(figsize=(10,5))
    famous = df.sort_values("popularity", ascending = False).head(10)
    sns.barplot(y = "genre", x = "popularity", data = famous).set(title="Top 5 Genre by Popularity")
    plt.show()
fun11()