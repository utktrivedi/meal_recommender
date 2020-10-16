import random
import pickle
from unit import unit

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
    
    def __len__(self):
        return len(self.object_list)

    @staticmethod
    def import_repo(filename="repo_file"):
        with open(filename,"rb") as f:
            new_repo=pickle.load(f)
        return new_repo
    
    def __repr__(self, seperator=','):
        """ Return random 10 records from repo"""
        if len(self.object_list)>10:
            return seperator.join(map(str,self.object_list[:10]))
        else:
            return seperator.join(map(str,self.object_list))
    
    def add_record(self,new_record:any):
        """ Method to add new record to repo"""
        self.object_list.append(new_record)
    
    def remove_record(self,old_record:any):
        """ Method to remove a record from repo"""
        if (old_record in self.object_list):
            self.object_list.remove(old_record)
    
    def export_repo(self,filename="repo_file"):
        """Method to export the repository. This will act as permanent database to repo"""
        with open(filename,"wb") as f:
            pickle.dump(self,f)

    def find_record(self,search_word:str):
        """Method to handle various aliases of unit, ingredients etc and returns the standard record back"""
        for record in self.object_list:
            if(search_word in record.aliases):
                return record