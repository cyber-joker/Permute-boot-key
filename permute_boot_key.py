def permute_boot_key(boot_key):
    """Permutes the boot_key array according to a fixed transformation table."""
    BOOT_KEY_SIZE = 16
    transforms = [8, 5, 4, 2, 11, 9, 13, 3, 0, 6, 1, 12, 14, 10, 15, 7]
    
    # Create a temporary copy of boot_key
    temp = boot_key[:]
    
    # Apply the permutation
    for i in range(BOOT_KEY_SIZE):
        boot_key[i] = temp[transforms[i]]

def print_byte_array(byte_array):
    """Prints the byte array in hexadecimal format without spaces and in lowercase."""
    print("".join(f"{b:02x}" for b in byte_array))

def main():
    # Example: Replace this with your own byte array input
    input_bytes = input("Enter 16 bytes of hex data (e.g., 0102030405060708090a0b0c0d0e0f10): ")
    
    # Convert input hex string to byte array
    if len(input_bytes) != 32:
        print("Error: Input must be exactly 32 hex characters long.")
        return
    
    try:
        boot_key = bytearray.fromhex(input_bytes)
    except ValueError as e:
        print(f"Error parsing hex string: {e}")
        return
    
    if len(boot_key) != 16:
        print("Error: Byte array must be 16 bytes long.")
        return
    
    # Perform permutation
    permute_boot_key(boot_key)
    
    # Output the result without spaces and in lowercase
    print("Permuted boot key is:", end=" ")
    print_byte_array(boot_key)

if __name__ == "__main__":
    main()
