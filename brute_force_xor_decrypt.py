import sys
from BitVector import *
from xor_cipher import *
import glob
from timeit import default_timer as timer

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

def brute_force_xor_bin(bin_encrypted, bits, expected):
    #with open(input_file, "r") as fptr:
        #bin_encrypted = fptr.read()
    #expected = get_message()

    bin_str = gen_binary_strings(bits)
    #bin_encrypted = BitVector(bitstring=bin_encrypted)

    for i in bin_str:
        temp_key = BitVector(bitstring=i)
        decrypted = xor_encrypt(temp_key, bin_encrypted)
        if decrypted == expected:
            #print("DECRYPTED! \nKey is: " + str(temp_key))
            #print(decrypted.get_text_from_bitvector())
            return temp_key
    print("can't find key?")

def brute_force_xor_test():
    ################################################################
    # Get all the encrypted outputs
    ################################################################
    all_results = []
    for file in glob.glob("results/*.txt"):
        print(file)
        all_results.append(file)
    all_results.sort(key=natural_keys)

    expected = get_message()

    j = 1
    print("Number of bits   Max combinations checked   Total Time(sec)     Value of Key")
    print("--------------   ------------------------   ---------------     ------------")
    for i in all_results:
        encrypted_bin = get_message_binary(i)
        start = timer()
        found_key = brute_force_xor_bin(encrypted_bin, j, expected)
        end = timer()
        print("{:<16d} {:<23d} {:>14.9f}         {:>s}".format(j, 2**j, end-start , str(found_key)))
        j += 1


    ################################################################
    # Get the message
    ################################################################
    message = get_message()


if __name__ == "__main__":
    brute_force_xor_test()
    #brute_force_xor_text(sys.argv[1], int(sys.argv[2]))
    #gen_binary_strings(3)

