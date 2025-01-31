def NULL_not_found(object: any) -> int:
    # Check for specific "null-like" objects and print their type
    if object is None:
        print(f"Nothing: None {type(object)}")
    elif isinstance(object, float) and object != object:  # NaN check
        print(f"Cheese: nan {type(object)}")
    elif object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == '':
        print(f"Empty: {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0
