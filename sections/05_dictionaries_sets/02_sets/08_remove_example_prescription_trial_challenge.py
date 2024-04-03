from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban (we want them to replace):
for patient in trial_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        # Check this last:
        # However, this isn't an ideal solution. Performing that test, on line 8, takes time – testing conditions is
        # a relatively slow operation. Our trial could include thousands, or tens of thousands, of patients. It's wise
        # to use 'Exception' here, but we did not cover it yet. We'll be covering it soon tho.
        prescription.remove(warfarin)
    # prescription.discard(warfarin)
    # We could have use 'discard' too, but if a patient normally isn't using Warfarin, it wouldn't give us any error
    # but would add 'Edoxaban' to his/her prescription. What we wanted to achieve was replacing them, not adding
    # Edoxaban to someone that not using Warfarin. That's why 'remove' is the best option here because it would give
    # us an error if the patient doesn't have Warfarin on the prescription.

    # A crash is definitely better than killing Kenny. You may be thinking "hy don't we just check if warfarin is
    # in the set, before we try to remove it?" We could definitely do that. Let's do it^^ (Line 8)
        prescription.add(edoxaban)
    else:
        print(f"Patient {patient} is not taking Warfarin."
              f" Please remove {patient} from the trial")
    print(patient, prescription)
