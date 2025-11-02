import numpy as np

# Solve quadratic in x for given k and y
def solve_for_x(k, y):
    a = -283.3333
    b = 98.7865 + 0.1838 * y
    c = -200.1912 + 0.3383 * y - 0.0001*y**2 - k

    disc = b**2 - 4*a*c
    if disc < 0:
        return None
    sqrt_disc = np.sqrt(disc)
    x1 = (-b + sqrt_disc) / (2*a)
    x2 = (-b - sqrt_disc) / (2*a)
    # pick root with smaller absolute value
    for x in [x1, x2]:
        if np.isfinite(x):
            return x
    return None

# Step size for k
k_values = np.arange(6, 204, 0.5)
points = []

# Scan y between 750 and 2000
y_scan = np.linspace(750, 2000, 1000)  # fine grid

for k in k_values:
    found = False
    for y in y_scan:
        x = solve_for_x(k, y)
        if x is not None:
            points.append((x, y))
            found = True
            break
    if not found:
        points.append((np.nan, np.nan))  # fallback if no solution

# Print Java array with 3 decimals
print("double[][] points = {")
for x, y in points:
    if np.isnan(x) or np.isnan(y):
        print("    {Double.NaN, Double.NaN},")
    else:
        print(f"    {{{x:.3f}, {y:.3f}}},")
print("};")

