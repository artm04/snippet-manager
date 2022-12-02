"""The main module of the CLI snippet manager."""
import argparse
import os
import sys

from utils import Snippet, SnippetList

file = 'snippets.json'


def main():
    if not os.path.exists(file):
        print(f'File {file} not found. Creating new file.')
        snippets = SnippetList()
        snippets.save(file)
    else:
        snippets = SnippetList.load(file)

    """Commands:
    - add: add a new snippet
    - delete: delete a snippet
    - list: list all snippets
    - copy: copy a snippet to the clipboard"""

    parser = argparse.ArgumentParser(description='Manage your snippets.')
    parser.add_argument('command', help='The command to run (add, delete, list, copy)')
    parser.add_argument('--snippet_id', nargs='?', type=int, help='The id of the snippet.')
    parser.add_argument('--name', nargs='?', help='The name of the snippet.')
    args = parser.parse_args()

    if args.command == 'add':
        if args.name:
            snippet_id = len(snippets)
            snippet_name = args.name
            """Enter a code until EOF."""
            print('Enter a code. Press Ctrl+D orCtrl+Z to finish.')
            snippet_code = sys.stdin.read()
            snippet = Snippet(snippet_id, snippet_name, snippet_code)
            snippets.add(snippet)
            snippets.save(file)
            print(f'Snippet {snippet_name} added.')
        else:
            print('Please provide a name and code for the snippet.')
    elif args.command == 'delete':
        if args.snippet_id is not None:
            snippets.delete(args.snippet_id)
            snippets.save(file)
        else:
            print('Please provide a snippet id.')
    elif args.command == 'list':
        print('Snippets:', snippets, sep='\n')

    elif args.command == 'copy':
        if args.snippet_id is not None:
            snippet = snippets.get(args.snippet_id)
            print("You're copying the following snippet:")
            print(snippet, '\n', snippet.code)
            confirm = input('Are you sure? (y/n) ')
            if confirm == 'y':
                snippet.copy()
                print('Snippet copied to clipboard.')
        else:
            print('Please provide a snippet id.')
    else:
        print('Invalid command.')


if __name__ == '__main__':
    main()
