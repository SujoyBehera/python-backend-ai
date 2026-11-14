class APIKey:
    def __init__(self, key_id : str, client_name : str, rate_limit : int=5):
        self.key_id = key_id
        self.client_name = client_name
        self.rate_limit = rate_limit
        self.calls_made = 0
    def record_call(self)-> bool:
        if self.calls_made < self.rate_limit:
            self.calls_made += 1
            return True 
        else:
            return False
    def reset_usage(self)-> None:
        self.calls_made = 0 

        
