from urllib.parse import urlsplit
import validators


def process_url(url: str) -> str:

    is_valid_url = validators.url(url)
    if not is_valid_url:
        return url

    index = url.index("github.com")
    no_base_url = url[index + 11 :]
    parts = no_base_url.split("/")

    # check if we are dealing with a file
    if parts[2] == "blob":
        parts[-1] = remove_line_number(
            parts[-1]
        )  # check line number (e.g., run.go#L151-L163)
        return "/".join(parts[4:])  # concate the full file path back together

    # if the url is a branch
    elif parts[2] == "tree":
        return "/".join(parts[3:])

    # if the url is an issue
    elif parts[2] == "issues":
        return "#" + parts[-1]

    raise Exception(f'Not an expected url: {url}' )

def remove_line_number(filename_with_line_number: str) -> str:
    return filename_with_line_number.split("#")[0]
