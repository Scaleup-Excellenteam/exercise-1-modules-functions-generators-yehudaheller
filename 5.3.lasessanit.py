import re


# Define a generator function that yields blocks of data from a file
def read_file_in_blocks(filename, block_size=4096):
    with open(filename, 'rb') as f:
        while True:
            block = f.read(block_size)
            if not block:
                break
            yield block


# Define a generator function that yields secret messages from a block of text
def extract_secret_messages(text_block):
    messages = re.findall(r'\b[a-z]{5,}!\b', text_block)
    for message in messages:
        yield message


# Use the generators to read the logo file and extract secret messages
for block in read_file_in_blocks('logo.jpg'):
    text_block = block.decode('ascii', errors='ignore')
    for message in extract_secret_messages(text_block):
        print(message)
