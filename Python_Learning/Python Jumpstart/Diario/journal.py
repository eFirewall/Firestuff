"""This is the journal module."""
import os


def load(name):
    """Create and load a new journal.

    Args:
        variable (name):  This base name of the journal to load.

    Returns:
        data: A new journal data structure populated with the file data.

    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """Save the journal data."""
    filename = get_full_pathname(name)
    print("..... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    """Collect the path to the file."""
    filename = os.path.abspath(os.path.join('./journals/' + name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    """Add entry."""
    journal_data.append(text)
