from typing import List, Tuple
import random

from config import CROSSOVER_PROB

def single_point_crossover(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    if random.random() > CROSSOVER_PROB:
        return parent1[:], parent2[:]

    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2


def uniform_crossover(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    if random.random() > CROSSOVER_PROB:
        return parent1[:], parent2[:]

    child1, child2 = [], []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])

    return child1, child2


def two_point_crossover(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    if random.random() > CROSSOVER_PROB:
        return parent1[:], parent2[:]

    points = sorted(random.sample(range(1, len(parent1)), 2))

    child1 = parent1[:points[0]] + parent2[points[0]:points[1]] + parent1[points[1]:]
    child2 = parent2[:points[0]] + parent1[points[0]:points[1]] + parent2[points[1]:]

    return child1, child2


def crossover_wrapper(parent1: List[int], parent2: List[int], method_id: int) -> Tuple[List[int], List[int]]:
    methods = {
        0: single_point_crossover,
        1: uniform_crossover,
        2: two_point_crossover
    }
    return methods[method_id](parent1, parent2)