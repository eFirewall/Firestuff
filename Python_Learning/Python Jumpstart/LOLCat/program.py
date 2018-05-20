"""LOLcat Factory."""
import os


def main():
    """Orchestrate the main program."""
    print_the_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    # TODO Download Cats
    # TODO Display cats
    # print('hello from main')


def print_the_header():
    """Print the welcome screen."""
    print('-----------------------------------')
    print('       LOLCat Factory V1.0')
    print('-----------------------------------')
    print()


def get_or_create_output_folder():
    """Create directory or use in case it already exists."""
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os. path.join(base_folder, folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}...'.format(full_path))
        os.mkdir(full_path)
    return full_path


if __name__ == '__main__':
    main()
