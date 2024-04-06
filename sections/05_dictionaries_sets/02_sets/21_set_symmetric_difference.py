# The symmetric difference is the opposite of intersection.
# It produces the set of items that are in one set or the other, but not in both.
# (A/B) U (B/A) == (B/A) U (A/B)

morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}

possible_courses1 = morning ^ afternoon  # << symmetric difference operator
print(possible_courses1)
possible_courses2 = morning.symmetric_difference(afternoon)  # << symmetric difference method
print(possible_courses2)
# The symmetric difference method is more readable than its operator version.
# It has another advantage – as do all these methods. You can pass an 'iterable' to it, instead of a set.

morning_list = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon_list = ['Python', 'C#', 'Java', 'C', 'Ruby']

possible_courses3 = set(morning_list).symmetric_difference(afternoon_list)
# The 1st one needs to be converted to set; for the 2nd one, you can directly pass the iterable object (it's a list on
# this example^^) to the method
print(possible_courses3)
