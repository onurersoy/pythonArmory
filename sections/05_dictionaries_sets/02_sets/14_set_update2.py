from prescription_data import adverse_interactions

# We actually could replace the below for loop with a single line of code by using 'unpacking' technic...
meds_to_watch = set()  # To hold our unified sets, we initialized an empty set first.

# for interaction in adverse_interactions:
# UNION:
#     # meds_to_watch = meds_to_watch.union(interaction)
#     meds_to_watch = meds_to_watch | interaction

# UNPACKING:
meds_to_watch.update(*adverse_interactions)

print(meds_to_watch)
print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')
