import random
import argparse

def generate(length, seed, width):
    rng = random.Random(seed)

    lines = []

    max_width = length * width

    for i in range(length):
        depth = i / length

        inner_width = int((1 - depth) * max_width)

        if inner_width < 1:
            inner_width = 1
        
        left_pad = " " * (i // 2)

        wall_left = "|"
        wall_right = "\\" if rng.random() < 0.05 else "/"
        
        middle = " " * inner_width if inner_width >= 2 else ""
        
        line = left_pad + wall_left + middle + wall_right
        lines.append(line)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=20)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--width", type=int, default=2)
    args = parser.parse_args()

    print(generate(args.length, args.seed, args.width))


if __name__ == "__main__":
    main()