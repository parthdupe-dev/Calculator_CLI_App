
def main():

    while True:

        # Step 1: Display menu
        print("\n========== PYTHON CALCULATOR ==========")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("Type EXIT to close calculator")
        print("=======================================")

        # Step 2: Get operation
        operation = input("Enter your choice: ").strip().upper()

        # Step 3: Exit condition
        if operation == "EXIT":
            print("Calculator closed. Goodbye!")
            break

        try:
            # Step 4: Get numbers
            input_1 = float(input("Enter the first number: "))
            input_2 = float(input("Enter the second number: "))

            # Step 5: Perform calculation
            if operation in ("1", "ADDITION", "+"):
                result = input_1 + input_2

            elif operation in ("2", "SUBTRACTION", "-"):
                result = input_1 - input_2

            elif operation in ("3", "MULTIPLICATION", "*"):
                result = input_1 * input_2

            elif operation in ("4", "DIVISION", "/"):
                if input_2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")

                result = input_1 / input_2

            else:
                print("Invalid operation selected!")
                continue

            # Step 6: Display result
            print("\nResult:", result)

        except ValueError:
            print("Error: Please enter valid numeric values.")

        except ZeroDivisionError as error:
            print("Calculation Error:", error)


if __name__ == "__main__":
    main()
