  
import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

client = language.LanguageServiceClient()

print("===========================================================")

with open('reviews.json') as f:
  data = json.load(f)
  for i in data:
    text = data[i]["Text "]
    location = data[i]["Location"]
# The text to analyze
    document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
    sentiment= client.analyze_sentiment(document=document).document_sentiment

    print('Location: {}'.format(location))
    print('Sentiment: {0:.3f}, {0:.3f} \n'.format(sentiment.score, sentiment.magnitude))
print("===========================================================")