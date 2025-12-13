def chatbot_response(user):
    responses = {
        "hello": "Hi! How can I help you?",
        "how are you": "I'm doing great, thanks for asking!",
        "what is python": "Python is a popular programming language.",
        "bye": "Goodbye! Have a great day."
    }

    return responses.get(user, "Sorry, I don't understand that.")


print("🤖 Chatbot Started (type 'bye' to exit)\n")

while True:
    user_input = input("You: ").lower()

    reply = chatbot_response(user_input)
    print("Bot:", reply)

    if user_input == "bye":
        break
