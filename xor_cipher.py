import sys

from BitVector import *
import re
import glob

# https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

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
def get_encryption_key(key_file_name="key.txt"):

    with open(key_file_name, "r") as fptr:
        key_str = fptr.read()

    #print("Key: " + key_str)
    key = BitVector(bitstring=key_str.strip())
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
def get_message(filename="input.txt"):
    with open(filename, "r") as fptr:
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
def xor_encrypt(key, message, out_file_name="output_binary.txt", wren = False):

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

    if wren:
        with open(out_file_name, "w") as fptr:
            fptr.write(str(out_encrypted))
    # with open("output_text.txt", "w") as fptr:
    #     fptr.write(out_encrypted.get_text_from_bitvector())
    # with open("output_hex.txt", "w") as fptr:
    #     fptr.write(out_encrypted.get_hex_string_from_bitvector())

    return out_encrypted

#################################################
# Function Name: gen_keys
# Arguments:
#   1. n_bits
# Return:
#   key_array
# Description:
#       Generates random keys for bits 1 to n
##################################################
def gen_keys(n_bits):
    key_array = []
    bv = BitVector(size=n_bits)
    # For some reason, gen_random_bits doesn't work with a size < 3?
    for i in range(3, n_bits, 1):
        bv = bv.gen_random_bits(i)
        print(str(bv))
        key_array.append(bv)
        with open("keys/key_" + str(i) +"_bits.txt", "w") as fptr:
            fptr.write(str(bv))

    with open("keys/all_keys.txt", "w") as fptr:
        for i in key_array:
            fptr.write(str(i) + "\n")


def encrypt_xor_test():
    ################################################################
    # Get the message
    ################################################################
    message = get_message()

    ################################################################
    # Get all the keys
    ################################################################
    all_keys = []
    for file in glob.glob("keys/key*.txt"):
        all_keys.append(file)
    all_keys.sort(key=natural_keys)
    j = 1
    for i in all_keys:
        key = get_encryption_key(i)
        print("Encrypting with " + str(key))
        out = xor_encrypt(key, message, "results/output_" + str(j) + "_bits.txt", True)
        j += 1


if __name__ == "__main__":

    gen_keys(15)
    encrypt_xor_test()
    # key = get_encryption_key()
    # message = get_message()
    # out_encrypted = xor_encrypt(key, message)







