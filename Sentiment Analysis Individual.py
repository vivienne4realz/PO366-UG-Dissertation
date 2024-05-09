import pandas as pd
import re
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import seaborn as sns
import warnings
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

def remove_punctuation(text): # remove punctuation function
    return re.sub(r'[^\w\s]', '', text)

input_filename = 'rSingaporeRaw_comments.txt' 
output_filename = 'rSingaporeRaw_comments_cleaned.txt'

with open(input_filename, 'r') as file:
    original_content = file.read()

modified_content = re.sub(r'\n+', '\n', original_content)
cleaned_data = remove_punctuation(modified_content)

with open(output_filename, 'w') as output_file: # write cleaned data to new file
    output_file.write(cleaned_data)

df = pd.read_csv(output_filename, header=0) # read cleaned data into dataframe using pandas
df = df.rename(columns={'Unnamed:0': 'Comments'}) # rename header to 'Comments'
df.to_csv(output_filename, index=False) # tell them that the index is false
df = pd.read_csv(output_filename) 
df.index = df.index + 1 # manually reset index to start from 1

def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # Remove @mentions, replace with blank
    text = re.sub(r'#', '', text)  # Remove the '#' symbol, replace with blank
    text = re.sub(r'RT[\s]+', '', text)  # Remove RT, replace with blank
    text = re.sub(r'https?:\/\/\S+', '', text)  # Remove hyperlinks
    text = re.sub(r':', '', text)  # Remove colons
    return text

def remove_emoji(string):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
    "]+", flags=re.UNICODE)
    return emoji_pattern.sub('', string)

def getSubjectivity(text): #Create a function to get the subjectivity
 return TextBlob(text).sentiment.subjectivity
def getPolarity(text): #Create a function to get Polarity
 return TextBlob(text).sentiment.polarity

def getInsight(score):
    if score < 0:
        return "Negative"
    elif score == 0: # elif = "else if"
        return "Neutral"
    else:
        return "Positive"

df = pd.read_csv(output_filename, header=None)
df.iloc[:, 0] = df.iloc[:, 0].apply(cleanTxt).apply(remove_emoji)
df['Subjectivity'] = df.iloc[:, 0].apply(getSubjectivity) # create a new column for what I did and add to dataframe
df['Polarity'] = df.iloc[:, 0].apply(getPolarity)
df['Insight'] = df['Polarity'].apply(getInsight)
# print(df.head(10))
df.to_csv('output_1.csv', index=True)

df2 = pd.read_csv('rsingapore.csv', header=None)

plt.title('Scholarship Sentiment Score')
plt.xlabel('Sentiment')
plt.ylabel('Scores')
plt.rcParams['figure.figsize'] = (10,10)
ax = df['Insight'].value_counts().plot(kind='bar', color= 'olive')
for p in ax.patches:
   ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')
plt.xticks(rotation=0)
plt.show()

