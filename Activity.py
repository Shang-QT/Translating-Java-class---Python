class Dog:
    def __init__(itself, name, age):
        itself.name = name
        itself.age = age
    
    def bark(isself):
        print("Woof! Woof!")
    
    def celebrateBirthday(itself):
        itself.age += 1
        print(f"Happy birthday! {itself.name} is now {itself.age} years old!")
    
    def getInfo(itself):
        return f"Dog Name: {itself.name}, Age: {itself.age}"

if __name__ == "__main__":
    name = input("Enter the dog's name: ")
    age = int(input("Enter the dog's age: "))
    
    mydog = Dog(name, age)
    mydog.bark()
    mydog.celebrateBirthday()
    print(mydog.getInfo())
