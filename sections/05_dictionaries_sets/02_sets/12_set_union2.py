from prescription_data import adverse_interactions

meds_to_watch = set()  # To hold our unified sets, we initialized an empty set first.

for interaction in adverse_interactions:
    # UNION:
    # meds_to_watch = meds_to_watch.union(interaction)
    meds_to_watch = meds_to_watch | interaction
print(meds_to_watch)
print(sorted(meds_to_watch))
