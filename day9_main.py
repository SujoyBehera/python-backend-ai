from models import APIKey
key1 = APIKey("key_1", "Client A", 2)
key2 = APIKey("key_2", "Client B", 3)

print(key1.record_call())
print(key1.record_call())
print(key1.record_call())
print(key1.record_call())
print(key1.calls_made)
key1.reset_usage()
assert key1.record_call() is True
assert key1.record_call() is True
assert key1.record_call() is False
assert key2.calls_made == 0
assert key2.record_call() is True
key1.reset_usage()
assert key1.calls_made == 0
assert key1.record_call() is True

