excited_dog = 'excited dog'                 
# local variable because it is without any prefixes
self.excited_dog = 'excited dog'            
# instance variable because of the self prefix
self.__class__.excited_dog = 'excited dog'  
# class variable because of the self.__class__ prefix uses the instance's class
BigDog.excited_dog = 'excited dog'          
# class variable because BigDog is a class name per the Python naming conventions