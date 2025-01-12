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

# Tester script
if __name__ == "__main__":
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False

    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))
