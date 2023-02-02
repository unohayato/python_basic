"""
with open('file/test.txt') as f:
  s = f.read()
  print(s)
  
with open('file/test.txt') as f:
  for _ in range(4):
    s_line = f.readline()
    print(s_line)
    if s_line == '':
      print('終了です。')
  
with open('file/test2.txt', 'w') as f:
  f.write('あああ\nいいい\nううう')

with open('file/test2.txt', 'a') as f:
  f.write('\nえええ\nおおお')
"""

x_list = ['apple', 'orange', 'banana']
s = '\n'.join(x_list)
with open('file/test3.txt', 'w') as f:
  f.writelines(s)