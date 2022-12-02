import json

import pyperclip

""" The classes and functions related to the functionality of the snippet manager. """


class Snippet:
    """ A snippet is a piece of code that can be copied to the clipboard. """

    def __init__(self, snippet_id: int, name: str, code: str):
        """
        Create a new snippet.
        :param snippet_id: ID of the snippet in the file.
        :param name: The snippet's title that you see when printing the snippet.
        :param code: Snippet's code. Can be copied to the clipboard and contains multiple lines.
        """
        self.snippet_id = snippet_id
        self.name = name
        self.code = code

    def __str__(self):
        return f'{self.snippet_id} - {self.name}'

    def to_dict(self):
        """ Return the snippet as a dictionary.
        :return: The snippet instance in a dictionary format.
        """
        return {
            'id': self.snippet_id,
            'name': self.name,
            'code': self.code
        }

    def copy(self):
        """ Copy the snippet's code to the clipboard. """
        pyperclip.copy(self.code)

    @classmethod
    def from_dict(cls, data: dict):
        """ Load a snippet from a dictionary.
        :param data: The dictionary containing the snippet's data in format {'id': int, 'name': str, 'code': str}
        :return: A Snippet object.
        """
        return cls(data['id'], data['name'], data['code'])


class SnippetList(list):
    """ A list of snippets. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sort(key=lambda s: s.snippet_id)

    def __str__(self):
        return '\n'.join([str(s) for s in self])

    def add(self, snippet: Snippet):
        """ Add a snippet to the list. """
        self.append(snippet)
        self.sort(key=lambda s: s.snippet_id)

    def delete(self, snippet_id: int):
        """ Delete a snippet from the list. """
        for snippet in self:
            if snippet.snippet_id == snippet_id:
                self.remove(snippet)
                return
        raise ValueError(f'Snippet with id {snippet_id} not found.')

    def save(self, file_path: str):
        """ Save the snippet list to a file.
        :param file_path: file path to save the snippet list to.
        """
        with open(file_path, 'w') as f:
            json.dump([s.to_dict() for s in self], f, indent=4)

    def get(self, snippet_id: int):
        """ Get a snippet from the list. """
        for snippet in self:
            if snippet.snippet_id == snippet_id:
                return snippet
        raise ValueError(f'Snippet with id {snippet_id} not found.')

    @classmethod
    def load(cls, file_path: str):
        """ Load a snippet list from a file.
        :param file_path: file path to load the snippet list from."""
        with open(file_path, 'r') as f:
            data = json.load(f)
        return cls([Snippet.from_dict(d) for d in data])
