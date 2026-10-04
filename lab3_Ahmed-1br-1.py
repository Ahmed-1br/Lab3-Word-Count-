"""
Program Name: Word Count
Author: Ahmed Ibrahim
Purpose: Analyze a selected text file and count the frequency of each word.
Starter code: None
Date: October 4, 2026
"""

from pathlib import Path
import string


class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.frequencies = {}

    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            with self.__filepath.open("r") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans("", "", string.punctuation))
                    words = line.split()

                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True
        except FileNotFoundError:
            print("Error: The selected file couuld not be found.")
            return False

    def print_report(self):
        words = sorted(self.__frequencies.keys())

        for word in words:
            print(f"{word} :: {self.__frequencies[word]}")


def main():
    print("\nWord Count Analyzer")
    print("1. A princess of Mars")
    print("2. Tarzan")
    print("3. Treasure Island")
    print("4. The Count of Monte Cristo")

    choice = input("Select a book (1-4): ")
    if choice == "1":
        filepath = ("princess_mars.txt")
    elif choice == "2":
        filepath = ("Tarzan.txt")
    elif choice == "3":
        filepath = ("treasure_island.txt")
    elif choice == "4":
        filepath = ("monte_cristo.txt")
    else:
        print("Invalid choice. Please select a number from 1-4.")
        return

    analyzer = WordAnalyzer(filepath)

    if analyzer.process_file():
        analyzer.print_report()

if __name__ == "__main__":
    main()

  