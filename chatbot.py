# chatbot.py

def chatbot():
    print("🤖 Hi! I'm CodSoftBot. How can I help you today?")
    
    while True:
        msg = input("You: ").lower()

        if "hello" in msg or "hi" in msg:
            print("🤖 Hello! Nice to meet you.")
        elif "your name" in msg:
            print("🤖 I'm CodSoftBot, your friendly assistant!")
        elif "how are you" in msg:
            print("🤖 I'm just code, but I feel great!")
        elif "bye" in msg or "exit" in msg:
            print("🤖 Bye! Take care!")
            break
        else:
            print("🤖 Sorry, I didn't get that.")

chatbot()
