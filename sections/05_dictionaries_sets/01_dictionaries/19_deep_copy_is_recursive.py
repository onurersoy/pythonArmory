from contents import recipes
import copy


def my_deepcopy(d: dict) -> dict:

    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict


original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")  # we are adding an immutable value, so it won't reflect to the copied dicts
original["J-P"].append("UK")  # we are adding an immutable value, so it won't reflect to the copied dicts

original["Tim"][1].append("Cashier")  # we are adding into a mutable object, so it will reflect to the copied dicts
# unless it's a deepcopy
jp_list = original["J-P"]
jp_list[1].append("Courier")  # we are adding into a mutable object, so it will reflect to the copied dicts
# unless it's a deepcopy

print(original)
print(copy_1)  # deep copy
print(copy_2)  # our own deep copy method (it might not act like a total deep copy method as if we are copying a mutable
# object value, then our method's code would pass the exact reference of the mutable object instead of creating its own
# copy of the object, f.e. the list in this case)
