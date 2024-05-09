import pandas as pd
import matplotlib.pyplot as plt

data = [["r/singapore", 411, 163, 164],
        ["r/SingaporeRaw", 170, 77, 69] 
        ]

my_colour = ['green', 'blue', 'red']

df = pd.DataFrame(data, columns=["Subreddit", "Positive", "Neutral", "Negative"])

ax = df.plot(x="Subreddit", y=["Positive", "Neutral", "Negative"],
             kind='bar', figsize=(15,10), color=my_colour)

# Annotate each bar with its respective value
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

# Adjust x-axis label rotation
plt.xticks(rotation=0)

# Add title to the graph
plt.title('Keyword: elite')

plt.show()