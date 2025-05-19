import os

class Directory:
    def __init__(self, path):
        self.path = path
        self.dirname, self.filename = os.path.split(self.path)
    
    ## Directory Functions ##
    def clear(self):
        for file in os.listdir(self.path):
            os.remove(file)
    
    def get_content(self, extentions=None):
        files = []
        
        for file in os.listdir(self.path):
            if extentions == None:
                files.append(file)
            elif os.path.splitext(file)[1] == extentions:
                files.append(file)
            else: return None
            
        return files
    
    ## Directory Property's ##
    @property
    def path(self):
        return self.path

    @property
    def parent(self):
        return self.dirname