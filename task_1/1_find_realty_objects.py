def find_realty_objects(csv_db):
    with open('frequently_sold.csv', 'w') as answer:
        with open(csv_db, 'r') as database:
            hash_dict = {}

            for line in database:
                cols = line.strip().split(',')
                # похоже, что с 8 по 13 столбец идет адрес объекта, по нему можно сделать ключ для словаря
                items = [cols[i] for i in range(7, 13)]
                address = ", ".join(items).replace('"', '') + "\n"

                if address not in hash_dict:
                    hash_dict[address] = 1
                elif hash_dict[address] == 1:
                    hash_dict[address] += 1
                    answer.write(address)
                else:
                    continue


if __name__ == "__main__":
    find_realty_objects('pp-complete.csv')
