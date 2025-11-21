import csv
from datetime import date

FILE = "mood_journal.csv"

def add_entry():
    mood = input("How are you feeling today (1-5)? ")
    note = input("What's on your mind? ")
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date.today(), mood, note])
    print("Entry added!\n")

def view_entries():
    try:
        with open(FILE, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                print(f"{row[0]} | Mood {row[1]} | {row[2]}")
    except FileNotFoundError:
        print("No entries yet.\n")

def average_mood():
    moods = []
    try:
        with open(FILE, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                moods.append(int(row[1]))
        if moods:
            print(f"Average Mood: {sum(moods)/len(moods):.2f}\n")
        else:
            print("No moods recorded.\n")
    except FileNotFoundError:
        print("No data yet.\n")

def main():
    print("=== Mood Journal ===")
    while True:
        print("1) Add entry\n2) View entries\n3) Average mood\n4) Quit")
        choice = input("Choose: ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            average_mood()
        elif choice == "4":
            break
        else:
            print("Invalid option\n")

if __name__ == "__main__":
    main()
