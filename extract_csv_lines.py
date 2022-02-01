import csv


def main(input_file_name: str, output_file_name: str, from_line: int, to_line: int):
    with open(input_file_name, encoding='utf-8-sig') as read_file:
        read_csv_file = csv.reader(read_file)
        line_count = 0
        rows_to_write = []
        for row in read_csv_file:
            print(line_count)
            if line_count == 0 or from_line <= line_count + 1 <= to_line:
                print(row)
                rows_to_write.append(row)
            line_count += 1

    with open(output_file_name, 'w', newline='', encoding='utf-8-sig') as write_file:
        write_csv_file = csv.writer(write_file)
        print(rows_to_write)
        write_csv_file.writerows(rows_to_write)


if __name__ == '__main__':
    from_line = 22500
    to_line = 35000
    main(f'example.csv', f'Example from {from_line} to {to_line}.csv', from_line, to_line)
