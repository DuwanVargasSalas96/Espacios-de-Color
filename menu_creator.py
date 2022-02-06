# Create table
def table(title, rows):
    # Create
    margins = "---------------------------------------------------"

    # Print header
    print("\n" + margins + "\n" + row(title) + "\n" + margins)

    # Print rows
    for item in rows:
        print(row(item))
    
    # Print bottom margin
    print(margins + "\n")


# Create header
def header(title):
    # Create
    margins = "---------------------------------------------------"
    
    # Print header
    print("\n" + margins + "\n" + row(title) + "\n" + margins)


# Create row
def row(txt):
    # Create
    row = list("|                                                 |")

    # Change content
    for pos in range(len(txt)):
        # Replace each character
        row[pos + 2] = txt[pos]
    
    # Return row
    return "".join(row)