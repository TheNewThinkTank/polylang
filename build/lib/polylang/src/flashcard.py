"""_summary_
"""

import yaml  # type: ignore

lang_files = [
    "abbreviations",
    "acronyms",
    "common_phrases",
    "vocabulary",
]

lang_file = f"assets/english/processed/{lang_files[-1]}.yml"

with open(lang_file, "r") as rf:
    data = yaml.load(rf, Loader=yaml.SafeLoader)

flashcards = {}
for k, v in data.items():
    # print(k)
    if "definition" in v:
        # print(v["definition"])
        flashcards[k] = v["definition"]
    else:
        # print(v["definition_1"])
        flashcards[k] = v["definition_1"]
