import argparse

if __name__ == '__main__':
  # parser = argparse.ArgumentParser()
  # parser.add_argument(
  #   'numbers', 
  #   help='調べたい数値を入力してください。',
  #   type=int,
  #   nargs=3
  #   )
  
  # args = parser.parse_args()
  # print(args.numbers)
  # parser = argparse.ArgumentParser()
  # parser.add_argument(
  #   'language',
  #   choices=['English', 'Japanese']
  # )
  # args = parser.parse_args()
  # print(args.language)
  
  parser = argparse.ArgumentParser()
  parser.add_argument('-t', '--text', default='xxx', nargs='*')
  args = parser.parse_args()
  print(args.text)