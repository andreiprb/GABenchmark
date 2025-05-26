import numpy as np
from typing import List
import random


def tournament_selection(population: List[List[int]], fitness_values: List[float], num_parents: int) -> List[List[int]]:
    parents = []
    tournament_size = 3

    for _ in range(num_parents):
        tournament_indices = random.sample(range(len(population)), tournament_size)
        tournament_fitness = [fitness_values[i] for i in tournament_indices]
        winner_idx = tournament_indices[np.argmin(tournament_fitness)]
        parents.append(population[winner_idx][:])

    return parents


def roulette_wheel_selection(population: List[List[int]], fitness_values: List[float], num_parents: int) -> List[
    List[int]]:
    max_fitness = max(fitness_values)
    adjusted_fitness = [max_fitness - f + 1e-6 for f in fitness_values]
    total_fitness = sum(adjusted_fitness)
    probabilities = [f / total_fitness for f in adjusted_fitness]

    parents = []
    for _ in range(num_parents):
        r = random.random()
        cumulative = 0
        for i, prob in enumerate(probabilities):
            cumulative += prob
            if r <= cumulative:
                parents.append(population[i][:])
                break

    return parents


def rank_selection(population: List[List[int]], fitness_values: List[float], num_parents: int) -> List[List[int]]:
    sorted_indices = np.argsort(fitness_values)
    ranks = np.empty_like(sorted_indices)
    ranks[sorted_indices] = np.arange(len(fitness_values), 0, -1)

    total_rank = sum(ranks)
    probabilities = ranks / total_rank

    parents = []
    for _ in range(num_parents):
        r = random.random()
        cumulative = 0
        for i, prob in enumerate(probabilities):
            cumulative += prob
            if r <= cumulative:
                parents.append(population[i][:])
                break

    return parents


def selection_wrapper(population: List[List[int]], fitness_values: List[float], num_parents: int, method_id: int) -> \
List[List[int]]:
    methods = {
        0: tournament_selection,
        1: roulette_wheel_selection,
        2: rank_selection
    }
    return methods[method_id](population, fitness_values, num_parents)