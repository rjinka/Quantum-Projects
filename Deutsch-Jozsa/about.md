# About the Deutsch-Jozsa Quantum Algorithm

The **Deutsch-Jozsa algorithm** is a foundational quantum algorithm that demonstrates the potential speedup quantum computers can achieve over classical computers. It was one of the first examples to show that quantum algorithms can solve certain problems exponentially faster than any deterministic classical algorithm.

## Problem Statement

Given a function \( f: \{0,1\}^n \rightarrow \{0,1\} \), which is guaranteed to be either _constant_ (returns the same output for all inputs) or _balanced_ (returns 0 for half the inputs and 1 for the other half), the task is to determine whether \( f \) is constant or balanced.

## Classical vs Quantum

- **Classical Approach:** In the worst case, a classical algorithm needs to evaluate \( f \) on \( 2^{n-1} + 1 \) inputs to be certain.
- **Quantum Approach:** The Deutsch-Jozsa algorithm can solve the problem with a single evaluation of \( f \) using quantum parallelism and interference.

## Key Steps

1. Prepare a quantum register in a superposition of all possible inputs.
2. Apply the quantum oracle representing \( f \).
3. Use quantum interference to extract the global property (constant or balanced) with a single measurement.

## Significance

The Deutsch-Jozsa algorithm illustrates the power of quantum computation and serves as a stepping stone for more complex quantum algorithms.

# First Project: Light switch problem

Imagine you're designing a smart home system, and you have a special kind of light switch with multiple inputs. Let's say it has 2 input wires, representing a binary configuration (e.g., Wire 1 is 0 or 1, Wire 2 is 0 or 1).

The light switch itself has a hidden internal logic (our "mystery function" f(x)). You're told it's one of two types:

Always ON (Constant 1): No matter what combination of inputs (00, 01, 10, 11) you provide, the light always turns ON.
Always OFF (Constant 0): No matter what combination of inputs you provide, the light always stays OFF.
Specific ON/OFF Pattern (Balanced): For exactly half of the input combinations, the light turns ON, and for the other half, it turns OFF. For example, it might be ON for (00, 11) and OFF for (01, 10). Or ON for (01, 10) and OFF for (00, 11).

Find out if the light switch is contact 0 or constant 1 or balanced
