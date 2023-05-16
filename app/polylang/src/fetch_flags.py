
# import cairosvg
import requests


def main() -> None:
    """_summary_
    """

    URLs = {
        "england": "https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg",
        "spain": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Spain.svg",
        "france": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg",
        "germany": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Germany.svg",
        "china": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Flag_of_the_People%27s_Republic_of_China.svg",
    }

    url = URLs["england"]

    response = requests.get(url)

    # # Write the content of the response to a file
    with open('image.svg', 'wb') as file:
        file.write(response.content)

    # Convert SVG to PNG
    # cairosvg.svg2png(
    #     url=url,  # 'path/to/file.svg',
    #     write_to='test_img.png'
    #                  )


if __name__ == "__main__":
    main()
