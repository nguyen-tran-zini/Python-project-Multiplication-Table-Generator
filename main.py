# Project: Multiplication Table Generator
# Goal: Generate multiplication tables from 1 to 9 and save them to a file.

# Function to generate multiplication tables and save them to a file.
def generate_multiplication_tables(file_name="multiplication_table.txt"):
    try:
        with open(file_name, "w") as file:
            for i in range(1, 10):
                file.write(f"Multiplication Table {i}:\n")
                for j in range(1, 10):
                    file.write(f"{i} x {j} = {i * j}\n")
                file.write("\n")
        print(f"Multiplication tables successfully written to '{file_name}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
generate_multiplication_tables()
