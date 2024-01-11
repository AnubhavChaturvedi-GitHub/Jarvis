import random

class SimpleAI:
    def __init__(self, dialogues):
        self.dialogues = dialogues

    def get_response(self, user_input):
        for pattern, response_list in self.dialogues.items():
            if any(keyword in user_input.lower() for keyword in pattern):
                return random.choice(response_list)
        return "I'm sorry, I don't understand that."

# Example dialogues
dialogues = {
    ("hello", "hi", "hey"): ["Hello! How can I help you?", "Hi there!", "Hey!"],
    ("how are you", "how's it going"): ["I'm doing well, thank you!", "I'm fine, how about you?"],
    ("goodbye", "bye", "see you later"): ["Goodbye!", "See you later!", "Take care!"],
}

# Create an instance of the SimpleAI
ai = SimpleAI(dialogues)

# Simulation of a conversation
print("AI: Hello! I'm a simple AI. Type 'exit' to end the conversation.")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("AI: Goodbye!")
        break
    response = ai.get_response(user_input)
    print(f"AI: {response}")
