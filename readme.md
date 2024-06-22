# Vigenere Cipher

This Python program implements the Vigenere cipher, which is a polyalphabetic substitution cipher. It allows you to encrypt and decrypt text using a keyword.

## Description

A Vigenere cipher is very similar to a Caesar cipher; however, in a Vigenere cipher, every character in the plaintext could be shifted by a different amount. The amount of shift is determined by the provided keyword.

In the normal Vigenere cipher, each letter in the ciphertext is the sum of the indexes for the letters in the plaintext and the key. Thus, the first character of ciphertext is L due to the following calculations:

A + L = 0 + 11 = 11 -> L (L is the 11th letter in the alphabet, using -0- based indexing)

In similar fashion, but to accommodate unicode text in this program, the shift in a given character in [PLAINTEXT] is determined by the code point of the corresponding character in the [KEY]. For example, if the [PLAINTEXT] is "Boats launch at midnight" and the [KEY] is "Lemon", then the code point for "L" (76) is added to the code point for "B" (66) to yield a cipher character of 142 (Ž). Decryption reverses this computation.

The keyword is repeated or truncated as necessary to fit the length of the plaintext. As an example, encrypting `ATTACKATDAWN` with the key `LEMON` gives:

```
 Plaintext: ATTACKATDAWN
       Key: LEMONLEMONLE
Ciphertext: LXFOPVEFRNHR
```

## Usage

**Encryption:** provide both a message and a key

`python vigenere_cipher.py "The boats launch at midnight." "LEMoN"`

**Decryption:**

`python vigenere_cipher.py`


## Functions
- **generate_key(plaintext, key)**: Creates the Vigenere key by repeating the provided key to match the length of the plaintext. It also preserves the capitalization of the plaintext in the key.
- **cipher(text, cipher_key, key, encrypt=True)**: Encrypts or decrypts the given text using the provided cipher key.
- **decipher()**: Decrypts the ciphertext in "encrypted.json" using the saved cipher key.

## Example
    Plain text: Attack at Dawn!!
           Key: LEMon

    Cipher text: ¹ÁÐÑ·e®ã¦ÄÝm

    Decrypted text: Attack at Dawn!!

## NOTES
- The program will save the cipher key to "encrypted.json" for decryption.
- Obviously, saving the encryption key along with the encrypted text is a ludicrous security risk. The program can be modified to prevent this, but the user will need to keep the key *somewhere*!