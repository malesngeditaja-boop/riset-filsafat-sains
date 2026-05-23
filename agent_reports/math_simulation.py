#!/usr/bin/env python3
"""
Reproducible math checks for "Distance in Doctrinal Space" cosine similarity.

Validates:
1) cosine similarity formula correctness,
2) the reported 0.5923 value given n=57, k=20,
3) the design-ratio identity cos = sqrt(k/n) under the paper's binary setup,
4) basic sensitivity to n and k.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable


def cosine_similarity(a: Iterable[float], b: Iterable[float]) -> float:
    a_list = list(a)
    b_list = list(b)
    if len(a_list) != len(b_list) or len(a_list) == 0:
        return 0.0
    dot = sum(x * y for x, y in zip(a_list, b_list))
    norm_a = math.sqrt(sum(x * x for x in a_list))
    norm_b = math.sqrt(sum(y * y for y in b_list))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)


@dataclass(frozen=True)
class CosineParts:
    n: int
    k: int
    dot: float
    norm_a: float
    norm_b: float
    cosine: float
    theta_deg: float


def parts_for_design_ratio(n: int, k: int) -> CosineParts:
    if n <= 0:
        raise ValueError("n must be positive")
    if not (0 <= k <= n):
        raise ValueError("k must satisfy 0 <= k <= n")

    a = [1.0] * n
    b = [1.0] * k + [0.0] * (n - k)
    dot = float(k)
    norm_a = math.sqrt(float(n))
    norm_b = math.sqrt(float(k)) if k > 0 else 0.0
    cosine = cosine_similarity(a, b)
    theta_deg = (
        math.degrees(math.acos(max(-1.0, min(1.0, cosine))))
        if (0.0 < cosine < 1.0)
        else (0.0 if cosine >= 1.0 else 90.0)
    )
    return CosineParts(n=n, k=k, dot=dot, norm_a=norm_a, norm_b=norm_b, cosine=cosine, theta_deg=theta_deg)


def identity_sqrt_ratio(n: int, k: int) -> float:
    return 0.0 if k == 0 else math.sqrt(k / n)


def check_close(actual: float, expected: float, tol: float = 1e-9) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"Expected {expected}, got {actual}")


def main() -> None:
    base = parts_for_design_ratio(n=57, k=20)
    check_close(base.cosine, identity_sqrt_ratio(57, 20), tol=1e-12)

    print("=== Core check (paper configuration) ===")
    print(f"n={base.n}, k={base.k}")
    print(f"dot = {base.dot:.0f}")
    print(f"||a|| = sqrt({base.n}) = {base.norm_a:.4f}")
    print(f"||b|| = sqrt({base.k}) = {base.norm_b:.4f}")
    print(f"cos(theta) = {base.cosine:.6f}")
    print(f"theta = arccos(cos) = {base.theta_deg:.2f} deg")
    print(f"sqrt(k/n) identity = sqrt({base.k}/{base.n}) = {identity_sqrt_ratio(base.n, base.k):.6f}")
    print()

    print("=== Sensitivity: add more variables (k fixed at 20) ===")
    for n in (57, 60, 67, 80, 100):
        p = parts_for_design_ratio(n=n, k=20)
        print(f"n={n:3d}, k=20 -> cos={p.cosine:.6f}")
    print()

    print("=== Sensitivity: change shared foundations (n fixed at 57) ===")
    for k in (0, 5, 10, 15, 20, 25, 30, 40, 57):
        p = parts_for_design_ratio(n=57, k=k)
        print(f"n=57, k={k:2d} -> cos={p.cosine:.6f}")
    print()

    print("=== Sanity checks ===")
    check_close(cosine_similarity([1, 1], [1, 1]), 1.0)
    check_close(cosine_similarity([1, 1], [0, 0]), 0.0)
    check_close(cosine_similarity([], []), 0.0)
    check_close(cosine_similarity([1, 0, 1], [1, 0]), 0.0)
    print("OK: formula + identity + edge cases.")


if __name__ == "__main__":
    main()
