import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('target')
  args = parser.parse_args()
  print(args.target)