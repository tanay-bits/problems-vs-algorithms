Each `TrieNode` has a dictionary of its children nodes and whether that node represents the end of a word. The `Trie` class holds a collection of such `TrieNode`s. For dictionaries, checking whether a key exists, getting the value for a key, and setting a new
key-value pair are all `O(1)` in the average case and `O(n)` in the worst case (if the hash function is really bad and all entries
collide into the same bucket), where `n` represents the number of entries in the dictionary.

The `insert` and `find` methods of the `Trie` class perform these operations while traversing over each character of the input word
or prefix, hence their average case time complexity is `O(n)`.

The `insert` method of the `TrieNode` class simply creates a new entry in the `children` dictionary of that node, so it is of `O(1)`
average time complexity. The `suffixes` method recursively goes over all the children nodes and collects suffixes of valid words,
hence it is of `O(n)` average time complexity.

