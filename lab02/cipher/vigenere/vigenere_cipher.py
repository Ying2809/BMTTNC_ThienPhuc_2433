class VigenereCipher:
    def__init__(self):
        pass
    def vigenere_encrypt(self, plain_text, key):
        encrypt_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypt_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord ('A')