
from trie import Trie
from cache import get_suggestions, client

# Build the Trie
trie = Trie()

with open("words.txt", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        if word:
            trie.insert(word)

# Test autocomplete twice
client.ping()

print("\nFirst search:")
print(get_suggestions("app", trie))

print("\nSecond search:")
print(get_suggestions("app", trie))
