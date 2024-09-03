# your code goes here!
from collections import Counter

class Anagram:
    def __init__(self, word):
        self.word = word.lower().replace(" ", "")
        self.word_counter = Counter(self.word)
    
    def match(self, possible_anagrams):
        matches = []
        for candidate in possible_anagrams:
            cleaned_candidate = candidate.lower().replace(" ", "")
            if Counter(cleaned_candidate) == self.word_counter:
                matches.append(candidate)
        return matches

# Example usage
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))  # Output: ['inlets']
