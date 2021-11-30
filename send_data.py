import requests
import json

MAX_DATA_ROWS_OVER_PETITIONS = 75
URL = ''
AUTH_TOKEN = ''


def main(file_path=None):
    with open(file_path) as file:
        json_data = json.load(file)
        index = 0
        data_to_send = []
        for row in json_data:
            index = index + 1
            data_to_send.append(row)
            if index % MAX_DATA_ROWS_OVER_PETITIONS == 0:
                send_data(data_to_send)
                data_to_send = []
        print(f'Last Data {data_to_send}')
        send_data(data_to_send)


def send_data(data_to_send):
    body_to_send = {'events': data_to_send}
    r = requests.post(URL,
                      headers={"Content-Type": "application/json",
                               "Authorization": f'Bearer {AUTH_TOKEN}'},
                      json=body_to_send)
    print(f'Result {r.content}')


if __name__ == '__main__':
    main('booking_trip_finished_clean.txt')
