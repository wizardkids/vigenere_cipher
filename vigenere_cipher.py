"""
    Filename: vigenere_cipher.py
     Version: 2.0
      Author: Richard E. Rawson
        Date: 2023-04-30
 Description:

A Vigenere cipher is very similar to a Caesar cipher; however, in a Vigenere cipher, every character in the plaintext could be shifted by a different amount. The amount of shift is determined by a keyword, where 'A' in the keyword corresponds to shift of 0 (no shift), 'B' corresponds to a shift of 1, ..., and 'Z' corresponds to a shift of 25.

The keyword is repeated or truncated as necessary to fit the length of the plaintext. As an example, encrypting "ATTACKATDAWN" with the key "LEMON" gives:

Plaintext:		ATTACKATDAWN
Key:			LEMONLEMONLE
Ciphertext:	    LXFOPVEFRNHR

Looking more closely, each letter in the ciphertext is the sum of the letters in the plaintext and the key. Thus, the first character of ciphertext is L due to the following calculations:

A + L = 0 + 11 = 11 -> L (L is the 11th letter in the alphabet, using -0- based indexing)
"""

import json
from string import ascii_uppercase

import click
from icecream import ic

VERSION = "2.0"


@click.command(help="", epilog="")
@click.argument("plaintext", required=False, type=str)
@click.argument("key", type=str, required=False)
@click.version_option(version=VERSION)
def cli(plaintext: str, key: str) -> None:
    print()
    ic(plaintext)
    ic(key)
    print()

    # If there is only one string on the command line, it will be seen as [PLAINTEXT] rather then [KEY].
    if plaintext and key is None:
        print("[PLAINTEXT] and [KEY] must appear on the command line together.")
        exit()

    if plaintext:
        # The key is not only expanded, but modified to preserve case of the text when decrypted.
        cipher_key: list[str] = generate_key(plaintext, key)
        cipher(plaintext, cipher_key, key)
    else:
        decipher()


def generate_key(plaintext: str, key: str) -> list[str]:
    """
    Create a vigenere key that is the same length as the length of the plain text.

    Parameters
    ----------
    plaintext : str -- the text that will be encrypted/decrypted
    key : str -- the original vigenere key, as a string

    Returns
    -------
    list[str] -- the vigenere key
            -- The original key is expanded so that there is one letter for each letter in the plain text
            -- The expanded key also contains capitalization that matches that of the plaintext for correct decryption.

    """
    cipher_key: list[str] = []
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


def cipher(text: str, cipher_key: list[str], key: str, encrypt=True):
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

    encrypted_text = "".join(c)
    print(f'Encrypted text:\n{encrypted_text}', sep="")

    encrypted_dict = {'encrypted_text': encrypted_text, 'cipher_key': key}

    if encrypt:
        with open('encrypted.json', 'w', encoding="utf-8") as f:
            json.dump(encrypted_dict, f)
    else:
        with open('decrypted.json', 'w', encoding="utf-8") as f:
            json.dump(encrypted_text, f)


def decipher() -> None:
    """
    Given an encrypted text, generate the decrypted text using the encryption key.

    CODENOTE:
        -- The encrypted text is sent to the same function as the plain text. The fourth argument tells cipher() to decrypt rather than encrypt.
    """

    with open("encrypted.json", 'r', encoding='utf-8') as f:
        encrypted_dict = json.load(f)

    ciphertext: str = encrypted_dict['encrypted_text']
    key: str = encrypted_dict['cipher_key']
    cipher_key: list[str] = generate_key(ciphertext, key)

    cipher(ciphertext, cipher_key, key, False)


if __name__ == '__main__':

    plaintext = 'Attack at Dawn!!'
    key = 'LeMON'

    # plaintext = "In the café, the bánh mì sandwich is a popular choice among the regulars. The flaky baguette, stuffed with savory grilled pork, pickled daikon and carrots, fresh cilantro, and a dollop of sriracha mayo, is the perfect lunchtime indulgence. As I sipped my matcha latte, I noticed the barista's shirt had a cute ねこ (neko, or cat) graphic on it. It reminded me of the time I visited Tokyo and saw the famous 東京タワー (Tokyo Tower) at night, aglow with colorful lights. The world is full of unique and beautiful symbols, and Unicode makes it possible to express them all in one cohesive language."

    # main(plaintext, key)
    print()
    cli()
