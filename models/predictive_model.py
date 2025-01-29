from transformers import pipeline

def predict_performance(feeling):
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)
    result = sentiment_analyzer(feeling)
    return result[0]

from transformers import pipeline

def analyze_sentiment(feeling):
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)
    result = sentiment_analyzer(feeling)
    return result[0]
