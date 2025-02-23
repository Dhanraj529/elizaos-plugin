# ElizaOS Plugin - AI Agent Creation

## Overview
This repository contains a FastAPI-based backend for the ElizaOS plugin that allows users to create AI agents by selecting eligible NFTs.

## How It Works
1. **User Requests an AI Agent**
   - The backend checks if the user owns eligible NFTs.
   - If no NFTs are found, a link to obtain them is provided.

2. **User Selects an NFT**
   - The user picks an NFT from the returned list.
   - The user provides a name for the AI agent.

3. **Plugin Returns the Agent Details**
   - The system responds with a JSON object containing the chain, contract, tokenId, and agent name.

## Installation & Running the Backend

### Prerequisites
- Python 3.8+
- FastAPI
- Uvicorn

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Dhanraj529/elizaos-plugin.git
   cd elizaos-plugin
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server:**
   ```sh
   uvicorn main:app --reload
   ```

4. **Access API documentation at:**
   ```
   http://127.0.0.1:8000/docs
   ```

## API Endpoints

### 1. Request Eligible NFTs
- **Endpoint:** `POST /request-agent`
- **Payload:**
  ```json
  { "user_id": "user123" }
  ```
- **Response:**
  ```json
  {
    "nfts": [
      { "chain": "Ethereum", "contract": "0x1234abcd...", "tokenId": "5678", "name": "CyberBot" }
    ]
  }
  ```

### 2. Select an NFT & Name AI Agent
- **Endpoint:** `POST /select-nft`
- **Payload:**
  ```json
  {
    "tokenId": "5678",
    "agent_name": "Guardian AI"
  }
  ```
- **Response:**
  ```json
  {
    "chain": "Ethereum",
    "contract": "0x1234abcd...",
    "tokenId": "5678",
    "name": "Guardian AI"
  }
  ```

## Contact for Support
For any issues or clarifications, please reach out via GitHub Issues.

