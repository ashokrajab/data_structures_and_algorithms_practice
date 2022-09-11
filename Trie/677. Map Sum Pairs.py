"""
Design a map that allows you to do the following:

    Maps a string key to a given value.
    Returns the sum of the values that have a key with a prefix equal to a given string.

Implement the MapSum class:

    MapSum() Initializes the MapSum object.
    void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
    int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

 

Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

 

Constraints:

    1 <= key.length, prefix.length <= 50
    key and prefix consist of only lowercase English letters.
    1 <= val <= 1000
    At most 50 calls will be made to insert and sum.
"""
class PrefixTree:
    
    def __init__(self):
        self.char = None
        self.children = {}
        self.endOfWord = False
        self.endOfWordValue = None
        self.value = None
        
class MapSum:
    
    def __init__(self):
        self.root = PrefixTree()

    def insert(self, key: str, val: int) -> None:
        
        key_len = len(key)
            
        def traverse(node, index):
            if index == key_len:
                is_word_already_exist = node.endOfWord
                node.endOfWord = True
                
                if not is_word_already_exist:
                    node.endOfWordValue = val
                    return False, None #canOverWriteValue
                else:
                    new_value = val - node.endOfWordValue 
                    node.endOfWordValue += new_value
                    return True, new_value #canOverWriteValue
            
            char = key[index]
            if char in node.children:
                canOverWriteValue, new_value = traverse(node.children[char], index+1)
                if canOverWriteValue:
                    node.children[char].value += new_value
                else:
                    node.children[char].value += val
            else:
                char_node = PrefixTree()
                char_node.char = char
                char_node.value = val
                node.children[char] = char_node
                canOverWriteValue, new_value = traverse(char_node, index+1)
            return canOverWriteValue, new_value
        
        traverse(self.root, 0)
            
    def sum(self, prefix: str) -> int:
        key_len = len(prefix)
        def traverse(node, index):
            if not node:
                return 0
            if index == key_len:
                return node.value
            
            char = prefix[index]
            return traverse(node.children.get(char), index+1)
        
        return traverse(self.root, 0)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)