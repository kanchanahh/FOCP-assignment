import random
import json
import time

# Load responses from a JSON file
def load_responses():
    with open("responses.json", "r") as file:
        return json.load(file)

responses = load_responses()

# Generate a random agent name
agent_names = ["Alexa", "Siri", "Rosie", "Julie", "Casie","Nikki","Krish"]
agent_name = random.choice(agent_names)

# Function to log chat history
def log_chat(user_name, chat_log):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"chat_log_{user_name}_{timestamp}.txt"
    with open(filename, "w") as log_file:
        for entry in chat_log:
            log_file.write(entry + "\n")

# Main chatbot function
def chatbot():
    print("Welcome to the University of Poppleton Chatbot!")
    user_name = input("Please enter your name: ").strip()
    print(f"Hello {user_name}! My name is {agent_name}, your agent for today. How can I help you?")

    chat_log = []
    chat_log.append(f"User: {user_name} has started the chat with {agent_name}.")

    while True:
        user_input = input(f"{user_name}: ").strip().lower()
        chat_log.append(f"{user_name}: {user_input}")

        if user_input in ["bye", "quit", "exit"]:
            print(f"{agent_name}: Goodbye {user_name}! Have a great day!")
            chat_log.append(f"{agent_name}: Goodbye {user_name}! Have a great day!")
            break

        response = None
        for keyword in responses:
            if keyword in user_input:
                response = responses[keyword]
                break

        if response:
            print(f"{agent_name}: {response}")
            chat_log.append(f"{agent_name}: {response}")
        else:
            random_response = random.choice(responses["default"])
            print(f"{agent_name}: {random_response}")
            chat_log.append(f"{agent_name}: {random_response}")

        # Randomly disconnect for realism (1 in 10 chance)
        if random.randint(1, 10) == 1:
            print(f"{agent_name}: Oops! I got disconnected. Please refresh the chat.")
            chat_log.append(f"{agent_name}: Disconnected unexpectedly.")
            break

    log_chat(user_name, chat_log)

if __name__ == "__main__":
    chatbot()
