// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TimeStampedNotes {

    struct Note {
        string content;
        uint256 timestamp;
    }

    Note[] public notes;

    // Add a note to the blockchain
    function addNote(string memory _content) public {
        notes.push(Note({
            content: _content,
            timestamp: block.timestamp
        }));
    }

    // Get the count of notes
    function getNotesCount() public view returns (uint256) {
        return notes.length;
    }

    // Get a note by its index (with a static return for debugging)
    function getNoteByIndex(uint256 _index) public view returns (string memory, uint256) {
        require(_index < notes.length, "Note index out of bounds");
        // Temporary debug value
        return (notes[_index].content, notes[_index].timestamp);
    }
}
