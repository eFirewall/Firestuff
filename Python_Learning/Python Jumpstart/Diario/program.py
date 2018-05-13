
def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------------')
    print('         JOURNAL APP')
    print('-------------------------------')
    print('')


def run_event_loop():

    print('What do you wanna do with your journal?')
    cmd = None
    journal_data = []  # list()

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry, we cannot understand '{}'.".format(cmd))

    print('That will be all. Good bye!')


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("* [{}] {}".format(idx + 1, entry))


def add_entry(data):
    text = input('Type your enry, <enter>, to exit: ')
    data.append(text)


main()
