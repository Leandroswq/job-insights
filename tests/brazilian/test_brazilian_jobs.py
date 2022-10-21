from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    jobs = read_brazilian_file(path)
    job_keys = [key for key in jobs[0].keys()]
    job_keys.sort()
    
    valid_keys = ["title", "salary", "type"]
    valid_keys.sort()
    
    is_valid_array = [
        False
        for key_index in range(len(valid_keys))
        if valid_keys[key_index] != job_keys[key_index]
    ]

    assert len(is_valid_array) == 0
