#this class should be able to handle all ingredients for recepie 
class recepie():
    def __init__(self,name,kind,calories,color,aliases=None):
        self.name = name
        self.kind = kind
        self.calories = calories
        self.color = color
        if aliases is None:
            self.aliases = []
        else:
            if isinstance(aliases,list):
                self.aliases=aliases    #list of other aliases for recepie
            else:
                Exception