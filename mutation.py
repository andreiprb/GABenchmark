from typing import List
import random

from config import MUTATION_PROB


def bit_flip_mutation(chromosome: List[int]) -> List[int]:
    mutated = chromosome[:]
    for i in range(len(mutated)):
        if random.random() < MUTATION_PROB:
            mutated[i] = 1 - mutated[i]
    return mutated


def swap_mutation(chromosome: List[int]) -> List[int]:
    mutated = chromosome[:]
    if random.random() < MUTATION_PROB:
        pos1, pos2 = random.sample(range(len(mutated)), 2)
        mutated[pos1], mutated[pos2] = mutated[pos2], mutated[pos1]
    return mutated


def inversion_mutation(chromosome: List[int]) -> List[int]:
    mutated = chromosome[:]
    if random.random() < MUTATION_PROB:
        start = random.randint(0, len(mutated) - 2)
        end = random.randint(start + 1, len(mutated) - 1)
        mutated[start:end + 1] = mutated[start:end + 1][::-1]
    return mutated


def mutation_wrapper(chromosome: List[int], method_id: int) -> List[int]:
    methods = {
        0: bit_flip_mutation,
        1: swap_mutation,
        2: inversion_mutation
    }
    return methods[method_id](chromosome)