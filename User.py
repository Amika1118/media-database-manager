import file_handeling as fh
Content = {}

def lines(number):
    for i in range(number):
        print("-", end="")
    print()



def search_content_by_name(content_title):
    fh.reader(Content, "comments.csv")

    for id,data in Content.items():
        content_id = id
        title = data[0]
        comment = data[1]

        if id[0] == "m":
            type = "movie"
        elif id[0] == "t":
            type  = "tv-show"
        else:
            type = "anime"

        if content_title.lower() == title.lower():
            print(f"Name of the {type.capitalize()} is {title.capitalize()}.")
            print(f"Comments ----->")
            lines(20)
            print(f"{comment}")

search_content_by_name("Before We Go")
