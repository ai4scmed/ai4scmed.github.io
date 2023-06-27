import argparse
import warnings
import os
import bibtexparser
import unicodedata

parser = argparse.ArgumentParser()
parser.add_argument(
    "filename",
    help="Path to file containing bibtex formatted references")
parser.add_argument(
    "output_dir",
    help="Path to the output directory")
parser.add_argument(
    "--filter-author", "-f", default=None,
    help="Filter for author, e.g., 'Junier, Ivan'")
args = parser.parse_args()

filename = args.filename
output_dir = args.output_dir
filter_author = args.filter_author


with open(filename) as bibtex_file:
    bib_database = bibtexparser.bparser.BibTexParser(
        common_strings=True).parse_file(bibtex_file)


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode()


def get_authors(citation, format="only_last_name"):
    authors = citation["author"].replace("\n", " ").split(" and ")
    authors = [a.strip().split(", ") for a in authors]

    if format == "only_last_name":
        authors = [a[0] for a in authors]
    elif format == "abbrvnat":
        authors = [create_initials(a) for a in authors]
        authors = [" ".join([a[1], a[0]]) for a in authors]
    else:
        raise ValueError(
            "Unknown format. Please specify one of ['only_last_name']")
    return authors


def create_initials(author):
    # Start by splitting first names
    if len(author) == 1:
        return [author[0].replace("{", "").replace("}", ""), ""]
    first_names = author[1].split(" ")
    # Then initialize by dealing with hyphenated names
    initialized_first_name = []
    for first_name in first_names:
        initialized_first_name.append(
            "-".join([s[0].strip() + "." for s in first_name.split("-") if len(s)]))
    initialized_first_name = " ".join(initialized_first_name)
    author[1] = initialized_first_name
    return author


def create_filename(citation):
    authors = get_authors(citation)[:4]
    # Ok… Let's just remove anything non alphanumerical which is a bit
    # annoying for people with special characters in their name but will save
    # us some trouble later on.
    authors = [remove_accents(a) for a in authors]
    try:
        month = citation["month"]
    except KeyError:
        warning = (
            "Citation '%s' is missing information about month" %
            citation["title"])
        warnings.warn(warning)
        month = "none"
        pass

    filename = (
        citation["year"] +
        convert_month(month) + "-" + "_".join(authors) + ".md")
    return filename


def convert_month(month):
    months = {
        "none": "00",
        "jan": "01",
        "1": "01",
        "january": "01",
        "feb": "02",
        "february": "02",
        "2": "02",
        "mar": "03",
        "march": "03",
        "3": "03",
        "apr": "04",
        "april": "04",
        "4": "04",
        "may": "05",
        "5": "05",
        "jun": "06",
        "june": "06",
        "6": "06",
        "jul": "07",
        "july": "07",
        "7": "07",
        "aug": "08",
        "august": "08",
        "8": "08",
        "sep": "09",
        "september": "09",
        "9": "09",
        "oct": "10",
        "october": "10",
        "10": "10",
        "nov": "11",
        "november": "11",
        "11": "11",
        "dec": "12",
        "december": "12",
        "december": "12",
        "12": "12",
        }
    return months[month.lower()]


def format_citation(citation, max_authors=4):
    authors = get_authors(citation, format="abbrvnat")
    et_al = ""
    if len(authors) > 4:
        authors = authors[:4]
        et_al = " <i>et al.</i>"
    authors = ", ".join(authors) + et_al
    title = citation["title"].replace("{", "").replace("}", "")
    try:
        journal = citation["journal"] + ","
    except KeyError:
        journal = ""

    try:
        month = citation["month"].capitalize() + " "
    except KeyError:
        month = ""

    try:
        year = citation["year"]
    except KeyError:
        year = ""

    formatted_citation = (
        "{authors}. <b>{title}</b>, <i>{journal}</i>"
        " {month}{year}").format(
            authors=authors,
            title=title,
            journal=journal,
            month=month,
            year=year)
    return formatted_citation


try:
    os.makedirs(output_dir)
except OSError:
    pass

for citation in bib_database.entries:
    # Filter based on author if necessary
    if filter_author is not None:
        if filter_author not in citation["author"]:
            print("Ignoring '%s', '%s'" % (
                citation["title"], citation["author"]))
            continue

    # Clean up title name

    citation["title"] = citation["title"].replace("{", "").replace("}", "")
    try:
        note = citation["note"]
        note = note.replace(r"\_", "_")
        note = note + "\n"
    except KeyError:
        note = ""

    try:
        url = "paperurl: '" + citation["url"] + "'\n"
    except KeyError:
        url = ""

    # create the filename
    filename = create_filename(citation).lower()
    formatted_citation = format_citation(citation)
    print(filename)
    md = "---\n"
    md = md + "title: " + '"' + citation["title"] + '"' + "\n"
    md = md + "collection: publications\n"
    md = md + "permalink: /publication/" + filename.split(".md")[0].lower() + "\n"
    md = md + "venue: ''\n"
    md = md + "citation: '" + formatted_citation + "'\n"
    md = md + "year: '" + citation["year"] + "'\n"
    md = md + note + url
    md = md + "---\n"

    with open(os.path.join(output_dir, filename), "w") as f:
        f.write(md)
    print("")
