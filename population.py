from xor_cipher import *
from chromosome import *
from common import *
import random

class population:
    def __init__(self, bit_size, bin_encrypted):
        self.bit_size = bit_size
        self.bin_encrypted = bin_encrypted
        self.individuals = []
        self.next_individuals = []
        self.elites = []
        self.children = []

    def get_size(self):
        return self.bit_size

    def get_bin_encrypted(self):
        return self.bin_encrypted

    def initialize(self):
        for i in range(NUM_PER_GENERATION):
            temp_str = self.get_random_bitstring(self.bit_size)
            temp_chromosome = chromosome(temp_str, self.bin_encrypted)
            self.individuals.append(temp_chromosome)

    def get_random_bitstring(self, bit_size):
        return_str = ""
        for i in range(bit_size):
            return_str = return_str + (str(random.randint(0, 1)))
        return_bv = BitVector(bitstring=return_str)
        #print(return_str)

        return return_bv

