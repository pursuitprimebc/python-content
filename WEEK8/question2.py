'''QUSTION - Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    '''
    # PLATFORM - IITM course

    def relation(file1, file2):
   
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
    num_lines1 = len(lines1)
    num_lines2 = len(lines2)
    
    for i in range(num_lines1):
        if lines1[i].strip() != lines2[i].strip():
            return 'No Relation'
            
    if num_lines1 == num_lines2:
        return 'Equal'
    else:
        return 'Subset'