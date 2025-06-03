from .trieNode import *

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, title, movie_id):
        node = self.root
        for char in title.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.movie_ids.append(movie_id)

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_movies_with_prefix(node)

    def _find_movies_with_prefix(self, node):
        result = []
        result.extend(node.movie_ids)
        for child in node.children.values():
            result.extend(self._find_movies_with_prefix(child))
        return result