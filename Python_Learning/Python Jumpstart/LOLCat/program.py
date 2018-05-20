"""LOLcat Factory."""
import os
import cat_service
import subprocess
import platform


def main():
    """Orchestrate the main program."""
    print_the_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    download_cats(folder)
    display_cats(folder)


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
    full_path = os.path.join(base_folder, folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}...'.format(full_path))
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    """Download the cats."""
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat {}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)
    print('Done')


def display_cats(folder):
    """Display the cats."""
    # open folder
    print('Displaying cats in OS window.')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your OS: " + platform.system())


if __name__ == '__main__':
    main()
