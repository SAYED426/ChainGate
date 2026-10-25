def is_address(Address):
    # 1. Check the input type
    if not isinstance(Address,str):
        return False

    # 2. Check the length
    if len(Address) != 42:
        return False

    # 3. Check the prefix
    if not Address.startswith("0x"):
        return False
    
    # 4. Extract the hexadecimal part
    body = Address[2:]

    hex_chars = "0123456789abcdefABCDEF"

    # 5. Validate each character
    for char in body:
        if char not in hex_chars:
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
        ("0Xa0b8...", False),
    ]

    for address, expected in cases:
        result = is_address(address)
        if result == expected:
            print("PASS")
        else:
            print(f"FAIL: input={address!r}, expected={expected}, got={result}")
