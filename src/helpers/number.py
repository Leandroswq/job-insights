def is_in_int_format(value):
    try:
        int(value)
    except Exception:
        return False
    return True
