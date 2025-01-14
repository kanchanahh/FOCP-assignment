import random
import string

def encrypt_message(message):
    interval=random.randint(2,20)

    encrypted_message=[]

    for char in message:
        encrypted_message.append(char)

        for _ in range(interval - 1):
            random_letter=random.choice(string.ascii_lowercase)
            encrypted_message.append(random_letter)

    encrypted_message_str=''.join(encrypted_message)
    return encrypted_message_str,interval

if __name__=="__main__":
    message="send cheese"
    encrypted_message, interval=encrypt_message(message)
    print(f"Original message:{message}")
    print(f"Encrypted message:{encrypted_message}")
    print(f"Interval used:{interval}")