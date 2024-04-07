# 5.Blockchain

## Efficiency
The Blockchain implementation exhibits a linear time complexity, O(n), for most of its operations, where n is the number of blocks in the chain. This is evident in the is_chain_valid and print_chain methods, which iterate through each block from the tail to the genesis block to verify integrity or print the chain's contents. The add_block method operates in constant time, O(1), as it only involves assigning a new block to the tail of the blockchain, regardless of the chain's length. The space complexity of the blockchain is also O(n), as storage is required for each block added to the chain.


## Code Design
The Block class encapsulates the data and metadata for each block, including a cryptographic hash to ensure data integrity. The Blockchain class manages the chain, supporting operations to add blocks and verify the chain's integrity. Notably, the calc_hash method in the Block class uses a fixed string, which deviates from typical blockchain implementations where the hash would be computed from the block's actual content and metadata. This design choice simplifies the hashing process but limits the demonstration of a blockchain's security features.