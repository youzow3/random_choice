import random
import argparse
    
def main(args: argparse.Namespace) -> int:
    with open(args.file, encoding = "utf-8") as f:
        lines: list[str] = list(map(lambda x: x.strip(), f.readlines()))
    if args.k > len(lines):
        print("Warning: k is bigger than number of lines.")
    chosen_lines: list = random.sample(lines, k = args.k)

    for i, line in enumerate(chosen_lines, 1):
        print(f"{i}. {line}")

if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("-k", default = 1, help = "Choice k items from given list [default = 1]", type = int)
    parser.add_argument("-f", "--file", default = "text.txt", help = "Input file [default = text.txt]", type = str)
    
    args: argparse.Namespace = parser.parse_args()

    exit(main(args))
