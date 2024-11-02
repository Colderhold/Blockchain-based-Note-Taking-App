from flask import Flask, render_template
from web3 import Web3

app = Flask(__name__)

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Set default account for contract interactions
web3.eth.default_account = web3.eth.accounts[0]

# Contract ABI
contract_abi = [
    {
        "inputs": [{"internalType": "string", "name": "_content", "type": "string"}],
        "name": "addNote",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getNotesCount",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_index", "type": "uint256"}],
        "name": "getNoteByIndex",
        "outputs": [
            {"internalType": "string", "name": "content", "type": "string"},
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Contract address (replace with your deployed contract address)
contract_address = "0x83aFd021EAEc379199a259D35F1c179f6f19Abda"

# Contract instance
notes_contract = web3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/')
def index():
    try:
        notes_count = notes_contract.functions.getNotesCount().call()
        notes = []

        for i in range(notes_count):
            try:
                # Fetch the note content and timestamp
                note_content, timestamp = notes_contract.functions.getNoteByIndex(i).call()
                notes.append({'content': note_content, 'timestamp': timestamp})
            except Exception as e:
                print(f"Error retrieving note {i}: {e}")
                notes.append({'content': 'Error', 'timestamp': 'N/A'})
        
        return render_template('index.html', notes=notes)

    except Exception as e:
        return f"Error fetching notes count: {e}"

if __name__ == '__main__':
    app.run(debug=True)
