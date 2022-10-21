from src.sorting import sort_by


def test_sort_by_criteria():
    job1 = {"max_salary": 1000, "min_salary": 10, "date_posted": "2020-05-18"}
    job2 = {"max_salary": 100, "min_salary": 30, "date_posted": "2020-05-21"}
    job3 = {"max_salary": 200, "min_salary": 28, "date_posted": "2020-06-18"}

    jobs = [job1, job2, job3]

    sort_by(jobs, "min_salary")
    jobs_sorted_by_min_salary = [job1, job3, job2]

    assert jobs == jobs_sorted_by_min_salary

    sort_by(jobs, "max_salary")
    jobs_sorted_by_max_salary = [job1, job3, job2]

    assert jobs == jobs_sorted_by_max_salary

    sort_by(jobs, "date_posted")
    jobs_sorted_by_date_posted = [job3, job2, job1]
    assert jobs == jobs_sorted_by_date_posted
