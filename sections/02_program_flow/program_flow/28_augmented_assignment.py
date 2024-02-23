# Augmented Assignment == 'Arttırılmış Atama':
# The combination, in a single statement, of a binary operation and an assignment statement.

guesses = 0
guesses = guesses + 1
# It binds that new variable to the result of performing the calculation, then destroys the original variable.

# OR:
guesses += 1  # More efficient <<<
# Using an augmented assignment, it can perform the operation in-place where possible, modifying the original variable.
# This isn't always possible, depending on the type of object (variable) in question, but will be done in place whenever
# possible.
