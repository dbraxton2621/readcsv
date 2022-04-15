import csv

def main():
    print ("Find out players who were drafted by each year and round.")

    draft_year = input("What draft year would you like to search between 1936 and 2013?")
    draft_round = input("What draft round would you like to pick between 1 and 7?")

    csv_file = csv.reader(open('nflplayers.csv', 'r'))

    for row in csv_file:
        if (draft_year in row[11]) & (draft_round in row[9]):
            print(f'{row[0]} went to {row[7]}, was the {row[10]} draft pick and played {row[12]}.')
if __name__ == '__main__':
    main()




