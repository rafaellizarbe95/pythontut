class Television:
    def __init__ (self):
    
        self.ligada=False
    
        self.canal=5
    def power(self):

        if self.ligada:
            self.ligada=False
        
        else:
            self.ligada=True
    
    def subircanal(self):
    
        self.canal += 1
    
    def descecanal(self):
    
        self.canal -= 1 
print(__name__)

if __name__=='__main__':
    televisao = Television()
    televisao.power()
    a = televisao.ligada 
    print(a)
    
