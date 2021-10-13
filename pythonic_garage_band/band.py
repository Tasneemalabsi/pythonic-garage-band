

class Guitarist:
    """
    """
    def __init__(self,name):
        self.name=name
        self.sound="face melting guitar solo"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    # def play_solo(self):
    #     return self.instrument

class Drummer:
    """
    """
    def __init__(self,name):
        self.name=name
        self.sound="bom bom buh bom"
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}" 
    # def play_solo(self):
    #     return self.instrument    

class Bassist:
    """
    """
    def __init__(self,name,sound):
        self.name=name
        self.sound="rattle boom crash"
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}" 
    # def play_solo(self):
    #     return self.instrument    

class Band:
    def __init__(self,name,members,sound):
        self.name=name  
        self.members=members 
        self.sound=str(sound)

    def play_solo(self):
        return self.sound                   
          




