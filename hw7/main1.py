import os, shelve, csv


def edit_db():
    while True:
        with shelve.open('nums') as db:
            mode = input(
                'Add(add or replace), delete phone numbers, all clear, or exit the application?: (a, d, c, e) ')
            if mode == 'a':
                pattern = 'Enter [firstname, lastname, job, etc...] and number: (Example - Artem, ' \
                          'Ismagilov, Developer, etc... - +79999186903, +71234567890, ...)'
                while True:
                    user_text = input(pattern)
                    try:
                        info, numbers = user_text.split(' - ')
                    except ValueError:
                        print(f'Incorrect input text ` {user_text} `!!!')
                    else:
                        print(f'[{info} - {numbers}] is added')
                        db[info] = numbers
                        return
            elif mode == 'd':
                pattern = 'Enter the information you want to delete [firstname, lastname, job, etc...]'
                info = input(pattern)
                try:
                    print(f'[{info} - {db[info]}] is deleted')
                    del db[info]
                    return
                except KeyError:
                    print(f'There is no such person: [{info}] in the phone book')
            elif mode == 'c':
                print(f'Clear all numbers. Your dictionary-numbers is empty. ')
                db.clear()
                return
            elif mode == 'e':
                print('Bye-Bye)')
                quit()
            else:
                print(f'Incorrect mode: {mode}. Try enter a, d, c, e.')


def run():
    while True:
        with shelve.open('nums') as db:
            d = input('Choose to export, import or edit the phone book? : (export, import, edit)')
            if d == 'export':
                namefile = input('enter filename: ')
                f = input('export in .csv or .txt format ? (csv, txt)')

                if f == 'txt':
                    with open(namefile + '.txt', 'w') as file:
                        get_text = '\n'.join('%s - %s' % (k, db[k]) for k in db)
                        file.write(get_text)
                    print(f'The file is available on the path: {os.path.abspath(namefile + ".txt")}')
                    break
                elif f == 'csv':
                    with open(namefile + '.csv', 'w') as csv_f:
                        writer = csv.writer(csv_f)
                        for k in db:
                            print(f'+ {k} - {db[k]}')
                            writer.writerow([k, db[k]])
                        print(f'The file is available on the path: {os.path.abspath(namefile + ".csv")}')
                        break
                else:
                    print('Incorrect format file. Enter txt or csv')
            elif d == 'import':
                namefile = input('enter filename and extension: ')
                if namefile.endswith('.txt'):
                    with open(namefile) as txt_f:
                        for i in txt_f.read():
                            info, phones = i.split('; ')
                            db[info] = [phones]
                elif namefile.endswith('.csv'):
                    with open(namefile) as csv_file:
                        reader = csv.reader(csv_file)
                        for row in reader:
                            if row and all(row):
                                i, n = row
                                db[i] = n
                    print(f'The imported file {namefile} changed the phone book. ')
            elif d == 'edit':
                edit_db()
            else:
                print(f'Incorrect input text: {d}. Try enter import or export')


print('Hello, Welcome to the application - phone book.')
run()
