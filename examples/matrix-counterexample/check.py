"""Exact 2x2 integer counterexample to a false matrix identity."""
import json

A = ((0, 1), (0, 0))
B = ((0, 0), (1, 0))


def add(x, y):
    return tuple(tuple(x[i][j] + y[i][j] for j in range(2)) for i in range(2))


def matmul(x, y):
    return tuple(tuple(sum(x[i][k] * y[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def scale(k, x):
    return tuple(tuple(k * x[i][j] for j in range(2)) for i in range(2))


def square(x):
    return matmul(x, x)


def false_identity_sides(a, b):
    left = square(add(a, b))
    right = add(add(square(a), scale(2, matmul(a, b))), square(b))
    return left, right


def corrected_identity_holds(a, b):
    left = square(add(a, b))
    right = add(add(add(square(a), matmul(a, b)), matmul(b, a)), square(b))
    return left == right


if __name__ == "__main__":
    lhs, rhs = false_identity_sides(A, B)
    result = {
        "A": A, "B": B, "AB": matmul(A, B), "BA": matmul(B, A),
        "original_lhs": lhs, "original_rhs": rhs,
        "universal_claim_disproved": lhs != rhs,
        "corrected_identity_verified_for_example": corrected_identity_holds(A, B),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
