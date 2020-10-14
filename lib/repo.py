import random

class repo():
    """This class is created to act as database for objects of classes like unit() and ingrediants()
    it has methods to add or remove items from repo, find out correct item from aliases, import and export database 
    """
    def __init__(self,object_list=None):
        if object_list is None:
            self.object_list = []
        else:
            if isinstance(object_list,list):
                self.object_list=object_list
            else:
                Exception
    
    def __repr__(self, seperator=','):
        """ Return random 10 records from repo"""
        if len(self.object_list)>10:
            return seperator.join(map(str,random.choices(self.object_list,k=10)))
        else:
            return seperator.join(map(str,self.object_list))