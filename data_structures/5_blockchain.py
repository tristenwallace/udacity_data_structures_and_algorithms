import hashlib
from datetime import datetime
import pytz

class Block:

    def __init__(self, data: str, previous_hash: str, previous_block: 'Block' = None) -> None:
        GMT = pytz.timezone("Etc/GMT")
        self.timestamp = datetime.now(GMT)
        self.data = data
        self.previous_block = previous_block
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self) -> str:
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()
    
    def __repr__(self):
        return (f"Block(Timestamp: {self.timestamp}, Data: '{self.data}', "
                f"Hash: {self.hash}, Previous Hash: {self.previous_hash})")

class Blockchain:
    
    def __init__(self) -> None:
        self.tail = None
        self.create_genesis_block()
    
    def create_genesis_block(self) -> None:
        genesis_block = Block("Genesis Block", None, None)
        self.tail = genesis_block
    
    def add_block(self, data: str) -> None:
        new_block = Block(data, self.tail.hash, self.tail)
        self.tail = new_block
    
    def is_chain_valid(self) -> bool:
        current_block = self.tail
        while current_block and current_block.previous_block:
            if current_block.previous_hash != current_block.previous_block.hash:
                return False
            current_block = current_block.previous_block
        return True
    
    def print_chain(self) -> None:
        if not self.is_chain_valid():
            print("Blockchain Invalid! Cannot print chain.")
            return
        
        current_block = self.tail
        while current_block:
            print(current_block)
            current_block = current_block.previous_block

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
print("\nTest Case 1: Empty Data")
blockchain = Blockchain()
blockchain.add_block("")  # Add a block with empty data
blockchain.print_chain()

## Test Case 2
print("\nTest Case 2: Very Large Data")
large_data = "x" * 10000  # Very large data
blockchain = Blockchain()
blockchain.add_block(large_data)
blockchain.print_chain()


## Test Case 3
print("\nTest Case 3: Regular Data")
blockchain = Blockchain()
blockchain.add_block("Block 1 Data")
blockchain.add_block("Block 2 Data")
blockchain.add_block("Block 3 Data")
blockchain.print_chain()