For dictionaries, checking whether a key exists, getting the value for a key, and setting a new
key-value pair are all `O(1)` in the average case and `O(n)` in the worst case (if the hash function is really bad and all entries
collide into the same bucket), where `n` represents the number of entries in the dictionary.

Each `RouteTrieNode` has a dictionary of its children nodes and a handler string. Its `insert` method simply adds a new entry to its
`children` dictionary, so it is of `O(1)` average time complexity.

The `RouteTrie` class holds the collection of Route Trie Nodes starting with a root node and a "not found" handler for invalid
paths. The `insert` and `find` methods of the `RouteTrie` class perform `O(1)` average time dictionary operations while traversing
over each word of the input path, hence their average case time complexity is `O(n)` where `n` is the number of "/" separated words
in the input path.

The `Router` class is a wrapper for `RouteTrie` which initializes the Route Trie with a root handler and a not-found handler. The
`add_handler` and `lookup` methods first split the input path into "/" separated parts and then call the `insert` or `find` methods
of `RouteTrie`. The `split_path` helper method actually performs the path splitting using the "/" separator, which is of `O(m)` time
where `m` is the number of characters in the input path string. Thus the `add_handler` and `lookup` methods are of `O(m + n)`
average time complexity, which can be simplified as `O(n)`.
