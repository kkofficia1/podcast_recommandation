class User():
    def __init__(self, name="user", age=0) -> None:
       self.name = name
       self.age = age
       self.known_podcasts = []
       self.languages = []
    
    