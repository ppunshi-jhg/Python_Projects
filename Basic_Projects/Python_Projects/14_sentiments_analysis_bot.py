from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float
    
def get_mood(input_text: str, * , sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity
    # Textblob uses a scale from -1.0 (very negative) to 1.0 (very positive), it takes the input text and returns a polarity score.
    # Define mood thresholds
    
    friendly_threshold: float = sensitivity
    hostile_threshold: float = -sensitivity
    
    if polarity >= friendly_threshold:
        return Mood('😊', polarity)
    elif polarity <= hostile_threshold:
        return Mood('😠', polarity)
    return Mood('😐', polarity)

def run_bot():
    while True:
        print(f"Bot: Enter some text and I will perform a sentiment analysis on it.")
        user_input: str = input('You: ')
        if user_input.lower() in ["exit", "quit", "stop"]:
            print("Bot: Goodbye!")
            break
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f"Bot: Your mood is {mood.emoji} with a sentiment score of {mood.sentiment:.1f}")
        
if __name__ == '__main__':
    run_bot()
