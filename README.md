# Blockchain-based Note-Taking App

This project is a decentralized note-taking application that uses blockchain technology to provide secure, transparent, and immutable storage of personal notes. Built on Ethereum and simulated locally using Ganache, the app enables users to create and store notes in a decentralized way, ensuring data integrity and preventing unauthorized modifications.

## Project Overview

This application demonstrates how blockchain technology can be applied to personal data management. Each note is treated as a blockchain transaction, stored on the Ethereum blockchain, and managed through a web-based interface. Using Ganache as a local Ethereum blockchain simulator, the app allows users to experience blockchain interactions like transaction fees, wallet balance adjustments, and secure note storage.

## Features
- **Decentralized Storage**: Notes are stored as blockchain transactions, making them immutable and tamper-proof.
- **Transparency and Security**: Blockchain’s decentralized nature removes the need for a central authority and protects against unauthorized data modifications.
- **Wallet Interaction**: Simulated transaction fees via Ganache showcase real blockchain network behaviors like gas consumption.
- **Web-Based Interface**: Users can input and view notes through an intuitive frontend built with HTML, CSS, and Flask.

## System Design

### 1. Frontend: User Interface
The frontend is a simple web interface that enables users to input notes. 
- **HTML and CSS**: Structure and style the note input area and note display list.
- **JavaScript**: Optionally used for form validation and real-time updates without page reloads.

### 2. Backend: Flask Web Framework
Flask serves as the intermediary between the frontend and blockchain.
- **API Endpoints**:
  - `/submit_note`: Sends the note to the blockchain as a new transaction.
  - `/get_notes`: Retrieves all stored notes from the blockchain for display.
- **Web3.py**: Allows interaction with the Ethereum blockchain, simulating transactions and wallet management with Ganache.

### 3. Smart Contract: Solidity
The smart contract handles the storage and retrieval of notes.
- **Functions**:
  - `addNote(string memory note)`: Adds a new note to the blockchain.
  - `getNotes()`: Returns the list of all stored notes.

### 4. Blockchain Environment: Ganache
Ganache provides a local Ethereum network for testing.
- **Local Blockchain Simulation**: Allows for testing of blockchain transactions and smart contract deployment.
- **Wallet and Transaction Management**: Each note submission reduces the user's wallet balance, simulating gas fees.

## How It Works

1. **User Interaction**: The user submits a note via the web interface.
2. **Backend Processing**: The frontend sends the note to the Flask server, which uses Web3.py to interact with the smart contract.
3. **Blockchain Storage**: The note is recorded on the blockchain as a transaction.
4. **Display**: The updated note list is fetched from the blockchain and displayed on the frontend.

## How to Use

### Prerequisites
- **Python 3.x**
- Required libraries: `Flask`, `web3`, and `Ganache` (for local blockchain simulation)

Install dependencies:
```bash
pip install flask web3
```

Run command:
```bash
python app.py
```
