# Chat-Application
TCP Chat Application 
Here's a README for your TCP Chat Application with encryption:

---

# Encrypted TCP Chat Application

A simple TCP-based chat application in Python with encrypted message transmission, built using sockets and the cryptography library. This app allows two users to chat over a TCP connection, with messages encrypted to ensure secure communication.

## Features

- **Encrypted Message Transmission:** Messages are encrypted using symmetric encryption for secure transmission.
- **TCP Connection:** Relies on TCP sockets for reliable data transfer.
- **User Interface (Optional):** Basic command-line interface; can be extended to a GUI.

## Prerequisites

- Python 3.6+
- Install `cryptography` library:
  ```bash
  pip install cryptography
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tcp-chat-app.git
   cd tcp-chat-app
   ```

2. Ensure `server.py` and `client.py` scripts are in the same directory.

## Usage

1. **Run the Server:**
   - In a terminal, navigate to the directory and start the server:
     ```bash
     python server.py
     ```
   - The server will listen for a connection on `localhost:10000`.

2. **Run the Client:**
   - In a separate terminal, run the client script:
     ```bash
     python client.py
     ```
   - Connects to the server, enabling encrypted chat communication.

3. **Chat!**
   - Type your message in the client terminal. Messages are encrypted and sent to the server.

## How It Works

- **TCP Socket:** `socket` is used to establish a connection between server and client.
- **Encryption:** Messages are encrypted using a symmetric key (AES encryption) for secure transmission.

## Project Structure

```plaintext
.
├── client.py         # Client-side script to connect and chat with the server
├── server.py         # Server-side script to accept connections and relay messages
└── README.md         # Project documentation
```

## Acknowledgments

This project uses Python's `socket` and `cryptography` libraries. Special thanks to community resources for networking and cryptography tutorials.
