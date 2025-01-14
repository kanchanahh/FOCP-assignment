def get_sorted_unique_letters(input_string):
    
    unique_letters = set(char for char in input_string if char.isalpha())
    return sorted(unique_letters)

if __name__ == "__main__":
    test_string1 = "cheese"
    test_string2 = "Hello, World!"
    test_string3 = "12345abc!@#"
    test_string4 = ""

    print(get_sorted_unique_letters(test_string1))  
    print(get_sorted_unique_letters(test_string2))  
    print(get_sorted_unique_letters(test_string3))  
    print(get_sorted_unique_letters(test_string4))