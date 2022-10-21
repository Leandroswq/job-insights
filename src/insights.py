from src.jobs import read
from src.helpers.number import is_in_int_format


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    jobs = read(path)
    jobs_types = set([job["job_type"] for job in jobs])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_job = [
        job for job in jobs if job["job_type"].lower() == job_type.lower()
    ]

    return filtered_job


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs = read(path)
    industry_types = set(
        [job["industry"] for job in jobs if job["industry"] != ""]
    )
    return industry_types


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_job = [
        job for job in jobs if job["industry"].lower() == industry.lower()
    ]

    return filtered_job


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    jobs = read(path)
    jobs_max_salaries = set(
        [
            int(job["max_salary"])
            for job in jobs
            if is_in_int_format(job["max_salary"])
        ]
    )

    max_salary = max(jobs_max_salaries)
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    jobs_mim_salaries = set(
        [
            int(job["min_salary"])
            for job in jobs
            if is_in_int_format(job["min_salary"])
        ]
    )

    min_salary = min(jobs_mim_salaries)
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    min_salary = job["min_salary"] if "min_salary" in job else ""
    max_salary = job["max_salary"] if "max_salary" in job else ""

    print(f"-- salary: {salary}, min {min_salary}, max {max_salary}--")

    if min_salary == "":
        raise ValueError("min_salary doesn't exists")
    if max_salary == "":
        raise ValueError("max_salary doesn't exists")
    if is_in_int_format(min_salary) != True:
        raise ValueError("min_salary aren't valid integer")
    if is_in_int_format(max_salary) != True:
        raise ValueError("max_salary aren't valid integer")
    if not isinstance(salary, int):
        raise ValueError("salary isn't a valid integer")

    min_salary = int(min_salary)
    max_salary = int(max_salary)

    if min_salary > max_salary:
        raise ValueError("min_salary  is greather than max_salary ")

    if min_salary <= salary <= max_salary:
        response = True
    else:
        response = False

    print(
        f"== salary: {salary}, min {min_salary}, max {max_salary}, response {response} =="
    )
    return response


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
