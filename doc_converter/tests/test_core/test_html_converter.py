def test_html_conversion():
    input_data = "<html><body><h1>Hello World</h1></body></html>"
    expected_output = "Hello World"
    assert convert_html_to_text(input_data) == expected_output


def convert_html_to_text(html):
    from bs4 import BeautifulSoup

    return BeautifulSoup(html, "html.parser").get_text()
