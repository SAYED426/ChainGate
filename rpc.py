import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_rpc_url():
    url = os.getenv("RPC_URL")
    if not url:
        raise RuntimeError("RPC_URL environment variable is not set.")
    return url

def rpc_call(method, params):
    # Build the payload here
    payload ={
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params,
    }

    # Make the RPC call
    response = requests.post(
        get_rpc_url(),
        json=payload,
        timeout=10  
    )

    # Raise an error for bad responses
    response.raise_for_status()  

    # Parse the JSON response
    data = response.json()
    if "error" in data:
        raise RuntimeError(data["error"]["message"])
    if "result" not in data:
        raise RuntimeError(f"No result in RPC response: {data}")
    return data["result"]

def get_block_number():
    hex_block_number = rpc_call("eth_blockNumber", [])
    block_number = int(hex_block_number, 16)
    return block_number

if __name__ == "__main__":
    print("Current Ethereum Block Number:", get_block_number())
    hexa_chain_id = rpc_call("eth_chainId", [])
    chain_id = int(hexa_chain_id, 16)
    print("Current Ethereum Chain ID:", chain_id)