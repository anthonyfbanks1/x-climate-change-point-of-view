# x-climate-change-point-of-view
The purpose of our project was to analyze climate change point of view through X user post data, primarily focusing on US-based users and users who deny the existence of climate change, to see what patterns we could find.

Our Initial Research Questions:
What trends, if any, are present in climate related tweets? Has the stance, sentiment, or aggression of Tweets changed significantly in the 2010s?

What trends might we uncover by isolating the tweets denying climate change? Are there any patterns to find that would help make sense of the spread of misinformation on social media?

What does X activity look like before and after a major natural disaster?

Project Structure
You can find the main script for this project in the root folder called "Final_Project.ipynb", along with the presentations slides called "Final_Project_Slides.pptx". 

Raw data resources can be found in the Resources folder, and in the subfolder "sample_cut_references" we have included some of the .py files used to cut the original dataframe down to usable pieces. These won't function since they are referencing the original 2GB file not included on GitHub due to filesize constraints but are included for context only. You can also find the individual data visualizations in the Images folder.

Our Original Datasets:
Climate Change Twitter Data Set & Disasters Data Set
"Abstract: This work creates and makes publicly available the most comprehensive dataset to date regarding climate change and human opinions via Twitter. It has the heftiest temporal coverage, spanning over 13 years, includes over 15 million tweets spatially distributed across the world, and provides the geolocation of most tweets. Seven dimensions of information are tied to each tweet, namely geolocation, user gender, climate change stance and sentiment, aggressiveness, deviations from historic temperature, and topic modeling, while accompanied by environmental disaster events information. These dimensions were produced by testing and evaluating a plethora of state-of-the-art machine learning algorithms and methods, both supervised and unsupervised, including BERT, RNN, LSTM, CNN, SVM, Naive Bayes, VADER, Textblob, Flair, and LDA."

Dimitrios Effrosynidis, Alexandros I. Karasakalidis, Georgios Sylaios, Avi Arampatzis, The climate change Twitter dataset, Expert Systems with Applications, Volume 204, 2022, 117541, ISSN 0957-4174

For more information on the original dataset used, please read the documentation and references found here and here

Analysis:
Looking at Stance, Aggression, and Sentiment Over Time
Question1_Trends
The percent of aggressive tweets is gradually decreasing over time. The percentage of tweets that support the belief of climate change is increasing overall. The average sentiment for each month fluctuates and contains smaller trends.

Before early 2014, there is higher variability in the data and any trends present. Starting in early 2014, some clear and more steady and positive trends appear in the percentage of tweets that support climate change and that have positive sentiment. Separate research shows that in 2014, the world experienced many climate related natural disaster starting with wildfires in early 2014 in Australia and heat waves in Canada and Alaska.

Starting in late 2015, the sentiment switches from steadily increasing, to steadily decreasing. The percentage of tweets supporting climate change stops increasing and begins to decrease. The percentage of aggressive tweets stops decreasing, and increases slightly. These trends end in mid 2017. The start of these trends coincides with the ramping up of the 2016 election cycle which had climate change as a major devisive talking point/issue. The trend ends in mid-late 2017. A notible climate change event that may have had an impact was the US leaving the Paris Climate Agreement in June 2017.

A large jump in the average sentiment and the percentage of tweets that believe in climate change occurs in the Fall of 2017, after which the data becomes more variable. The percentage of aggressive tweets begins to decrease again.

Comparing the Number of Tweets from Users and Their Stances
Q1_Stance_Numbers
The number of tweets about climate change decreases from 2019 to 2012. After 2012 there is a rapid increase in the number of tweets per year about climate change. The increase appears exponential. The increase in the number of tweets could be due to an increase in the numner of consumers joining Twitter or the increased politcal attention to climate change starting in 2015/2016 in the 2016 election cycle. A rapid increase could also be related to Greta Thunberg entering the international stage in 2018 and garnering a large Twitter following.

The second graph was made with the same data but uses a logarithmic scale to better examine how the number of tweets changed over time. It is clear that the changes are explonential. It is less clear how the number of believer tweets is changing compared to the number of denier tweets as the logarithmic scale can be misleading.

Taking a Closer Look at Stance Over Time
Q1_Regression
There is growth in the percentage of believer tweets, but the rate is slowing down. There is a decrease in the percentage of tweets that deny climate change.

If these trends continue, the percent of tweets from believers will reach 100% in 12-15 years, and the percentage of denier tweets will reach 0% in 7-8 years. The descrepancy in time could be the neutral tweets. However, are these results due to deniers changing their minds or are deniers leaving Twitter? Or are the number of people joining Twitter who believe in climate change and are active dwarf the number of deniers joning/being active on Twitter? More research and analysis is required to answer these questions.

Geographic Trends in Early Climate Denier Tweets
Q2_Geographic_Trends
Climate denial has existed since the late ninties, well before Twitter first became publicly available in 2006. From our dataset, we learned that tweets about climate denial found their way onto the platform almost from the beginning, with the first tweet from a climate denier on the subject sent in December of that same year.

The above map shows the geolocation of the first 5 tweets about climate change from the stance of "Denier" on each subtopic as shown in the legend to the right. The locations highlighted with a white circle are the first tweets on each subject, to show the origin point of the conversation.

What we notice is that most of tweets originate in coastal or near-coastal regions. From the above analysis, we can also see that many of these tweets are from large, highly populated cities as well. 7 of the first 10 tweets are from the US, 3 are from the same state of North Carolina, and 2 were sent from the same city of Charlotte.

There doesn't seem to be any major discernible pattern to the spread of the topics geographically, and this isn't very surpising given the medium of social media. It's difficult to determine if this kind of distribution is related to the subject matter of climte change specifically, or to Twitter in general, but it does seem to be an interesting pattern that may merit further study.

Trends in Climate Denier Sentiment/Aggression Over Time
Q2_Deniers_Sentiment
This graph shows the total number of tweets from the stance "Denier" across the timeframe of the full dataset, grouped by sentiment level & aggression. "Sentiment" was a somewhat difficult concept to grasp from the context of the original dataset documentation, but seems to refer to the sentiment of the tweet itself rather than the user's sentiment toward climate change, which is why we see a number of positive sentiment tweets from climate deniers, which would otherwise seem to be an oxymoron. This means that positive sentiment is associated with people communicating with someone who agrees with them, and negative sentiment would be associated with arguments and disagreements.

What we see from the above graph is that both high and low sentiments are consistently favored across the whole timeframe, where average sentiments consistently remain along the bottom and less common. This is what we would expect to see on social media sites, especially during times of high engagement, either strong positive or negative emotions being the norm when people are communicating with others, and a lot less neutral statements.

Another slightly more subtle pattern is that those with "Very Low" sentiment have a tendency to be aggressive more often than they are non-aggressive, particularly when the number of tweets are higher, or during "high engagement" time periods.

The dramatic increase in tweets after the beginning of the 2016 presidential campaign is common to users of all stances, suggesting a boost in popularity in Twitter at that point, or at least in the discussion of the subject of climate change on Twitter, but it is not limited to only deniers of climate change only. This suggests that this graph shows us either the shape of the conversation around climate change, the shape of the popularity of Twitter in general, or some combination of both.

ANOVA: Relationship Between Stance and Sentiment
ANOVA_Results
Finally, the above graph shows the results of an ANOVA test to check if there is a relationship between Twitter user stance and sentiment levels. For this test we returned to the original dataset and took a random sampling of 5% of the total worldwide data (due to filesize constraints) in order to compare all stances.

What we see is a clear, significant difference in the mean sentiment of denier posts in comparison to all other posts from both believers and those expressing no stance on the subject of climate change. These latter two both average a neutral sentiment, as would be expected, where the mean of the denier tweets falls much lower. We also found that denier tweets with a sentiment above about 0.85 were likely to be outliers.

While this result is dramatic, it isn't necessarily surprising. Denier tweets were about 8% of the total 15 million data points in the original dataset, and a minority group is likely to spend time debating with people who disagree with them more often than not simply due to being outnumbered. However, it could also imply that deniers are spending more time trying to convert those who disagree with them rather than communicating with those who already agree. Further study would be required to determine more information on that subject, but it is an interesting finding nonetheless.

Disaster Tweet Analysis:
Hurrican Harvey:
Q3_Hurricane
There is a significant increase of tweets after Hurricane Harvey concluded. During the storm there was an average amount of activity based on all the topics of the data that include climate change. When we break down the graph to just include the topic of 'Weather Extremes' there is an increase in acivity throughout the duration of the storm. There is an upward trend of weather and climate related tweets even two weeks after Hurricane Harvey concludes. As we recall, Hurricane Harvey was one of the more devestating hurricanes in recent memory which continues to show how these storms continue to get stronger over time.

2018 California Wildfires:
Q3_Wildfire
Looking at the data of the 2018 California Wildfire tweet activity it shows a trend up after the wildfires had concluded. Considering we really don't know the severity of a wildfire until it is contained or it has concluded, in the tweet data two weeks before the wildfire begins there is minimum tweet activity across all weather and climate topics on Twitter. It's not until the Wildfire concludes that there is a trend up in tweet acitivity acorss all climate related tweets.

2015 Wimberley Flood:
Q3_Flood
The 2015 Wimberley Floods started on May 23, 2015. The data shows that there is a uptick of tweets as the storms and flood trended up as the days went on and the flood began to affect more people. On May 28, there is a significant uptick in tweet activity. Two weeks before the flood occured, there was a decent amount of tweets related to weather and cliumate topics on twitter, with a slight dip days before the flood begins.
