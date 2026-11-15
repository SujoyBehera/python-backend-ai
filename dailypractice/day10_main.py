from day10_models import ServerConfig, BaseEmployee, Developer
cfg1 = ServerConfig(host="localhost")
cfg2 = ServerConfig(host="localhost", port=8000, debug=False)
assert cfg1.get_url() == "https://localhost:8000"
assert cfg1 ==cfg2
print(cfg1)
emp = BaseEmployee(name="Aditya", base_salary=50000)
dev = Developer("Sujoy Behera", 50000, 200000)
assert emp.calculate_salary()==50000
assert dev.calculate_salary()==250000
print(dev.name)

