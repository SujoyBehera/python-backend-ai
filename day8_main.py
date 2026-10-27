from helpers import clean_tags, add_tag
assert clean_tags("") == []
assert add_tag("a") == ["a"]
assert add_tag("b") == ["b"]   

result = clean_tags("  Python,   FastAPI, pyhton")
print(result)