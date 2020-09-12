# Your code here
database = {}


def add_to_database(file):
    without_slash = file.split("/")
    last_part = without_slash[-1]
    if database.get(last_part) is None:
        database[last_part] = [file]
    else:
        database[last_part].append(file)


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    for f in files:
        add_to_database(f)

    for q in queries:
        if database.get(q) is not None:
            for x in database[q]:
                result.append(x)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
