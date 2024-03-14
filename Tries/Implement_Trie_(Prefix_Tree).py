# Implement Trie (Prefix Tree)

'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
'''

class TrieNode:
    def __init__(self):
        # Array to store links to child nodes
        self.children = [None] * 26
        # Flag to indicate if the node represents the end of a word
        self.isWord = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initialize the Trie with an empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        # Start traversal from the root node
        for c in word:
            # Calculate the index of the character in the children array
            i = ord(c) - ord("a")
            # Create a new node if the child does not exist
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            # Move to the child node
            curr = curr.children[i]
        # Mark the last node as the end of the inserted word
        curr.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        # Start traversal from the root node
        for c in word:
            # Calculate the index of the character in the children array
            i = ord(c) - ord("a")
            # Return False if any character is missing in the trie
            if curr.children[i] == None:
                return False
            # Move to the child node
            curr = curr.children[i]
        # Return True if the last node represents the end of a word
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        # Start traversal from the root node
        for c in prefix:
            # Calculate the index of the character in the children array
            i = ord(c) - ord("a")
            # Return False if any character is missing in the trie
            if curr.children[i] == None:
                return False
            # Move to the child node
            curr = curr.children[i]
        # Return True if the prefix exists in the trie
        return True
