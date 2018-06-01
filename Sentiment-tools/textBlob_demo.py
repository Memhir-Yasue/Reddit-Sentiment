from textblob import TextBlob

text = TextBlob("He definitely has mental problems. That man could be President.")
print(text.sentiment)
print(text.sentiment.polarity)