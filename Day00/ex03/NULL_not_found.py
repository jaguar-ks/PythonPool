def get_variable_name(var):
    names = {id(v): k for k, v in globals().items()}
    return names.get(id(var), None)

def NULL_not_found(object: any) -> int:
    name = get_variable_name(object)
    if name is None:
        print("Type not found")
        return 1
    else:
        print(f"{name}: {object} {type(object)}")
        
if __name__ == '__main__':
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
