from prescription_data import patients

# We've seen 'pop' used with a dictionary, and it can also be used with a list.
# When popping items from a set, there's a slight difference. Sets aren't indexable, so the set pop method doesn't
# take any arguments.
# It pops an arbitrary (you can't reliably predict which item will be popped from the set) item from the set, and
# returns that item.
# pop(): 'Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.

# Imagine you're processing a set of tasks, and it doesn't matter what order they're performed. Popping them from a set
# would be fine, in that case.

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trial_patients:  # it's like 'not null'
    patient = trial_patients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)
