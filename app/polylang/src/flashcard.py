"""_summary_
"""

import yaml

lang_files = [
    "abbreviations",
    "acronyms",
    "common_phrases",
    "vocabulary",
]

lang_options = [
    "english",
    # "french",
    "german",
    # "spanish",
    # "mandarin",
               ]

lang_choice = lang_options[1]

lang_file = f"app/polylang/assets/{lang_choice}/processed/{lang_files[-1]}.yml"

with open(lang_file, "r") as rf:
    data = yaml.load(rf, Loader=yaml.SafeLoader)

flashcards = {}

for k, v in data.items():
    if lang_choice == "english":
        # print(k)
        if "definition" in v:
            # print(v["definition"])
            flashcards[k] = v["definition"]
        else:
            # print(v["definition_1"])
            flashcards[k] = v["definition_1"]
    else:
        flashcards[k] = v["eng_translation"]
