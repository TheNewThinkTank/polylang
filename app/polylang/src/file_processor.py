"""_summary_
"""

from pprint import pprint as pp
import yaml

# TODO: handle single and double quotes
# TODO: add pipe (|) before multiline strings
# TODO: strip final dot from word definition and from word example


def sort_lang_file(lang_file: str) -> dict:
    """Load language yaml file, sort content alphabetically, and strip newlines.

    :param lang_file: _description_
    :type lang_file: str
    :return: _description_
    :rtype: dict
    """

    with open(lang_file, "r", encoding="utf-8") as rf:
        data = yaml.load(rf, Loader=yaml.SafeLoader)

    sorted_data = dict(sorted(data.items()))

    for k, v in sorted_data.items():
        # print(k)
        # print(v.get("part-of-speech", "part-of-speech missing!"))
        for kk, vv in v.items():
            # print(kk)
            # print(vv, type(vv))

            sorted_data[k][kk] = ''.join(vv.splitlines())  # vv.strip("\n")  # vv.removesuffix("\n")

    # "part-of-speech"
    # "definition"
    # "example"

    return sorted_data


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

    lang_options = [
        "english",
        # "french",
        "german",
        # "spanish",
        # "mandarin",
                ]

    lang_choice = lang_options[1]

    lang_file = f"app/polylang/assets/{lang_choice}/raw/{lang_files[-1]}.yml"

    sorted_data = sort_lang_file(lang_file)
    # pp(sorted_data)

    parts = lang_file.split('/')

    out_file = parts[0] + "/" + parts[1] + "/" + parts[2] + "/" + parts[3] + "/processed/" + parts[-1]


    write_sorted_to_file(lang_file, sorted_data, out_file)


if __name__ == "__main__":
    main()
