"""Write one fortune-cookie line to the make.fun output directory."""

import os

LINE = "Your code will outlive you. Comment accordingly — the stranger who inherits it may be future you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
