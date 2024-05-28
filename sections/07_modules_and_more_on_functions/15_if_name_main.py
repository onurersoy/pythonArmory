def area_of_square(length: float) -> float:
    return length * length

if __name__ == '__main__':
    # Dunder 'name' is bound to the string dunder 'main'. As we've seen, when we import this module, dunder 'name' will
    # be bound to the module's name. So this code shouldn't execute if this module is imported into another module. So
    # that's how you avoid exdcuting all the code (including the part you don't want) getting executed from another
    # module where you import this module.
    area = area_of_square(50)
    print(area)
