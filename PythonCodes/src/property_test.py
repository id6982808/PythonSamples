'''
Created on 2022/09/14

@author: nayuf
'''

class Sample1:
    def __init__(self):
        self.text = "sample"
    
    def get_text(self):
        return "({0})".format(self.text)

    def set_text(self, text):
        if text is None:
            self.text = ""
        else:
            self.text = text
    
    def delete_text(self):
        pass

class Sample2:
    def __init__(self):
        self.__text = "sample"
    
    @property
    def text(self):
        return "({0})".format(self.__text)
    
    @text.setter
    def text(self, text):
        if text is None:
            self.__text = "None"
        else:
            self.__text = text
    
    @text.deleter
    def text(self):
        pass
