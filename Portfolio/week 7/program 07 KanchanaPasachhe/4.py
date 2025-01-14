def analyze_frequency(text):
    char_counts={}

    for ch in text.lower():
        if ch.isalpha():
            if ch in char_counts:
                char_counts[ch] += 1
            else:
                char_counts[ch] = 1
    
    sorted_chars=sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    top_six=sorted_chars[:6]

    print("Top six most frequent letters:")
    for char, freq in top_six:
        print(f"{char}:{freq}")

text_input="She sells seashells by the seashore"
analyze_frequency(text_input)