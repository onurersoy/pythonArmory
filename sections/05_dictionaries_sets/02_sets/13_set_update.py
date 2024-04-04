from prescription_data import adverse_interactions

# 'update': Update the set, adding elements from the other sets, 'without creating a new set' unlike 'union'.
meds_to_watch = set()

for interaction in adverse_interactions:
    # UNION:
    # meds_to_watch = meds_to_watch.union(interaction)
    # meds_to_watch = meds_to_watch | interaction
    # UPDATE:
    meds_to_watch = meds_to_watch.update(interaction)  # << 'update method'
    # It's more efficient to use 'update' if you don't want to create a new set.

    # meds_to_watch |= interaction  # << 'update operator'
    # It's also the same with 'update'^^ (augmented).

    # Note that update method has an advantage over update operator because you can pass an 'iterable' to the method.
    # The operator one would only accept another 'set'.
    # The update method is also more readable than the operator.
print(meds_to_watch)
print(sorted(meds_to_watch))
