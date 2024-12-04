def create_txt_files(n):
    for i in range(1, n + 1):
        with open(f"{i}.txt", "w") as file:
            file.write(f"This is file {i}")

# Example usage
n = 30  # Replace with any number you want
create_txt_files(n)
