import csv

class CsvLoader:

    def load_csv(self, filename):
        data = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # skip the headers
            for row in reader:
                data.append(row)
        return data