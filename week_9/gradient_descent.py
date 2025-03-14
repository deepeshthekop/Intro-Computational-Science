#f(x) = x^2 + 4

x = 5
alpha = 0.1
tolerance = 0.001
max_iterations = 100

for i in range(max_iterations):
    gradient = 2 * x  # Derivative of f(x) = x^2 + 4
    x_new = x - alpha * gradient
    
    if abs(x_new - x) < tolerance:
        break
    
    x = x_new

print("Minimum occurs at x~ ", x)