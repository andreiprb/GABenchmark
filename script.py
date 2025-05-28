import numpy as np
import random
from typing import List
import itertools
from dataclasses import dataclass

from fitness import binary_to_real, fitness_function, sphere, ackley
from selection import selection_wrapper
from crossover import crossover_wrapper
from mutation import mutation_wrapper
from config import *


@dataclass
class GAResult:
    """Store results of a GA run"""
    best_fitness: float
    best_solution: List[int]
    convergence_history: List[float]
    selection_id: int
    crossover_id: int
    mutation_id: int


def run_ga(selection_id: int, crossover_id: int, mutation_id: int) -> GAResult:
    population = [[random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)] for _ in range(POPULATION_SIZE)]

    best_fitness_history = []
    best_overall_fitness = float('inf')
    best_overall_solution = None

    for generation in range(NUM_GENERATIONS):
        fitness_values = [fitness_function(chr) for chr in population]

        gen_best_idx = np.argmin(fitness_values)
        gen_best_fitness = fitness_values[gen_best_idx]

        if gen_best_fitness < best_overall_fitness:
            best_overall_fitness = gen_best_fitness
            best_overall_solution = population[gen_best_idx][:]

        best_fitness_history.append(best_overall_fitness)

        new_population = []

        new_population.append(population[gen_best_idx][:])

        parents = selection_wrapper(population, fitness_values, POPULATION_SIZE, selection_id)

        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)

            child1, child2 = crossover_wrapper(parent1, parent2, crossover_id)

            child1 = mutation_wrapper(child1, mutation_id)
            child2 = mutation_wrapper(child2, mutation_id)

            new_population.extend([child1, child2])

        population = new_population[:POPULATION_SIZE]

    return GAResult(
        best_fitness=best_overall_fitness,
        best_solution=best_overall_solution,
        convergence_history=best_fitness_history,
        selection_id=selection_id,
        crossover_id=crossover_id,
        mutation_id=mutation_id
    )


def grid_search():
    operator_names = {
        'selection': ['Tournament', 'Roulette Wheel', 'Rank'],
        'crossover': ['Single Point', 'Uniform', 'Two Point'],
        'mutation': ['Bit Flip', 'Swap', 'Inversion']
    }

    results = []

    print("Starting Grid Search...")
    print(f"Testing {3 ** 3} = 27 combinations")
    print("-" * 80)

    for sel_id, cross_id, mut_id in itertools.product(range(3), repeat=3):
        print(f"\nTesting: {operator_names['selection'][sel_id]} | "
              f"{operator_names['crossover'][cross_id]} | "
              f"{operator_names['mutation'][mut_id]}")

        trial_results = []
        for trial in range(NUM_SIMULATIONS):
            result = run_ga(sel_id, cross_id, mut_id)
            trial_results.append(result.best_fitness)
            print(f"  Trial {trial + 1}: {result.best_fitness:.6f}")

        avg_fitness = np.mean(trial_results)
        std_fitness = np.std(trial_results)

        results.append({
            'selection': sel_id,
            'crossover': cross_id,
            'mutation': mut_id,
            'avg_fitness': avg_fitness,
            'std_fitness': std_fitness,
            'selection_name': operator_names['selection'][sel_id],
            'crossover_name': operator_names['crossover'][cross_id],
            'mutation_name': operator_names['mutation'][mut_id]
        })

        print(f"  Average: {avg_fitness:.6f} (±{std_fitness:.6f})")

    results.sort(key=lambda x: x['avg_fitness'])

    print("\n" + "=" * 80)
    print("TOP 3 COMBINATIONS:")
    print("=" * 80)

    for i, result in enumerate(results[:3]):
        print(f"\n{i + 1}. {result['selection_name']} | {result['crossover_name']} | {result['mutation_name']}")
        print(f"   Average Fitness: {result['avg_fitness']:.6f} (±{result['std_fitness']:.6f})")
        print(
            f"   IDs: Selection={result['selection']}, Crossover={result['crossover']}, Mutation={result['mutation']}")

    return results


if __name__ == "__main__":
    print(f"GA Configuration:")
    print(f"  Chromosome Length: {CHROMOSOME_LENGTH} (X={X}, Y={Y}, Z={Z})")
    print(f"  Population Size: {POPULATION_SIZE}")
    print(f"  Generations: {NUM_GENERATIONS}")
    print(f"  Crossover Probability: {CROSSOVER_PROB}")
    print(f"  Mutation Probability: {MUTATION_PROB}")
    print(f"  Fitness Function: sphere^2 * ackley (2D)")
    print()

    all_results = grid_search()

    print("\n" + "=" * 80)
    print("Running best configuration in detail...")
    best_config = all_results[0]

    detailed_result = run_ga(
        best_config['selection'],
        best_config['crossover'],
        best_config['mutation']
    )

    real_solution = binary_to_real(detailed_result.best_solution, BOUNDS, X)
    print(f"\nBest solution found: {real_solution}")
    print(f"Best fitness: {detailed_result.best_fitness:.6f}")
