import pandas as pd
import random

path = "../../../../Downloads/archive/ClimateChangeTwitter.csv"

df = pd.read_csv(path)

cols = ["created_at", "lat", "lng", "sentiment", "topic", "stance", "gender", "aggressiveness"]

df_cut = df[cols]

df_NA = df_cut.loc[(df_cut["lat"]<70) & (df_cut["lat"]>15) & (df_cut["lng"]>-165) & (df_cut["lng"]<-60),:]

df_NA_sample = df_NA.sample(frac = 0.20)

df_NA_sample.to_csv("NA_sample_020.csv")