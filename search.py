import json
from utils import resource_path
def search_word(word, direction):

    # Load the latest dictionary every time
    with open(resource_path("dictionary.json"), "r") as file:
        dictionary = json.load(file)

    word = word.strip().title()

    if direction == "Manipuri → English":
        return dictionary.get(word, "Word not found")

    else:
        for key, value in dictionary.items():
            if value.lower() == word.lower():
                return key

        return "Word not found"
