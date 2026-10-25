from address import is_address
from rpc import rpc_call
from pathlib import Path

def get_code(address):
    if not is_address(address):
        raise ValueError(f"Invalid Ethereum address: {address}")
    code = rpc_call("eth_getCode", [address, "latest"])
    return code

def classify(code):
    # EOA
    if code == "0x":
        return "eoa"
    # Delegated EOA  
    elif code.startswith("0xef0100") and len(code) == 48:
        return "delegated_eoa"
    else:
        return "contract" 


def byte_length(code):
    # Remove the "0x" prefix
    code_stripped = code[2:]
    # Calculate the byte length
    bytes_length = len(code_stripped) // 2
    return bytes_length

def save_code(address, code):
    # Create a directory for the address if it doesn't exist
    dir_path = Path("cache") 
    dir_path.mkdir( exist_ok=True)
    # Save the code to a file at the directory path
    file_path = dir_path / f"{address.lower()}.hex"
    file_path.write_text(code, encoding="utf-8")
    return file_path

def get_code_cached(address):
    file_path = Path("cache") / f"{address.lower()}.hex"
    if file_path.exists():
        print("CACHE HIT")
        cached_byte = file_path.read_text(encoding="utf-8")
        return cached_byte
    print("CACHE MISS")
    code = get_code(address)
    save_code(address,code)
    return code
    


if __name__ == "__main__":
    addresses =[
        ("WETH","0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"),
        ("dEaD","0x000000000000000000000000000000000000dEaD"),
        ("vitalik","0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"),
    ]

    for name, address in addresses:
        code = get_code_cached(address)
        print(f"contract name:{name}")
        address_type = classify(code)
        print(f"address type:{address_type}")
        bytes_len = byte_length(code)
        print(f"bytes length:{bytes_len}")
