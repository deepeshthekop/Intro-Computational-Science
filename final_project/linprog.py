import numpy as np
from scipy.optimize import linprog

# List of food items
foods = ["Rice", "Maize", "Beans", "Fish", "Eggs", "Milk", "Leafy Greens", "Groundnuts", "Soybeans", "Oil"]

# Cost per kg (objective function coefficients) in dollars ($)
costs = np.array([1.2, 0.8, 1.5, 3.0, 2.5, 2.0, 0.5, 2.8, 2.2, 1.0])  # To minimize

# Nutrient content per kg [Energy (kcal), Protein (g), Iron (mg), Vitamin A (μg)]
nutrients = np.array([
    [1300, 28, 0.2, 0],      # Rice
    [1200, 25, 3.0, 0],      # Maize
    [1400, 90, 5.0, 0],      # Beans
    [900, 200, 1.5, 50],     # Fish
    [1550, 130, 2.1, 600],   # Eggs
    [700, 35, 0.5, 100],     # Milk
    [250, 20, 3.5, 3000],    # Leafy Greens
    [2500, 100, 4.0, 0],     # Groundnuts
    [1800, 120, 4.5, 0],     # Soybeans
    [9000, 0, 0, 0]          # Oil
])

# Minimum daily nutrient requirements
requirements = np.array([2100, 75, 10, 800])  # [Energy, Protein, Iron, Vitamin A]

# Constraints - Ensure nutrient requirements are met (Ax ≥ b form)
A = -nutrients.T  # Convert to ≤ form by negating and transposing
b = -requirements

# Bounds - Food quantities cannot be negative
x_bounds = [(0, None) for _ in foods]

# Solving using SciPy's linprog function
result = linprog(c=costs, A_ub=A, b_ub=b, bounds=x_bounds, method="highs")

# Result
if result.success:
    print("\nOptimal daily food basket(kg):")
    for i in range(len(foods)):
        if result.x[i] > 0:
            print(f"{'* ' + foods[i]}: {result.x[i]:.2f} kg")
    print(f"\nMinimum cost per day: ${result.fun:.2f}")
else:
    print("\nOptimization failed. No feasible solution found.")