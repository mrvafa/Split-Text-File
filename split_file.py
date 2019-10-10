import argparse
import codecs
import datetime
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', help='File name', required=True)
    parser.add_argument('-s', '--size', help='Size of sub files in MB (spited files size)', required=True)
    parser.add_argument('-f', '--filter', help='Filter to only make files with certain index \nUse <,> to separate '
                                               'values (e.g. --filter 1,2,3)')
    time = str(datetime.datetime.now()).replace(' ', '_').replace('-', '_').replace(':', '_').replace('.', '_')

    args = parser.parse_args()

    # filter list
    has_filter = False
    filter_list = args.filter

    if filter_list is not None:
        try:
            filter_list = [int(x) for x in filter_list.split(',')]
        except ValueError as e:
            print(str(e))
            exit(-1)

        has_filter = True
        max_item = max(filter_list)

    filename = args.name = args.name

    # get file suffix
    suffix = '.' + filename.split('.')[filename.count('.')]

    # split size in Megabit int(args.size)
    try:
        split_size = int(args.size)
    except ValueError as e:
        print(e)
        exit(-1)

    # path file
    file_path = os.path.abspath(filename)

    if not os.path.isfile(file_path):
        print('Error: File not found')
        exit(-1)

    # counter for splits files
    counter = 1

    sub_file_size = 0

    sub_file_name = filename.split('.')[0] + '_' + time + '_' + str(counter) + suffix
    sub_file = codecs.open(sub_file_name, "w", "utf-8")
    sub_file_path = os.path.abspath(sub_file_name)

    with open(filename) as file:
        for line in file:
            if sub_file_size < split_size * 1_000_000:
                sub_file.write(line)
                sub_file_size = os.path.getsize(sub_file_path)

            else:
                sub_file_size = 0
                sub_file.write(line)
                sub_file.close()

                if has_filter and counter not in filter_list:
                    os.remove(sub_file_path)

                if has_filter and counter > max_item:
                    exit(0)

                counter += 1
                sub_file_name = filename.split('.')[0] + '_' + time + '_' + str(counter) + suffix
                sub_file = codecs.open(sub_file_name, "w", "utf-8")
                sub_file_path = os.path.abspath(sub_file_name)
                sub_file_size = os.path.getsize(sub_file_path)

        if has_filter and counter not in filter_list:
            sub_file.close()
            os.remove(sub_file_path)

    file.close()
