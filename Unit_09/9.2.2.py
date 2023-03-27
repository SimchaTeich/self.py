def copy_file_content(source, destination):
    # open files for reading and writing
    src_file = open(source, 'r')
    dst_file = open(destination, 'w')
    
    # copy content from src file to dst file
    dst_file.write(src_file.read())
    
    # close the files.
    src_file.close()
    dst_file.close()
