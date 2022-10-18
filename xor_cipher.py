import sys

from BitVector import *
import re

#################################################
# Function Name: get_encryption_key
# Arguments:
#   1. None
# Return:
#   key (type: BitVector)
# Description:
#       Reads file "key.txt" and extracts key and
#       converts it into a text file
##################################################
def get_encryption_key():

    with open("key.txt", "r") as fptr:
        key_str = fptr.read()

    #print("Key: " + key_str)
    key = BitVector(bitstring=key_str)
    #key = BitVector(bitstring = key_str)
    #print(key.get_text_from_bitvector())
    print("Size of Key: " + str(len(key)) + "bit(s)")
    return key

#################################################
# Function Name: get_message
# Arguments:
#   1. None
# Return:
#   message (type: BitVector)
# Description:
#       Reads file "input.txt" and extracts message
#       and converts it into a text file
##################################################
def get_message():
    with open("input.txt", "r") as fptr:
        mes_str = fptr.read()

    mes_str = mes_str.lower()
    #mes_str = re.sub( "[^a-z ]", "", mes_str)
    #mes_str = re.sub("\\s", "", mes_str)
    #mes_str = re.sub("\\n", "", mes_str)
    #print(mes_str)
    message = BitVector(textstring=mes_str)

    return message

#################################################
# Function Name: xor_encrypt
# Arguments:
#   1. key (bitvector)
#   2. message (bitvector)
# Return:
#   encrypt_mes (type: BitVector)
# Description:
#       xor encrypts a message with the key
##################################################
def xor_encrypt(key, message):

    key_length = len(key)
    mes_length = len(message)
    key_pos = 0
    out_encrypted = BitVector(size=mes_length)

    for i in range(mes_length):
        out_encrypted[i] = message[i] ^ key[key_pos]
        #print("Comparing " + str(i) + " and " + str(key_pos))
        key_pos += 1

        if key_pos >= key_length:
            key_pos = 0

    with open("output_binary.txt", "w") as fptr:
        fptr.write(str(out_encrypted))
    # with open("output_text.txt", "w") as fptr:
    #     fptr.write(out_encrypted.get_text_from_bitvector())
    # with open("output_hex.txt", "w") as fptr:
    #     fptr.write(out_encrypted.get_hex_string_from_bitvector())

    return out_encrypted

if __name__ == "__main__":

    key = get_encryption_key()
    message = get_message()
    out_encrypted = xor_encrypt(key, message)






