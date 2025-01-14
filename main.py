# Project: Multiplication Table Generator
# Goal: Generate multiplication tables from 1 to 9 and print them to the console.

# Function to generate and print multiplication tables.
def generate_multiplication_tables():
    try:
        for i in range(1, 10):
            print(f"Multiplication Table {i}:")
            for j in range(1, 10):
                print(f"{i} x {j} = {i * j}")
            print()
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
generate_multiplication_tables()

# Run the project by clicking on the following link: https://pythonid.com/user/nguyentran/projects/python-project-multiplication-table-generator
