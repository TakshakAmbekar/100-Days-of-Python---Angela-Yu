# Name the class in PascalCase
class User:
    ...

user_1 = User()
user_1.id = "001"
user_1.username = "Annie"

print(user_1.username)




# Classes with constructor
class Person:
    # constructor function runs every time a new object is instantiated
    def __init__(self, id = "unknown", name = "unknown", age = "unknown"):
        self.id = id
        self.name = name
        self.age = age
        self.followers = set()
        self.followers_count = 0
        self.following = set()
        self.following_count = 0
    
    # class methods always have self as the first parameter
    def follow_someone(self, person):
        self.following.add(person.name)
        self.following_count = len(self.following)
        person.followers.add(self.name)
        person.followers_count = len(person.followers)
        
        
person_1 = Person()
print(person_1.name)
person_1.name = "Annie"
print(person_1.name)

person_2 = Person(1, "Takshak", 25)
print(person_2.name)

person_1.follow_someone(person_2)
print(person_1.name, "Following: ", person_1.following, person_1.following_count)
print(person_2.name, "Followers: ", person_2.followers, person_2.followers_count)
