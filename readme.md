# Vigenere Cipher

This Python program implements the Vigenere cipher, which is a polyalphabetic substitution cipher. It allows you to encrypt and decrypt text using a keyword.

## Description

A Vigenere cipher is very similar to a Caesar cipher; however, in a Vigenere cipher, every character in the plaintext could be shifted by a different amount. The amount of shift is determined by a keyword, where 'A' in the keyword corresponds to shift of 0 (no shift), 'B' corresponds to a shift of 1, ..., and 'Z' corresponds to a shift of 25.

The keyword is repeated or truncated as necessary to fit the length of the plaintext. As an example, encrypting `ATTACKATDAWN` with the key `LEMON` gives:

```
 Plaintext: ATTACKATDAWN
       Key: LEMONLEMONLE
Ciphertext: LXFOPVEFRNHR
```

Each letter in the ciphertext is the sum of the indexes for the letters in the plaintext and the key. Thus, the first character of ciphertext is L due to the following calculations:

A + L = 0 + 11 = 11 -> L (L is the 11th letter in the alphabet, using -0- based indexing)

Decryption follows the same process but with a negative shift.

## Usage

`python vigenere_cipher.py`

**_As of this version, the message to be encrypted/decrypted is hardcoded into the script. The next version will incorporate a command-line interface to accommodate provision of a message to encrypt._**

### Functions
- **generate_key(plaintext, key)**: Creates the Vigenere key by repeating the provided key to match the length of the plaintext. It also preserves the capitalization of the plaintext in the key.
- **cipher(text, cipher_key, encrypt=True)**: Encrypts or decrypts the given text using the provided cipher key.
- **decipher(ciphertext, cipher_key)**: Decrypts the ciphertext using the provided cipher key.
- **main(plaintext, key)**: The main function that orchestrates the encryption and decryption process.

### Example
    Plain text: Attack at Dawn!!

    Cipher text: LxfopvEfrnhr!!

    Decrypted text: Attack at Dawn!!