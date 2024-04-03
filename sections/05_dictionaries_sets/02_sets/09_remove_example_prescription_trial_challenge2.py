from prescription_data import *

# Improved version of '08_remove_example_prescription_trial_challenge.py' with using 'Exception':
trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban (we want them to replace):
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin."
              f" Please remove {patient} from the trial")
    print(patient, prescription)
