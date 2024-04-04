# The symmetric difference is the opposite of intersection.
# It produces the set of items that are in one set or the other, but not in both.
# (A/B) U (B/A)

morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}

possible_courses1 = morning ^ afternoon  # << symmetric difference operator
print(possible_courses1)
possible_courses2 = morning.symmetric_difference(afternoon)  # << symmetric difference method
print(possible_courses2)
