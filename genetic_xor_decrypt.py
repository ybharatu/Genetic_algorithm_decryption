import sys
from BitVector import *
from xor_cipher import *
import glob
from timeit import default_timer as timer
from chromosome import *
from population import *

def genetic_xor_decrypt(bin_encrypted, bits, expected):

    ################################################################
    # Create population of chromosomes and Initialize it
    ################################################################
    pop = population(bits, bin_encrypted)
    pop.initialize()

    ################################################################
    # Sort population by fitness
    ################################################################
    #pop = sorted(pop)
    #for c in pop:
        #print(c.key)


if __name__ == "__main__":
    bin_encrypted = get_message_binary("results/output_3_bits.txt")

    expected = get_message()

    genetic_xor_decrypt(bin_encrypted, 3, expected)


