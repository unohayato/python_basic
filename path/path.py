from pathlib import Path

path = Path.cwd()
print(path)
dir1 = path / 'dir1' / 'dir2'
print(dir1)

dir1_g = dir1.iterdir()


# for x in dir1_g:
#   print(x.name)

paths =  [str(x) for x in dir1_g]
print(paths)