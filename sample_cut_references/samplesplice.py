# shared for reference only - using the original 2Gb file not included
# on GitHub due to size restrictions

import pandas as pd

path = "Climate_Twitter.csv"

df = pd.read_csv(path)

deniers = df.loc[df['stance'] == 'denier', ['created_at', 'lat', 'lng', 'topic', 'sentiment', 'stance', 'gender', 'temperature_ave', 'aggressiveness']]

print(deniers.shape)

deniers.to_csv('Climate_Deniers.csv', index=False)

cols = ["created_at", "lat", "lng", "sentiment", "topic", "stance", "gender", "aggressiveness"]

df_cut = df[cols]

sample = df_cut.sample(frac = 0.05)

print(sample.shape)

sample.to_csv("sample_05.csv", index=False)