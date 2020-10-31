import random
import pickle
from pathlib import Path

class repo():
    """This class is created to act as database for objects of classes like unit() and ingrediants()
    it has methods to add or remove items from repo, find out correct item from aliases, import and export database 
    """
    def __init__(self,name:str,file_path:str=None,object_set=None):
        self.name = name
        if file_path is None:
            self.file_path=Path.cwd()/name
        else:
            self.file_path = Path(file_path)

        if object_set is None:
            self.object_set = set([])
        else:
            if isinstance(object_set,set):
                self.object_set=object_set
            else:
                Exception
    
    def __len__(self):
        return len(self.object_set)
    
    def __repr__(self, seperator='\n'):
        """ Return random 10 records from repo"""
        if len(self.object_set)>10:
            return seperator.join(map(str,list(self.object_set)[:10]))
        else:
            return seperator.join(map(str,self.object_set))
    
    @staticmethod
    def load(file_path:str):
        with open(file_path,"rb") as f:
            payload=pickle.load(f)
        return payload
    
    def add_record(self,new_record:any):
        """ Method to add new record to repo"""
        self.object_set.add(new_record)
        #self.save()
    
    def remove_record(self,old_record:any):
        """ Method to remove a record from repo"""
        if (old_record in self.object_set):
            self.object_set.remove(old_record)
        #self.save()
    
    def save(self):
        """Method to export the repository. This will act as permanent database to repo"""
        with open(self.file_path,"wb") as f:
            pickle.dump(self,f)
    
    def refresh(self):
        """method to refresh repo from its filebase"""
        with open(self.file_path,"rb") as f:
            self=pickle.load(f)

    def find_record(self,search_word:str):
        """Method to handle various aliases of unit, ingredients etc and returns the standard record back"""
        for record in self.object_set:
            if(search_word in record.aliases):
                return record