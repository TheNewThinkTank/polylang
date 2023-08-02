"""_summary_
"""

import argparse
# import os

import yaml

lang_files = [
    "abbreviations",
    "acronyms",
    "common_phrases",
    "vocabulary",
]

# lang_options = [
#     "english",
#     # "french",
#     "german",
#     # "spanish",
#     # "mandarin",
#                ]

# lang_choice = lang_options[1]

parser = argparse.ArgumentParser(description='Language Learning Program')
parser.add_argument('-l',
                    '--language',
                    type=str,
                    help='Specify the language for practice (english / german)'
                    )
args = parser.parse_args()
lang_choice = args.language

# lang_choice = os.environ["lang_choice"]
## or: input("Specify the language for practice (english/french)")

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
