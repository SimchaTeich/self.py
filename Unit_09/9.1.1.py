def are_files_equal(file1, file2):
    # open files
    files_object1 = open(file1, "r")
    files_object2 = open(file2, "r")
    
    # read content
    content1 = files_object1.read()
    content2 = files_object2.read()
    
    # close files
    files_object1.close()
    files_object2.close()
    
    return content1 == content2
