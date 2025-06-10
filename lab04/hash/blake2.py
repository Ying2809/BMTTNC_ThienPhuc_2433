import hashlib
def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size= 64)
    blake2_hash.update(message)
    return blake2_hash.digest()
def main():
    text = input("Nhập chuỗi văn bản: ").encode('UTF-8')
    hashed_text = blake2(text)
    print("Chuỗi văn bản đã nhập:",text.decode('UTF-8'))
    print("BLAKE2 Hash:", hashed_text.hex())
if __name__ == "__main__":
    main()