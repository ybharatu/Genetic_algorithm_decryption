from xor_cipher import *

class chromosome:
    def __init__(self, key, decrypted):
        self.key = key
        self.decrypted = decrypted
        self.score = self.xor_find_fitness(decrypted)

    def get_key(self):
        return self.key

    def get_decrypted(self):
        return self.decrypted

    def get_score(self):
        return self.score

    def xor_find_fitness(self, decrypted):
        common = 0
        total = 0
        expected = get_message()


        for i in range(len(expected)):
            if expected[i] == decrypted[i]:
                common += 1
            total += 1
        print ("Fitness: " + str(common / total))
        return common / total


if __name__ == "__main__":
    key = get_encryption_key("keys/key_2_bit.txt")
    decrypted = get_message("input2.txt")
    a = chromosome(key, decrypted)

