"""
    Filename: vigenere_cipher.py
     Version: 0.1
      Author: Richard E. Rawson
        Date: 2023-04-30
 Description:

A Vigenere cipher is very similar to a Caesar cipher; however, in a Vigenere cipher, every character in the plaintext could be shifted by a different amount. The amount of shift is determined by a keyword, where 'A' corresponds to shift of 0 (no shift), 'B' corresponds to a shift of 1, ..., and 'Z' corresponds to a shift of 25.

The keyword is repeated or truncated as necessary to fit the length of the plaintext. As an example, encrypting "ATTACKATDAWN" with the key "LEMON" gives:

Plaintext:		ATTACKATDAWN
Key:			LEMONLEMONLE
Ciphertext:	    LXFOPVEFRNHR
Looking more closely, each letter in the ciphertext is the sum of the letters in the plaintext and the key. Thus, the first character of ciphertext is L due to the following calculations:

A + L = 0 + 11 = 11 -> L
"""

from string import ascii_uppercase


def generate_key(plaintext, key):
    """
    Create ke vigenere key that is an appropriate length for the length of the plain text.

    Args:
        plaintext (str): the text that will be encrypted/decrypted
        key [list]: the original vigenere key, as a string

    Returns:
        [list]: the vigenere key
            -- The original key is expanded so that there is one letter for each letter in the plain text
            -- The expanded key also contains capitalization that matches that of the plaintext, so that decrypting can restore the capitalization as well as the characters.
    """
    cipher_key = []
    for i in range(len(plaintext)):
        e = i % len(key)
        cipher_key.append(key[e])

    # Modify key for upper/lower case of plaintext:
    for ndx, i in enumerate(plaintext):
        if ord(i) >= 97:
            cipher_key[ndx] = cipher_key[ndx].lower()
        else:
            cipher_key[ndx] = cipher_key[ndx].upper()

    return cipher_key


def cipher(text, cipher_key, encrypt=True):
    """
    Encrypt (if "encrypt" is True) or decrypt (if "encrypt" is False) the passed in text.

    Args:
        text (str): either the plain text or the encrypted text
        cipher_key [list]: the expanded key
        encrypt (bool, optional): True to encrypt; False to decrypt

    Returns:
        str: the encrypted or decrypted text
    """
    alp = list(ascii_uppercase)

    c = []
    for ndx, i in enumerate(text):
        o = ord(i)
        s = i.upper()
        if s not in ascii_uppercase:
            c.append(i)
            continue
        p_ndx = alp.index(s)
        k_ndx = alp.index(cipher_key[ndx].upper())
        if encrypt:
            alp_ndx = (p_ndx + k_ndx) % 26
        else:
            alp_ndx = (p_ndx - k_ndx) % 26

        if ord(i) >= 97 and ord(i) <= 122:
            c.append(alp[alp_ndx].lower())
        elif ord(i) >= 65 and ord(i) <= 90:
            c.append(alp[alp_ndx].upper())
        else:
            c.append(i)

    return "".join(c)


def decipher(ciphertext, cipher_key):
    """
    Given an encrypted text, create a decrypted text.

    Args:
        ciphertext (str): the encrypted text
        cipher_key [list]: the expanded key required for encryption/decryption

    Returns:
        str: the decrypted text

    CODENOTE:
        -- The encrypted text is sent to the same function as the plain text. The third argument tells cipher() to decrypt rather than encrypt.
    """
    decryptedtext = cipher(ciphertext, cipher_key, False)

    return "".join(decryptedtext)


def main(plaintext, key):
    """
    Main function that runs everything else.

    Args:
        plaintext (str): the plain text that will be encrypted/decrypted
        key (str):the vigenere key

    CODENOTE:
        -- The key will need to be expanded so that there is one letter in the modified key for every letter in plain text. That expanded key will then be used to encrypt/decrypt according to the method described in the initial docstring.
        -- Additionally, during processing, the expanded key will preserve the capitalization of the plain text.
    """

    # The key is not only expanded, but modified to preserve case of the text when decrypted.
    cipher_key = generate_key(plaintext, key)

    ciphertext = cipher(plaintext, cipher_key)

    decryptedtext = decipher(ciphertext, cipher_key)

    print()
    print(f'    Plain text: {plaintext}')
    print()
    print(f'   Cipher text: {ciphertext}')
    print()
    print(f'Decrypted text: {decryptedtext}')
    print()


if __name__ == '__main__':

    plaintext = 'Attack at Dawn!!'
    key = 'LeMON'

    plaintext = "In the café, the bánh mì sandwich is a popular choice among the regulars. The flaky baguette, stuffed with savory grilled pork, pickled daikon and carrots, fresh cilantro, and a dollop of sriracha mayo, is the perfect lunchtime indulgence. As I sipped my matcha latte, I noticed the barista's shirt had a cute ねこ (neko, or cat) graphic on it. It reminded me of the time I visited Tokyo and saw the famous 東京タワー (Tokyo Tower) at night, aglow with colorful lights. The world is full of unique and beautiful symbols, and Unicode makes it possible to express them all in one cohesive language."

    main(plaintext, key)
