import filecmp

def are_files_equal(file1, file2):
    return filecmp.cmp(file1, file2, shallow=False)
