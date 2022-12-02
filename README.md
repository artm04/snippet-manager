# CLI snippet manager

This is a CLI app for managing code snippets which was created just for fun.
The app uses JSON files to store snippets.

## Requirements

* [Python 3.6+](https://www.python.org/downloads/)
* [pyperclip](https://pypi.org/project/pyperclip/)

## Installation

1. Clone the repository: `git clone github.com/artm04/snippet-manager`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the app: `python snipman.py -h`

## Usage

```
positional arguments:
  command               The command to run (add, delete, list, copy)

options:
  -h, --help            show this help message and exit
  --snippet_id [SNIPPET_ID]
                        The id of the snippet.
  --name [NAME]         The name of the snippet.
```

### Add a snippet

The `add` command adds a code snippet to the given file.
Specify the --name option.
To stop the input for your code, press `Ctrl+D` on Linux or `Ctrl+Z` on Windows.

```
$ python snipman.py add --name helloworld
Enter the code below:
print("Hello, World!")
<Ctrl+D>
```

### Delete a snippet

The `delete` command deletes a code snippet from the given file by its ID.
Specify the --snippet_id option.

```
$ python snipman.py delete --snippet_id 1
```

### Copy a snippet

The `copy` command copies a code snippet to the clipboard by its ID.
Specify the --snippet_id option.

```
$ python snipman.py copy --snippet_id 1
```

### List all snippets

The `list` command lists all snippets in the given file.

```
$ python snipman.py list
1: helloworld
2: hello
```

## Demo of the app on Asciinema

[![asciicast](https://asciinema.org/a/542104.svg)](https://asciinema.org/a/542104)