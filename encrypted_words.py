import math

def findEncryptedWord(S):
    if len(S) == 0:                 # Hard-stop for recursive endpoints
        return ""
    n = math.ceil(len(S)/2)-1       # Midpoint calculation
    R = S[n]                        # Initial appending of middle-est character
    R += findEncryptedWord(S[:n])   # Recursive calls
    R += findEncryptedWord(S[n+1:])
    return R                        # Final string returned (if S is originally not empty)

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "abc"
    expected_1 = "bac"
    output_1 = findEncryptedWord(s1)
    check(expected_1, output_1)

    s2 = "abcd"
    expected_2 = "bacd"
    output_2 = findEncryptedWord(s2)
    check(expected_2, output_2)

    # Add your own test cases here
    s3 = "abcxcba"
    expected_3 = "xbacbca"
    output_3 = findEncryptedWord(s3)
    check(expected_3, output_3)
