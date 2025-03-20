from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.np_extractors import ConllExtractor

extractor = ConllExtractor()
analyzer = NaiveBayesAnalyzer()

phrase = "You can extract topics from phrases using TextBlob"

topics = TextBlob(phrase, analyzer=analyzer).noun_phrases

print(topics)