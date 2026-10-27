import sys

print(f"Running Python from: {sys.prefix}")
assert ".venv" in sys.prefix
print("Day 6 Local Environment & venv Verified! ")
