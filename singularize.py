from sys import argv
from pathlib import Path
from textblob import TextBlob
from stringcase import titlecase, snakecase
from json import dumps


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

    # for each line in lines:
    # 1. split into separate words (Title Case)
    # 2. Make each word singular
    # 3. Recombine into a string
    # 4. snake case the string
    # 5. add to a list
    # 6. merge input and output lists into a json object map
    # 7. save json to output file path

    output_lines = list()

    for word in lines:
        title_parts = titlecase(word)
        blob = TextBlob(title_parts)
        singular_words = [titlecase(part.singularize()) for part in blob.words]
        output_lines.append(snakecase(''.join(singular_words)))

    output_json = dumps(dict(zip(lines, output_lines)), indent=4)

    with open(output_file_path, mode="wt") as f:
        f.write(output_json)


