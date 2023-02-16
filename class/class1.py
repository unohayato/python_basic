from dataclasses import dataclass

"""
#デコレータ使わないver
class User:
  def __init__(self, name, age, gender, address, birthday):
    self.name = name
    self.age = age
    self.gender = gender
    self.address = address
    self.birthday = birthday
"""
    
    

#デコレータ使うver
@dataclass
class User2:
  name: str
  age: int
  gender: str
  
user = User2("sato", 10, "man")
print(user.name)
print(user.age)