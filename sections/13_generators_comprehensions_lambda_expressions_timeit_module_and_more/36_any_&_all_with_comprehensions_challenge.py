from data import plants_dict

if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
    print("This dict contains grasses")
else:
    print("No grasses in the dict")

if any(plants_dict[key].plant_type == "Grass" for key in plants_dict):
    print("This dict contains grasses")
else:
    print("No grasses in the dict")
