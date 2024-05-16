from format_html import build_page
from api_birds import get_birds


if __name__ == "__main__":

    with open("index.html", "w") as file:

        file.write(build_page(get_birds()))

