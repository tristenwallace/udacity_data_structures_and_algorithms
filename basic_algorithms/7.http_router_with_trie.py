class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, part):
        if part not in self.children:
            self.children[part] = RouteTrieNode()
            
class RouteTrie:
    def __init__(self, root_handler=None):
        self.root = RouteTrieNode(root_handler)

    def insert(self, parts, handler):
        node = self.root
        for part in parts:
            node.insert(part)
            node = node.children[part]
        node.handler = handler

    def find(self, parts):
        node = self.root
        for part in parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler
    
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        parts = self.split_path(path)
        self.route_trie.insert(parts, handler)

    def lookup(self, path):
        parts = self.split_path(path)
        handler = self.route_trie.find(parts)
        return handler if handler else self.not_found_handler

    def split_path(self, path):
        parts = path.strip("/").split("/")
        return [part for part in parts if part]  # Filter out empty parts
    
# Create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# Lookups with expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler'