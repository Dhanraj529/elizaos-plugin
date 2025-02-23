# ElizaOS Plugin - FastAPI Backend

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Mock NFT Data
MOCK_NFTS = [
    {"chain": "Ethereum", "contract": "0x1234abcd...", "tokenId": "5678", "name": "CyberBot"},
    {"chain": "Solana", "contract": "5xyz56gh...", "tokenId": "9012", "name": "AI Guardian"},
]

class AgentRequest(BaseModel):
    user_id: str  

class NFTSelection(BaseModel):
    tokenId: str
    agent_name: str

class AgentResponse(BaseModel):
    chain: str
    contract: str
    tokenId: str
    name: str

@app.post("/request-agent")
async def request_agent(data: AgentRequest):
    """Handle user request for AI agent creation."""
    user_nfts = MOCK_NFTS if data.user_id else []
    if not user_nfts:
        return {"message": "No eligible NFTs found.", "request_link": "https://get-nfts.example.com"}
    return {"nfts": user_nfts}

@app.post("/select-nft")
async def select_nft(selection: NFTSelection):
    """User selects an NFT and provides a name for the AI agent."""
    nft = next((nft for nft in MOCK_NFTS if nft["tokenId"] == selection.tokenId), None)
    if not nft:
        raise HTTPException(status_code=404, detail="NFT not found")
    return AgentResponse(chain=nft["chain"], contract=nft["contract"], tokenId=nft["tokenId"], name=selection.agent_name)

# To run the server:
# uvicorn main:app --reload
