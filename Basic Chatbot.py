import re

def message_probability(user_message, keywords, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in keywords:
            message_certainty += 1

    percentage = message_certainty / len(keywords) if len(keywords) > 0 else 0

    for word in required_words:
        if word not in user_message:
            has_required_words = False

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_messages(user_message):
    responses = {}

    # Each response with its keywords and required words
    responses["Hello!"] = message_probability(user_message, ["hello", "hi", "hey"], single_response=True)
    responses["I'm doing fine, and you?"] = message_probability(user_message, ["how", "are", "you", "doing"], required_words=["how"])
    responses["Thank you!"] = message_probability(user_message, ["i", "love", "code", "palace"], required_words=["code", "palace"])
    responses["I am eating now."] = message_probability(user_message, ["what", "you", "eat"], required_words=["you", "eat"])

    best_response = ""
    highest_score = 0

    for response in responses:
        if responses[response] > highest_score:
            highest_score = responses[response]
            best_response = response

    return best_response

def get_response(user_input):
    user_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    return check_messages(user_message)

# Chatbot loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break
    print("Bot:", get_response(user_input))
