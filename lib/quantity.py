import unit 

class quantity():
    def __init__(self,amount:int,unit_:str):
        self.amount=amount
        self.unit=unit_

    def from_string(self):
        pass
    def convert_to(self):
        pass

colors = ['red','green','red','blue','green','red']
d={}
for color in colors:
    if color not in d:
        d[color]=0
    print(str(d))
    d[color] += 1
    print(str(d))      