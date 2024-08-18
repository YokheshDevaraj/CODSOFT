import random
import string

def generator(length):
    
    char=string.ascii_letters+string.digits+string.punctuation
    
    password=''.join(random.choice(char) for _ in range(length))
    return password

def main():
    
    while True:
        try:
            length=int(input("Enter the length of the password:"))
            if length<1:
                raise ValueError("Length must be one or above one")
            break
        except ValueError:
            print("Please enter a number")

    
    password=generator(length)
    print(f"Generated password:{password}")


main()
