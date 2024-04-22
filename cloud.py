import nltk
from collections import Counter
from nltk.corpus import webtext
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
with open("/app/data/paragraphs.txt", "r") as file:
    dataset_content = file.read()

tokenize_words = word_tokenize(dataset_content)

tokenize_words_without_stop_words = []

for word in tokenize_words:
    if word not in stop_words:
        tokenize_words_without_stop_words.append(word)
print("Stop words which got removed from the paragraph:" , set(tokenize_words)-set(tokenize_words_without_stop_words))


words = Counter(tokenize_words_without_stop_words)
for word , count in words.items():
    print(f"{word} ,{count}")

