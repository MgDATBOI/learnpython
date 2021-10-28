"""
Bloom filters: "Lightweight" version of a hash table. Both hash tables and Bloom filters support efficient insertions and lookups. 
Bloom filters are more space efficient than hash tables, but this comes at the cost of having "false positives" for entry lookup. 
That is, Bloom filters can say with certainty that an element has not been inserted (no possibility of false negatives), 
but may indicate an element has been inserted when it has in fact not been (false positive).
"""

# https://en.wikipedia.org/wiki/Bloom_filter

from DataStructures import Stack
import pyhash

# Non cryptographic hash functions (Murmur, VNV)
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

bit_vector = [0] * 20


# Calc the output of FNV and Murmur hashes for Pikachu and Charmander.
fnv_pika = fnv("Pikachu") % 20
murmur_char = fnv("Charmander") % 20

print(fnv_pika, murmur_char)