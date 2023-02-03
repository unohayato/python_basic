from typing import List 

def calc(list: List[int], x: int) -> int:
  ret = 0
  for i in range(len(list)):
    ret += list[i]
  
  return ret * x

print(calc([1, 2, 3, 4, 5], 5)) 