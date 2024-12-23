# Command Examples

$ python3 stress/main.py parallel https://stackoverflow.com/questions/57126286/fastest-parallel-requests-in-python --runner 3 --booms 5

$ python3 stress/main.py sequential https://localhost:3000/api/data/persons --runner 2 --no-verify --timeout 1.0