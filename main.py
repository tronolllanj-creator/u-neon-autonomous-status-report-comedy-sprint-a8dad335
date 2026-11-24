"""Entry point that writes the required activity log line to entry.txt."""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os

LINE = "Activity log: I did zero actual work this week, but I spent eighty hours making this status report look so visually stunning that you will never question it."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    content = LINE + "\n"

    if not (1 <= len(content) <= 200 and content.strip() and content.count("\n") == 1 and content.endswith("\n")):
        raise ValueError("Content validation failed")

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
