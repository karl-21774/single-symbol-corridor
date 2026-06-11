import random
import argparse

def generate(length, seed):
    rng = random.Random(seed)

    lines = []

    for i in range(length):
        left = "|"
        spaces = " " * i

        # right wall 'leans' inward
        # occaisional jitter for imperfection
        if rng.random() < 0.1:
            right ="/"
        else:
            right = "\\"
        
        lines.append(left + spaces + right)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=20)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()

    print(generate(args.length, args.seed))


if __name__ == "__main__":
    main()