import sys
from BitVector import *
from xor_cipher import *

# https://stackoverflow.com/questions/64890117/what-is-the-best-way-to-generate-all-binary-strings-of-the-given-length-in-pytho
def gen_binary_strings(num_bits):
    bin_str = []
    recursive_gen_binary(num_bits, bin_str)
    # for i in bin_str:
    #     print(i)
    return bin_str

def recursive_gen_binary(num_bits, bin_str, base_str=""):
    if len(base_str) == num_bits:
        bin_str.append(base_str)
        return bin_str
    recursive_gen_binary(num_bits, bin_str, base_str + "0")
    recursive_gen_binary(num_bits, bin_str, base_str + "1")

def brute_force_xor_text(input_file, bits):
    with open(input_file, "r") as fptr:
        bin_encrypted = fptr.read()
    expected = get_message()

    bin_str = gen_binary_strings(bits)
    bin_encrypted = BitVector(bitstring=bin_encrypted)

    for i in bin_str:
        temp_key = BitVector(bitstring=i)
        decrypted = xor_encrypt(temp_key, bin_encrypted)
        if decrypted == expected:
            print("DECRYPTED! \nKey is: " + str(temp_key))
            print(decrypted.get_text_from_bitvector())
            break


if __name__ == "__main__":
    brute_force_xor_text(sys.argv[1], int(sys.argv[2]))
    #gen_binary_strings(3)

