from contract import get_code_cached

def to_bytes(code):
    slashed_0x = code[2:]
    raw_bytes = bytes.fromhex(slashed_0x)
    return raw_bytes

def metadata_length(raw):
    bytes_metadata_length = raw[-2:]
    metadata_len = int.from_bytes(bytes_metadata_length,"big")
    return metadata_len

def metadata(raw):
    len_ = metadata_length(raw)
    if len_ + 2 > len(raw):
        return None
    dataWithout_len = raw[:-2]
    if len_ == 0:
        return b""
    raw_metadata = dataWithout_len[-len_:]
    return raw_metadata

def parse_metadata(code):
    r = to_bytes(code)
    m = metadata(r)
    result = {}
    if m is None:
        return None
    index = m.find(b"solc")
    if index != -1 :
        version_bytes = m[index + 5:index + 8]
        version_string = f"{version_bytes[0]}.{version_bytes[1]}.{version_bytes[2]}"
        result["solc"] = version_string
    index = m.find(b"bzzr0")
    if index != -1:
        result["bzzr0"] = True
    index = m.find(b"ipfs")
    if index != -1:
        ipfs_bytes = m[index + 4 : index + 6]

        if len(ipfs_bytes) == 2 and ipfs_bytes[0] == 0x58:
            hash_len = ipfs_bytes[1]
            start = index + 6
            end = start + hash_len

            if end<= len(m):
                ipfs_hash = m[start : end ]
                result["ipfs"] = ipfs_hash.hex()
    return result

if __name__ == "__main__":
    
    addresses = [
        ("uniVfactory","0x1F98431c8aD98523631AE4a59f267346ea31F984"),
        ("usdc","0x43506849D7C04F9138D1A2050bbF3A0c054402dd"),
        ("Weth","0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"),
        ("proxy","0x00000000e91fc5BAd977C0cc4Ad60557c06886a2"),
    ]

    for name, addr in addresses:
        code = get_code_cached(addr)
        ver = parse_metadata(code)
        print(f"""name:{name}
        address: {addr}
        verson: {ver}""")