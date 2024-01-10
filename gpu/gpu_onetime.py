from transformers import pipeline
import sys

def load_model():
    model = pipeline(task="sentiment-analysis", model="philschmid/tiny-bert-sst2-distilled")
    return model

def predict(model, text):
    return model(text)

def main(text):
    model = load_model()
    prediction = predict(model, text)
    print(f"Text: {text}")
    print(f"Sentiment: {prediction[0]['label']}, Confidence: {prediction[0]['score']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a text for sentiment analysis")
        sys.exit(1)

    text = sys.argv[1]
    main(text)