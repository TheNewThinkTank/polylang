"""_summary_

examples:
python3 app/polylang/src/file_processor.py -l english
python3 app/polylang/src/file_processor.py -l spanish
"""

import argparse
from pprint import pprint as pp

import yaml  # type: ignore

# TODO: yaml key and values of "No" and "Yes" becomes bool.
# Add string casting to fix (example: spanish/raw/vocabulary.yml)

# TODO: handle single and double quotes
# TODO: add pipe (|) before multiline strings
# TODO: strip final dot from word definition and from word example


def sort_lang_file(lang_file: str):
    """Load language yaml file, sort content alphabetically, and strip newlines.

    :param lang_file: _description_
    :type lang_file: str
    :return: _description_
    :rtype:
    """

    with open(lang_file, "r", encoding="utf-8") as rf:
        data = yaml.load(rf, Loader=yaml.SafeLoader)

    pp(data)

    sorted_data = dict(sorted(data.items()))

    for k, v in sorted_data.items():
        # print(k)
        # print(v.get("part-of-speech", "part-of-speech missing!"))
        for kk, vv in v.items():
            print(kk)
            print(vv)
            # print(vv, type(vv))

            # sorted_data[k][kk] = ''.join(vv.splitlines())
            ## vv.strip("\n")  # vv.removesuffix("\n")

    # "part-of-speech"
    # "definition"
    # "example"

    # sorted_data =  {k.lower(): v for k, v in sorted_data.items()}

    return  # sorted_data


def write_sorted_to_file(lang_file: str, sorted_data: dict, out_file: str) -> None:
    """_summary_

    :param lang_file: _description_
    :type lang_file: str
    :param sorted_data: _description_
    :type sorted_data: dict
    :param out_file: _description_
    :type out_file: str
    """

    # from pprint import pprint as pp
    # pp(sorted_data)

    # with open(lang_file, 'r') as rf, open(out_file, 'wt') as wf:
    #     for line in rf:
    #         if line.strip():
    #             wf.write(line)

    with open(out_file,
            mode="wt",
            encoding="utf-8") as wf:
        yaml.safe_dump(
            sorted_data,
            wf,
            explicit_start=True,
            # default_style='\"',
                    )


def main() -> None:
    """_summary_
    """

    lang_files = [
        "abbreviations",
        "acronyms",
        "common_phrases",
        "vocabulary",
    ]

    # lang_options = [
    #     "english",
    #     "french",
    #     "german",
    #     "spanish",
    #     "mandarin",
    #             ]

    # lang_choice = lang_options[1]
    parser = argparse.ArgumentParser(description='Language Learning Program')
    parser.add_argument('-l', '--language', type=str,
                        help="""
                                Specify the language for practice
                                (english / german / spanish)
                        """
                        )
    args = parser.parse_args()
    lang_choice = args.language

    lang_file = f"app/polylang/assets/{lang_choice}/raw/{lang_files[-1]}.yml"
    # print(f"{lang_file = }")

    sorted_data = sort_lang_file(lang_file)
    pp(sorted_data)
    # parts = lang_file.split('/')
    # out_file = "/".join(parts[:4]) + "/processed/" + parts[-1]
    # write_sorted_to_file(lang_file, sorted_data, out_file)


if __name__ == "__main__":
    main()
