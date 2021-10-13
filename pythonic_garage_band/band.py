



class Musician():
    """
       this class has the properties that will be passed to to the other classes that describe the names, roles and instruments of multiple musicians

    """

    def __init__(self, name, player,instrument, noise):
        self.name = str(name)
        self.player = str(player) 
        self.instrument = str(instrument)
        self.noise = noise
        self.name = name
        
    def __str__ (self):
        return (f"My name is {self.name} and I play {self.instrument}")

    def __repr__ (self):
        return (f"{self.player} instance. Name = {self.name}")

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.noise

class Band():
    names =[]
    def __init__(self, name, members):

        self.name = name
        self.members = members
        Band.names.append(self.name)

class Guitarist(Musician):
    """
    
       this class has the properties of the guitarist class that is inherited from the musician

    """
    def __init__(self, name = ""):
        self.name = str(name)
        self.player = "Guitarist" 
        self.instrument = "guitar"
        self.noise = "face melting guitar solo"

class Bassist(Musician):
    """
    
       this class has the properties of the bassist class that is inherited from the musician

    """
    def __init__(self, name = ""):
        self.name = str(name)
        self.player = "Bassist" 
        self.instrument = "bass"
        self.voice = "bom bom buh bom"


class Drummer(Musician):
    """
    
       this class has the properties of the drummer class that is inherited from the musician

    """

    def __init__(self, name = ""):
        self.name = str(name)
        self.player = "Drummer" 
        self.instrument = "drums"
        self.voice = "rattle boom crash"



