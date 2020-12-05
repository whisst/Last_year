import csv
import requests

with open(r'..\UI_demo_II\Tuoitre.csv', newline='', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            url = row[len(row)-1]
            r = requests.get(url)

            with open(r'..\Images\tuoitre'+str(line_count)+'.jpg', 'wb') as f:
                f.write(r.content)
        line_count += 1