def is_int(value):
    try:
        int(value)
    except Exception:
        return False
    return True
