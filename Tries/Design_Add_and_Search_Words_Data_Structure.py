# Design Add and Search Words Data Structure

'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
'''

class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes mapped by characters
        self.children = {}  
        # Flag indicating whether the node represents the end of a word
        self.isWord = False 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            # Create a new node if the child does not exist
            if w not in curr.children:
                curr.children[w] = TrieNode()  
            curr = curr.children[w]
        # Mark the last node as representing the end of the inserted word
        curr.isWord = True


    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                w = word[i]
                # Handle wildcard character "."
                if w == ".":  
                    # Recursively search all child nodes for wildcard query
                    for child in curr.children.values():  
                        if dfs(i + 1, child):  
                            return True
                    return False
                else:
                    if w not in curr.children:
                        return False
                    curr = curr.children[w]
            # Return True if the last node represents the end of a word
            return curr.isWord  

        # Start DFS search from the root
        return dfs(0, self.root)  
