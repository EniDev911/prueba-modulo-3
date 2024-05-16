from api_birds import get_birds

def build_page(birds):
    html = "<html>"
    html += "<body style='text-align: center'>"
    html += "<ul>"
    for bird in birds:
        html += "<li style='display: inline-block; margin: 30px 20px; border: 1px solid #ff5'>"
        html += f"<img style='border-radius: 50%' src='{bird['images']['thumb']}' alt='{bird['name']['spanish']}' height='150' width='150' />\n"
        html += "<br>"
        html += f"<span><strong>Nombre español: {bird['name']['spanish']}</strong></span>"
        html +="<br>"
        html += f"<span><strong>Nombre inglés: {bird['name']['english']}</strong></span>"
        html += "</li>"

    html += "</ul>"
    html += "</body>"
    html += "</html>"
    return html

if __name__ == "__main__":
    birds = get_birds()
    print(build_page(birds))
