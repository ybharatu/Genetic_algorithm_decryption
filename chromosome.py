from xor_cipher import *
from BitVector import *


class chromosome:
    def __init__(self, key, message):
        self.key = key
        self.decrypted = xor_encrypt(key, message)
        self.score = self.xor_find_fitness(self.decrypted)

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

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
        decrypt_hex = BitVector(bitstring=decrypted)
        #print(decrypt_hex.get_hex_string_from_bitvector())


        for i in range(len(expected)):
            if expected[i] == decrypted[i]:
                common += 1
            total += 1
        #print("common: " + str(common) + " Total: " + str(total))
        # print(str(self.key))
        # print("Fitness: " + str(common / total))
        #print()
        return common / total

if __name__ == "__main__":
    key = get_encryption_key("keys/key_2_bit.txt")
    decrypted = get_message("input2.txt")
    a = chromosome(key, decrypted)

