"""
   Lab 8 UPC Code Validation
  Sammy Saqfelhait 
  This program checks if a 12-digit UPC code is valid.
   03/04/2026"""

def find_UPC(first11: str) -> int:

    odd_sum = 0
    even_sum = 0

    for i in range(len(first11)):
        num = int(first11[i])

        if i % 2 == 0:
            odd_sum += num
        else:
            even_sum += num

    total = (odd_sum * 3) + even_sum
    check_digit = (10 - (total % 10)) % 10

    return check_digit


def main():
    upc = input("Enter a 12-digit UPC: ")

    first11 = upc[:11]
    provided_digit = int(upc[11])

    print()
    print(f"The first 11 digits are '{first11}'.")
    print(f"The provided check digit is '{provided_digit}'.")
    print()
    print("Calculating...")

    expected_digit = find_UPC(first11)

    print(f"The expected check digit is {expected_digit}.")
    print()

    if expected_digit == provided_digit:
        print("This is a VALID UPC.")
    else:
        print("This is an INVALID UPC.")


if __name__ == "__main__":
    main()