import enum

#Making a class for all the units of Measurement
#source: https://en.wikibooks.org/wiki/Cookbook:Units_of_measurement

#ToDo : Add type of measurement (Weight, Volume)
#ToDo : How to incorportate t, tsp. , tablesoop etc as same inputs

class unit(enum.Enum):
    tsp=1  #teaspoon (also t or tsp.)
    tbl=2  #tablespoon (also T, tbl., tbs., or tbsp.)
    fl_oz=3  #fluid ounce (also fl oz)
    gill=4  #gill (about 1/2 cup)
    cup=5 #cup (also c)
    pt=6  #pint (also p, pt, or fl pt - Specify Imperial or US)
    qt=7  #quart (also q, qt, or fl qt - Specify Imperial or US)
    gal=8  #gallon (also g or gal - Specify Imperial or US)
    ml=9  #ml, also milliliter, millilitre, cc (and mL only in the US, Canada and Australia).
    l=10  #l, also liter, litre, (and L only in the US, Canada and Australia).
    dl=11  #dl, also deciliter, decilitre (and dL only in the US, Canada and Australia).
    lb=12 #pound (also lb or #)
    oz=13 #ounce (also oz)
    mg=14 #mg (also milligram or milligramme)
    g=15 #g (also gram or gramme)
    kg=16 #kg (also kilogram or kilogramme)

class quantity():
    def __init__(self,amount,unit):
        self.amount=amount
        self.unit=unit      