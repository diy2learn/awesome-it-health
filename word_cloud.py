from yaml import safe_load

with open("wrist_pain.yml", "r") as file:
    records = safe_load(file)

print(records)
raw_text = " ".join([t.lower() for el in records.values() for t in el["suggestions"]])
to_skip = ["wrist", "wrists", "using", "keep", "take", "control", "avoid"]
filtered_words = [w for w in raw_text.split(" ") if w not in to_skip]
text = " ".join(filtered_words)
print("text: ", text)

import matplotlib.pyplot as plt
from wordcloud import WordCloud
word_cloud = WordCloud(collocations=False, background_color = 'white').generate(text)

plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
