from difflib import get_close_matches

def get_best_match(user_question: str, questions: dict) -> str | None:
    """
    Get the best matching question from the dictionary based on the user's question.
    
    :param user_question: The question asked by the user.
    :param questions: A dictionary of predefined questions.
    :return: The best matching question or None if no close match is found.
    """

    list_questions: list[str] = [q for q in questions.keys()]
    matches: list = get_close_matches(user_question, list_questions, n = 1, cutoff=0.6)
    
    if matches:
        return matches[0]
    
def chatbot(knowledge: dict):
    while True:
        user_question = input('You:')
        
        if user_question.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            print('Bot: Goodbye! Have a great day!')
            break
        best_match: str | None = get_best_match(user_question= user_question, questions=knowledge)
        
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print(f'Bot: I don\'t understand your question. Please try again.')

def main():
    knowledge: dict = {
        "What is your name?": "I am a chatbot created to assist you.",
        "How can I reset my password?": "You can reset your password by going to the settings page and clicking on 'Reset Password'.",
        "What is the weather like today?": "I don't have real-time weather data, but you can check a weather website or app for the latest updates.",
        "How do I contact support?": "You can contact support by emailing support@example.com.",
        "How are you?": "I'm just a program, but I'm here to help you!",
        "What is the meaning of life?": "The meaning of life is a philosophical question that has been debated for centuries. Many believe it is to seek happiness, knowledge, and connection with others.",
        "What is Python?": "Python is a high-level, interpreted programming language known for its readability and versatility. It is widely used in web development, data analysis, artificial intelligence, and more.",
    }
    
    chatbot(knowledge)
    
if __name__ == "__main__":
    main()
        
        