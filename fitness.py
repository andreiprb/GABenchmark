from typing import List, Tuple
import numpy as np

from config import BOUNDS, X, Y


def binary_to_real(binary_str: List[int], bounds: Tuple[float, float], bits_per_dim: int) -> List[float]:
    num_dims = len(binary_str) // bits_per_dim
    real_values = []

    for i in range(num_dims):
        start = i * bits_per_dim
        end = (i + 1) * bits_per_dim
        binary_dim = binary_str[start:end]

        decimal = sum(bit * (2 ** idx) for idx, bit in enumerate(reversed(binary_dim)))
        max_decimal = (2 ** bits_per_dim) - 1

        scaled = bounds[0] + (bounds[1] - bounds[0]) * (decimal / max_decimal)
        real_values.append(scaled)

    return real_values


def sphere(x: List[float]) -> float:
    return sum(xi ** 2 for xi in x)


def ackley(x: List[float]) -> float:
    a = 20
    b = 0.2
    c = 2 * np.pi
    n = len(x)

    sum1 = sum(xi ** 2 for xi in x)
    sum2 = sum(np.cos(c * xi) for xi in x)

    term1 = -a * np.exp(-b * np.sqrt(sum1 / n))
    term2 = -np.exp(sum2 / n)

    return term1 + term2 + a + np.exp(1)


def fitness_function(chromosome: List[int]) -> float:
    real_values = binary_to_real(chromosome, BOUNDS, X * Y)
    return sphere(real_values) ** 2 * ackley(real_values)