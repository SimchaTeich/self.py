def copy_file_content(source, destination):
    with open(source, 'r') as src_file, \
        open(destination, 'w') as dst_file:
        dst_file.write(src_file.read())
