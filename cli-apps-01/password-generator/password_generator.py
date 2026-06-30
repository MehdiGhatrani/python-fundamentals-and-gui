# import and global variebles
from abc import ABC, abstractmethod
import string
import random


# create password generator abstract class
class PasswordGeneratorAbtract(ABC):
    @abstractmethod
    def password_generator(self, length=8):
        pass
    

# create numeric password generator
class NumericPasswordGenerator(PasswordGeneratorAbtract):
        
    letters = string.digits + string.punctuation

    def password_generator(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))


# create letters password generator
class LetterPasswordGenerator(PasswordGeneratorAbtract):
        
    
    letters = string.ascii_letters + string.punctuation

    def password_generator(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))


# create mixed password generator
class MixedPasswordGenerator(PasswordGeneratorAbtract):
        
    letters = string.ascii_letters +string.digits+ string.punctuation

    def password_generator(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))

# main function
def main():
    password1 = MixedPasswordGenerator()
    password2 = LetterPasswordGenerator()
    password3 = NumericPasswordGenerator()

    pass_list = [password1, password2, password3]

    for i in pass_list:                 #Train Polymorphism
        print(i.password_generator()) 



if __name__ == "__mai‍n__":
    main()
