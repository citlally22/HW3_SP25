from numericalMethods import GPDF, Probability, Secant


def user_input():
    """
    Solicits user input to determine if they are providing c to find P, or providing P to find c.
    """
    mean = (float(input("Enter population mean (μ):")))
    stDev = float(input("Enter standard deviation (σ):"))
    choice = input ("Are you specifying c (to find P) or P (to find c)? (Enter 'c' or 'P'): ").strip().lower()

    if choice == 'c':
        c = float(input("Enter c value: "))
        greater_than = input("Find P(x > c)? (y/n): ").strip().lower() == 'y'
        prob = Probability(GPDF, (mean, stDev), c, GT=greater_than)
        print(f"Computed Probability: P(x {'>' if greater_than else '<'} {c}) = {prob:.5f}")

    elif choice == 'p':
        P_target = float(input("Enter desired probability P: "))
        greater_than = input("Is this for P(x > c)? (y/n): ").strip().lower() == 'y'

        def func(c):
            return Probability(GPDF, (mean, stDev), c, GT=greater_than) - P_target

        c_guess1, c_guess2 = mean, mean + stDev  # Initial guesses near mean
        c_solution, iterations = Secant(func, c_guess1, c_guess2)
        print(f"Found c: {c_solution:.5f} after {iterations} iterations")
    else:
        print("Invalid choice. Please enter 'c' or 'P'.")


if __name__ == "__main__":
    user_input()
