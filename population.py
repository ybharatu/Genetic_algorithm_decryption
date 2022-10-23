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
        self.num_generations = 0

    ################################################################
    # Get Methods
    ################################################################
    def get_size(self):
        return self.bit_size

    def get_bin_encrypted(self):
        return self.bin_encrypted

    ################################################################
    # Creates a random set of chromosomes for the initial population
    ################################################################
    def initialize(self):
        self.num_generations = 0
        for i in range(NUM_PER_GENERATION):
            temp_str = self.get_random_bitstring(self.bit_size)
            temp_chromosome = chromosome(temp_str, self.bin_encrypted)
            self.individuals.append(temp_chromosome)

    ################################################################
    # Generates a random bitstring, returns a BitVector
    ################################################################
    def get_random_bitstring(self, bit_size):
        return_str = ""
        for i in range(bit_size):
            return_str = return_str + (str(random.randint(0, 1)))
        return_bv = BitVector(bitstring=return_str)

        return return_bv

    ################################################################
    # Fills the remaining members of the next generation with
    # children of the most fit of the current generation. Currently
    # implemented as a one point crossover selection
    ################################################################
    def crossover_chrmosomes(self):
        ################################################################
        # Create offspring until max number of chromosomes per
        # generation has been reached
        ################################################################
        curr_parent = 0
        while len(self.next_individuals) != NUM_PER_GENERATION:
            if curr_parent + 1 < NUM_PER_GENERATION - 1:
                ################################################################
                # Select two parents based on the most fit individuals and cycle
                # through them. Ex: I0 and I1, I1 and I2,...
                ################################################################
                p1 = self.individuals[curr_parent].key
                p2 = self.individuals[curr_parent+1].key

                ################################################################
                # Split both parents chromosomes into two. Getting a random
                # position from 1 and size -1 to avoid having the same parent
                # being created
                ################################################################
                crossover_pos = random.randint(1, self.bit_size - 1)
                #crossover_pos = int(self.bit_size / 2)
                l1, r1 = p1[:crossover_pos], p1[crossover_pos:]
                l2, r2 = p2[:crossover_pos], p2[crossover_pos:]

                ################################################################
                # Combine them to make a child
                ################################################################
                # print("Using Parents: " + str(p1) + " and " + str(p2) + " Combining " + str(l1) + " and " + str(r2) +
                #       " to form " + str(l1)+str(r2))
                c1 = chromosome(BitVector(bitstring=l1+r2), self.bin_encrypted)
                self.children.append(c1)
                self.next_individuals.append(c1)
                if len(self.next_individuals) != NUM_PER_GENERATION:
                    # print("Using Parents: " + str(p1) + " and " + str(p2) + " Combining " + str(l2) + " and " + str(
                    #     r1) + " to form " + str(l2) + str(r1))
                    c2 = chromosome(BitVector(bitstring=l2+r1), self.bin_encrypted)
                    self.children.append(c2)
                    self.next_individuals.append(c2)
                curr_parent += 1
            else:
                print("Shouldn't reach here in crossover_chromosomes")
                print(len(self.next_individuals))

    ################################################################
    # Based on MUTATION_RATE, flips a bit of random chromosomes to
    # induce changes
    ################################################################
    def mutate_chromosomes(self):
        ################################################################
        # Iterate through all chromosomes
        ################################################################
        for chrom in self.next_individuals:
            ################################################################
            # Iterate through each bit of the chromosome
            ################################################################
            for i in range(self.bit_size):
                ################################################################
                # flip the bit if the mutation check is successful
                ################################################################
                if random.randint(0, 99) < MUTATION_RATE * 100:
                    # print("Mutating " + str(chrom.key) + ": Flipping the " + str(i) + " bit")
                    if chrom.key[i] == 0:
                        chrom.key[i] = 1
                    else:
                        chrom.key[i] = 0

    ################################################################
    # Moves all the chromosomes from next generation to current
    # generation. Also resets states and increments generation count
    ################################################################
    def repopulate(self):
        self.individuals = []
        for i in self.next_individuals[:]:
            self.individuals.append(i)
            self.next_individuals.remove(i)
        self.elites = []
        self.children = []
        self.num_generations += 1
