class Stack:
    """Stack Class."""
    
    def __init__(self):
        self.__elements = []
    
    def push(self, value):
        self.__elements.append(value)
    
    def size(self):
        return len(self.__elements)
    
    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato
    
    def ontop(self):
        if self.size() > 0:
            return self.__elements[-1]
        
    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Stack):
            return self.__elements == stack_aux.__elements
        else:
            return False
    
    def vacia(self):
        return self.ontop() is None
    
        


        
