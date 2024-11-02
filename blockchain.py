import hashlib
import time
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = int(time.time())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = str(self.index) + str(self.timestamp) + self.data + self.previous_hash
        #print(block_content)
        return hashlib.sha256(block_content.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), new_data, previous_block.hash)
        self.chain.append(new_block)

    def get_all_blocks(self):
        for block in self.chain:
            # Only format timestamp if it's a float or int (UNIX timestamp)
            if isinstance(block.timestamp, (int, float)):
                # Format timestamp to a string
                block.timestamp = datetime.fromtimestamp(block.timestamp).strftime('%Y-%m-%d %H:%M:%S')
            # If it's already a string, you can choose to skip or handle it differently
            elif isinstance(block.timestamp, str):
                # You could choose to skip formatting if it's already a string
                pass  # or you can log or raise a warning if needed
        return self.chain