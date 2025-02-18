import numpy as np
#from sympy import Matrix

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
print("Vector1 : ", vector1)
print("Vector1 : ", vector2)

#scaled_vector = 2 * vector1
#print("Scaled Vector: ", scaled_vector)

print("\n")

magnitude_vector1 = np.linalg.norm(vector1)
magnitude_vector2 = np.linalg.norm(vector2)

print("Magnitude of Vector1: ", magnitude_vector1)
print("Magnitude of Vector2: ", magnitude_vector2)

print("\n")

dot_product = np.dot(vector1, vector2)
print("Vector Product: ", dot_product)

print("\n")