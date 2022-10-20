def is_int(value):
    try:
        int(value)
    except ValueError:
        return False
    return True
