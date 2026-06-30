
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from collections import Counter

with open("article.txt", "r") as file:
    text = file.read()

sentences = sent_tokenize(text)

summary = " ".join(sentences[:3])

print("========== SUMMARY ==========")
print(summary)

with open("output.txt", "w") as out:
    out.write("========== SUMMARY ==========\n\n")
    out.write(summary)

print("\nSummary saved to output.txt")
