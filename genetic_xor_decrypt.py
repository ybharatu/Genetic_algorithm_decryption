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

    for i in range(MAX_GENERATIONS):
        ################################################################
        # Sort population by fitness
        ################################################################
        #print("SORTED:")
        pop.individuals = sorted(pop.individuals, reverse=True)
        # for c in pop.individuals:
        #     print(c.key)

        ################################################################
        # Print Individuals of Current Generation
        ################################################################
        print("GENERATION " + str(pop.num_generations))
        for j in pop.individuals:
            print(j.key)
        ################################################################
        # Finish early if key has been found
        ################################################################
        if pop.individuals[0].score == 1:
            print("Took " + str(pop.num_generations) + " Generations to decrypt")
            print("Key is : " + str(pop.individuals[0].key))
            return pop.individuals[0].decrypted

        ################################################################
        # Find elites to carry over to the next generation, so
        # generations will always get better
        ################################################################
        for j in range(NUM_ELITES):
            new_elite = chromosome(pop.individuals[j].key, pop.get_bin_encrypted())
            pop.elites.append(new_elite)
            pop.next_individuals.append(new_elite)
            print("Elites: " + str(pop.individuals[j].key))

        ################################################################
        # Crossover most fit chromosomes to produce offspring
        ################################################################
        pop.crossover_chrmosomes()
        #print("New Children: ")
        # for j in pop.next_individuals:
        #     print(j.key)

        ################################################################
        # Create Mutations
        ################################################################
        pop.mutate_chromosomes()
        # print("New Children: ")
        # for j in pop.next_individuals:
        #     print(j.key)

        ################################################################
        # Repopulate the current individuals with next_individuals
        ################################################################
        pop.repopulate()

def genetic_xor_decrypt_explain_test():
    bin_encrypted = get_message_binary("results/output_6_bits.txt")
    expected = get_message()

    start = timer()
    output = genetic_xor_decrypt(bin_encrypted, 6, expected)
    end = timer()
    print("Took " + str(end - start) + " seconds")
    #print(output.get_text_from_bitvector())

if __name__ == "__main__":
    #bin_encrypted = get_message_binary("results/output_14_bits.txt")

    #expected = get_message()
    genetic_xor_decrypt_explain_test()




