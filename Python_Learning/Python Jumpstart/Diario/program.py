"""Program module."""
import journal

def main():
    """Main function to call them all."""
    print_header()
    run_event_loop()


def print_header():
    """Print the header."""
    print('-------------------------------')
    print('         JOURNAL APP')
    print('-------------------------------')
    print('')


def run_event_loop():
    """Event looper."""
    print('What do you wanna do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)  # []  # list()

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorr y, we cannot understand '{}'.".format(cmd))

    print('That will be all. Good bye!')
    journal.save(journal_name, journal_data)


def list_entries(data):
    """List entries."""
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("* [{}] {}".format(idx + 1, entry))


def add_entry(data):
    """Add entry."""
    text = input('Type your enry, <enter>, to exit: ')
    journal.add_entry(text, data)
    # data.append(text)


if __name__ == '__main__':
    main()
