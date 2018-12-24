# pytest_cov_pool_datafiles_250
A code to reproduce the pytest-cove issue with data files and multiprocessing.Pool

https://github.com/pytest-dev/pytest-cov/issues/250


    pipenv shell & pipenv install
  
    pytest --cov=src --cov-report=term-missing  tests/test_cov_pool.py
