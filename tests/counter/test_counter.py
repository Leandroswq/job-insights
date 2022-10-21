# from src.counter import count_ocurrences


from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    count = count_ocurrences(path, "test")

    excepted = 2687
    assert count == excepted
