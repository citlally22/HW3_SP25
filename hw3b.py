import math

def t_distribution_cdf(degrees_of_freedom, z):
    """
    Compute the cumulative probability for a t-distribution value.

    :param degrees_of_freedom: Number of degrees of freedom (int)
    :param z: t-value (float)
    :return: Computed cumulative probability
    """
    # Define the t-distribution probability density function (PDF)
    def t_pdf(t, df):
        gamma_factor = math.gamma((df + 1) / 2) / (
            math.sqrt(df * math.pi) * math.gamma(df / 2)
        )
        return gamma_factor * (1 + (t**2) / df) ** (-(df + 1) / 2)

    # Simpson's Rule for numerical integration
    def simpson_rule(f, a, b, n=100):
        if n % 2 == 1:
            n += 1  # Ensure an even number of intervals
        h = (b - a) / n
        result = f(a) + f(b)

        for i in range(1, n):
            x = a + i * h
            result += 4 * f(x) if i % 2 == 1 else 2 * f(x)

        return result * (h / 3)

    # Integrate from -infinity to z
    if z < 0:
        return 1 - t_distribution_cdf(degrees_of_freedom, -z)
    a = -10  # Lower bound approximation for -infinity
    cumulative_probability = 0.5 + simpson_rule(lambda t: t_pdf(t, degrees_of_freedom), 0, z, 100)
    return cumulative_probability

def main():
    """
    Prompt user for degrees of freedom and z-values, and compute t-distribution probabilities.
    """
    print("T-Distribution Cumulative Probability Calculator")

    # Get degrees of freedom from the user
    while True:
        try:
            degrees_of_freedom = int(input("Enter degrees of freedom (positive integer): "))
            if degrees_of_freedom <= 0:
                raise ValueError("Degrees of freedom must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    # Get z-values from the user
    z_values = []
    for i in range(3):
        while True:
            try:
                z = float(input(f"Enter z-value {i + 1}: "))
                z_values.append(z)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    print("\nResults:")
    for z in z_values:
        probability = t_distribution_cdf(degrees_of_freedom, z)
        print(f"For z = {z:.5f} and degrees of freedom = {degrees_of_freedom}, P = {probability:.5f}")

if __name__ == "__main__":
    main()
