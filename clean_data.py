OUTPUT_FILE_NAME = 'booking_trip_finished_clean.txt'


def main(file_path=None):
    with open(file_path) as file:
        clean_data = file.read().replace('"{"', "{").replace('"}"', "}").replace('""', '"').replace('\n', ',')
        clean_data = clean_data[:-1]
    with open(OUTPUT_FILE_NAME, 'x') as write_file:
        write_file.write("[")
        write_file.write(clean_data)
        write_file.write("]")


if __name__ == '__main__':
    main('booking_trip_finished.csv')
