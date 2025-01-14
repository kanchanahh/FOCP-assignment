def letters_in_at_least_one(word1, word2):
    return sorted(set(word1) | set(word2))  

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))  

def letters_in_either_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))  

test_word1 = "cheese"
test_word2 = "bread"

print("Letters in at least one of the two words:")
print(letters_in_at_least_one(test_word1, test_word2))

print("Letters in both words:")
print(letters_in_both(test_word1, test_word2))

print("Letters in either word, but not both:")
print(letters_in_either_but_not_both(test_word1, test_word2))
