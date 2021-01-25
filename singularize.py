from sys import argv
from pathlib import Path
from textblob import TextBlob
from stringcase import titlecase, snakecase
from json import dumps


def make_singular(pascal_str: str) -> str:
    terms = titlecase(pascal_str)
    blob = TextBlob(terms)
    singular_terms = [titlecase(part.singularize()) for part in blob.words]
    return ''.join(singular_terms)


def make_snake(pascal_str: str) -> str:
    return snakecase(pascal_str)


def make_singular_snake(pascal_str: str) -> str:
    return make_snake(make_singular(pascal_str))


if __name__ == "__main__":

    if len(argv) != 3:
        raise ValueError("Exactly two arguments (two text file paths) must be supplied.")

    input_file_path = Path(argv[1])
    output_file_path = Path(argv[2])

    if not input_file_path.exists():
        raise FileNotFoundError(f"File '{input_file_path.absolute()}' does not exist or unreachable.")

    with open(input_file_path, mode="rt") as f:
        lines = f.readlines()

    lines = [line.replace("\r", "").replace("\n", "") for line in lines]

    output_lines = list()

    for word in lines:
        output_lines.append(make_singular_snake(word))

    output_json = dumps(dict(zip(lines, output_lines)), indent=4)

    with open(output_file_path, mode="wt") as f:
        f.write(output_json)


