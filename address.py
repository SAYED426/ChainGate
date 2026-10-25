HEX_CHARS = "0123456789abcdefABCDEF"

def is_address(address):
    # 1. Check the input type
    if not isinstance(address,str):
        return False

    # 2. Check the length
    if len(address) != 42:
        return False

    # 3. Check the prefix
    if not address.startswith("0x"):
        return False
    
    # 4. Extract the hexadecimal part
    body = address[2:]

    # 5. Validate each character
    for char in body:
        if char not in HEX_CHARS:
            return False

    # 6. Return True if all checks pass
    return True


if __name__ == "__main__":
    cases = [
        ("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", True),
        ("0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", True),
        ("0x" + "0" * 40, True),
        ("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"[:-1], False),
        ("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48" + "0", False),
        ("A0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", False),
        ("0xZZb86991c6218b36c1d19D4a2e9Eb0cE3606eB48", False),
        (12345, False),
        ("", False),
        ("0X" + "a" * 40, False),
    ]

    for address, expected in cases:
        result = is_address(address)
        if result == expected:
            print("PASS")
        else:
            print(f"FAIL: input={address!r}, expected={expected}, got={result}")
