import csv

def main():
    champions = {}
    countries = set()

    with open("wimbledon.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            champion = row[2]
            country = row[1]
            champions[champion] = champions.get(champion, 0) + 1
            countries.add(country)
    
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion:20} {wins}")
    
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()
