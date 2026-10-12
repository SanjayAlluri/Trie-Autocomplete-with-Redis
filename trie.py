
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search_prefix(self, prefix, limit=5):
        node = self.root
        prefix = prefix.lower()

        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        results = []

        def dfs(curr, word):
            if len(results) >= limit:
                return

            if curr.is_end:
                results.append(word)

            for char in sorted(curr.children):
                dfs(curr.children[char], word + char)

                if len(results) >= limit:
                    return

        dfs(node, prefix)
        return results
