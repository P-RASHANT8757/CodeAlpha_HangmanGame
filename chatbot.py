
print("================================")
print("       CODEALPHA CHATBOT")
print("================================")
print("Hello! I am your chatbot.")
print("You can ask me simple questions.")
print("Type 'bye' to exit.")

while True:
    user = input("\nYou: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Namaste")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: My name is Prashant Kumar.")

    elif user == "what is python":
        print("Bot: Python is a programming language.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
