def main():
   
    numbers = [2, 3, 3, 4, 5, 5, 6]

    from mean import mean
    from median import median
    from mode import mode

    # Calculate and print mean, median, and mode by importing the functions
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

if __name__ == "__main__":
    main()