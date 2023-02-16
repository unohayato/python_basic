from dataclasses import dataclass, field

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
  items: list = field(default_factory=lambda: ['note', 'pen'])
  
user1 = User2("sato", 10, "man")
user2 = User2("sato", 10, "man")
print(user1 == user2)