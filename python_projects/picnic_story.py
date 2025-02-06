def encode_picnic_story(story, commands, base):
    # Step 1: Apply the commands to the story
    for command in commands:
        if command == "reverse":
            story = story[::-1]
        elif command == "uppercase":
            story = story.upper()
        elif command == "sort":
            story = ''.join(sorted(story))
    
    # Step 2: Convert each character to its ASCII code
    ascii_codes = [ord(char) for char in story]
    
    # Step 3: Convert each ASCII code to the specified base
    if base == "binary":
        base_func = lambda x: bin(x)[2:]
    elif base == "octal":
        base_func = lambda x: oct(x)[2:]
    elif base == "decimal":
        base_func = lambda x: str(x)
    elif base == "hexadecimal":
        base_func = lambda x: hex(x)[2:]
    else:
        raise ValueError("Invalid base")
    
    # Convert each ASCII code and concatenate them
    encoded_story = ''.join(base_func(code) for code in ascii_codes)
    
    return encoded_story

# Test example
story = "Picnic time!"
commands = ["reverse", "uppercase", "sort"]
base = "binary"

encoded_story = encode_picnic_story(story, commands, base)
print(encoded_story)
