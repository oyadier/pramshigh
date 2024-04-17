from models.user import User
from datetime import datetime
import json


class FileStorage:
    file_path = "note.txt"
    __note_object = {}
    
    def __init__(self):
       self.reload()
   

    def all_obj(self, cls=None):
        if cls is not None: 
            __new = {}
            for k, v in self.__note_object.items():
                self.__new[k] = v
                return __new
            return self.__note_object
    
    
    def save(self, obj=None):
        json_f = {}
        if obj is not None:
            k = obj.__class__.__name__ + "."+ obj.to_dict()["id"][:8]
            if obj.first_name and obj.last_name is not None:
                
                self.__note_object[k]= obj.to_dict()
               # self.delete(k)
                with open("note.txt", 'w') as file:
                    json.dump(self.__note_object, file, indent=0)
                    self.count()
                    file.close()
                
    def count(self):
        ct = len(self.__note_object)
        print (ct)
        return ct
    
    def deletes(self, by_id=None):
        print(by_id)
        if by_id in self.__note_object:
            self.__note_object.pop(by_id)
            self.count()
            self.reload()
            print(f"{by_id} with value: {self.__note_object[by_id]} is deleted")
               # del self.__note_object[k]
    
    def reload(self):
        try:
            with open(f"{self.file_path}", 'r') as note:
                notes = json.load(note)
                for k in notes:
                    self.__note_object[k] = notes[k]
                    print("Reloading data")
        except Exception:
            pass
                