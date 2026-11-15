from dataclasses import dataclass 
@dataclass 
class ServerConfig:
    host : str
    port : int= 8000
    debug : bool= False 

    def get_url(self) -> str:
        return f"https://{self.host}:{self.port}"

class BaseEmployee:
    def __init__(self, name: str, base_salary: int):
        self.name = name 
        self.base_salary = base_salary 
    def calculate_salary(self) -> int:
        return self.base_salary
class Developer(BaseEmployee):
    def __init__(self, name: str, base_salary: int, bonus: int):
        super().__init__(name,base_salary)
        self.bonus = bonus 

    def calculate_salary(self) -> int:
        return self.base_salary + self.bonus
    



