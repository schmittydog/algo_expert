def isPalindrome(string):
    '''
        Time: N
        Space: 1
    '''
    for i in range(len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return False
    return True
