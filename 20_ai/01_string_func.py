# Define the function to clean and convert a string
def clean_and_convert(text):
    # Step 1: Convert entire string to lowercase
    text = text.lower()

    # Step 2: Remove all special characters (keep only letters, digits, and spaces)
    cleaned = ""
    for char in text:
        if char.isalnum() or char.isspace():  # Check if character is a letter, number, or space
            cleaned += char  # Keep the character
        # Else: skip it (i.e., remove special characters like ! @ # etc.)

    # Step 3: Remove extra spaces and replace spaces with dashes
    words = cleaned.strip().split()  # Split string into words
    return "-".join(words)  # Join words using dash

# ===== Example Inputs =====
examples = [
    "Hello World!",
    "Python is    awesome!!!",
    "C@de w!th $$$ me",
    "  Learn - Code - Repeat  ",
    "Be #1 in 2025!!"
]

# ===== Run the function on each example and print the result =====
for i, sentence in enumerate(examples, 1):
    print(f"{i}. Original : {sentence}")
    print(f"   Converted: {clean_and_convert(sentence)}\n")
