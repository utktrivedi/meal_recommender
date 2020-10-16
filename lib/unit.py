#ToDo : Add type of measurement (Weight, Volume)
#ToDo : How to incorportate t, tsp. , tablesoop etc as same inputs

class unit():
    """
    Generic class to define a measurement unit. It contains following attributes
    Name : Name of the unit e.g. gms
    Property_ : Fundamental characterstic being measured e.g. Weight or Volume
    si_conv_factor : Used to convert units to SI unit e.g. gms = 0.001 kg -> si_conv_factor=0.001 (cannot handle temprature units)
    Aliases : List of other names the unit might be known by e.g. grams, gram, gramme
    """
    def __init__(self, name:str, property_:str, si_conv_factor:float, aliases=None):
        self.name=name              #name of the unit eg gram
        self.property=property_     #Property being measured e.g. Weight/ Volume
        self.si_conv_factor= si_conv_factor
        if aliases is None:
            self.aliases = []
        else:
            if isinstance(aliases,list):
                self.aliases=aliases    #list of other aliases for unit e.g. g for gram
            else:
                Exception
    
    def __repr__(self):
        return "unit('{}','{}','{}','{}')".format(self.name,self.property,self.si_conv_factor,self.aliases) 
    
    def add_alias(self,alias:str):
        """Method to add alias to exitng aliases of unit, can be used to manipulate aliases during runtime"""
        if alias not in self.aliases:
            self.aliases.append(alias)
    
    def remove_alias(self, alias:str):
        """Method to remove alias from exitng aliases, can be used to manipulate aliases during runtime"""
        if alias in self.aliases:
            self.aliases.remove(alias)
    
    def convertion_factor(self, other):
        """This method return the converstion factors between units measuring same property e.g. weight, volume"""
        if self.property == other.property:
            return self.si_conv_factor/other.si_conv_factor
        else:
            Exception
    
class weight_unit(unit):
    """Class to handle weight units like kg,g, pound, ounce"""
    kg=unit('kg','Weight',1,['kg','kgs','kilogram',"kilogramme"])
    si_unit = kg
    def __init__(self,name:str,si_conv_factor:float,aliases=None):
        super().__init__(name,"Weight",si_conv_factor, aliases)

class volume_unit(unit):
    """Class to handle volume units like liter, ml, fl oz"""
    meter_cube = unit("meter_cube","Volume", 1, ['m3','m^3','meter_cube','meter3','meter^3'])
    si_unit = meter_cube
    def __init__(self,name:str,si_conv_factor:float,aliases=None):
        super().__init__(name,"Volume",si_conv_factor,aliases)

