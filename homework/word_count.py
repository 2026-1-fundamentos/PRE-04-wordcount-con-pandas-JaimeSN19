"""Taller evaluable"""

import os
import re
from collections import Counter


def run_job(input_directory, output_directory):
    """Word count job"""

    os.makedirs(output_directory, exist_ok=True)

    word_counter = Counter()

    for filename in os.listdir(input_directory):

        filepath = os.path.join(input_directory, filename)

        if os.path.isfile(filepath):

            with open(filepath, "r", encoding="utf-8") as file:

                for line in file:

                    # Convertir a minúsculas y limpiar puntuación
                    words = re.findall(r"\b[a-zA-Z]+\b", line.lower())

                    word_counter.update(words)

    output_file = os.path.join(output_directory, "part-00000")

    with open(output_file, "w", encoding="utf-8") as file:

        for word in sorted(word_counter):

            file.write(f"{word}\t{word_counter[word]}\n")

    with open(os.path.join(output_directory, "_SUCCESS"), "w"):
        pass


if __name__ == "__main__":

    run_job(
        "files/input",
        "files/output",
    )