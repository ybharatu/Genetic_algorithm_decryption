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
        pop.individuals = sorted(pop.individuals, reverse=True)

        ################################################################
        # Print Individuals of Current Generation
        ################################################################
        # print("GENERATION " + str(pop.num_generations))
        # for j in pop.individuals:
        #     print(j.key)

        ################################################################
        # Finish early if key has been found
        ################################################################
        if pop.individuals[0].score == 1:
            #print("Took " + str(pop.num_generations) + " Generations to decrypt")
            #print("Key is : " + str(pop.individuals[0].key))
            return pop.individuals[0].key, pop.num_generations

        ################################################################
        # Find elites to carry over to the next generation, so
        # generations will always get better
        ################################################################
        for j in range(NUM_ELITES):
            new_elite = chromosome(pop.individuals[j].key, pop.get_bin_encrypted())
            pop.elites.append(new_elite)
            pop.next_individuals.append(new_elite)
            # print("Elites: " + str(pop.individuals[j].key))

        ################################################################
        # Crossover most fit chromosomes to produce offspring
        ################################################################
        pop.crossover_chrmosomes()

        ################################################################
        # Create Mutations
        ################################################################
        pop.mutate_chromosomes()

        ################################################################
        # Repopulate the current individuals with next_individuals
        ################################################################
        pop.repopulate()

    pop.individuals = sorted(pop.individuals, reverse=True)
    print("Couldn't find the key, maybe try increasing MAX_GENERATIONS?")
    return pop.individuals[0].key, pop.num_generations

################################################################
# A test that can be redirected to a text file (explain.txt),
# which can highlight important parts of genetic algorithms.
# Need to uncomment print statements though
################################################################
def genetic_xor_decrypt_explain_test():
    bin_encrypted = get_message_binary("results/output_6_bits.txt")
    expected = get_message()

    start = timer()
    output, num_generations = genetic_xor_decrypt(bin_encrypted, 6, expected)
    end = timer()
    print("Took " + str(end - start) + " seconds")
    #print(output.get_text_from_bitvector())

################################################################
# A test where it tries various bit sized key and tabulates the
# info to be used for analysis
################################################################
def genetic_xor_decrypt_full_test():
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
    print("Number of bits   Number of Generations   Total Time(sec)     Value of Key")
    print("--------------   ---------------------   ---------------     ------------")
    for i in all_results:
        encrypted_bin = get_message_binary(i)
        start = timer()
        found_key, num_gen = genetic_xor_decrypt(encrypted_bin, j, expected)
        end = timer()
        print("{:<16d} {:<20d} {:>14.9f}         {:>s}".format(j, num_gen, end - start, str(found_key)))
        j += 1

if __name__ == "__main__":
    #bin_encrypted = get_message_binary("results/output_14_bits.txt")

    #expected = get_message()
    #genetic_xor_decrypt_explain_test()
    genetic_xor_decrypt_full_test()




