import time
#use time to map efficiency

def append_word_list():
    """

    	Build list of all words using append
    """
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)

    return t


def add_word_list():
    """

    	Build list of all words using +
    """
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    
    return t


start_time = time.time()
appended_list = append_word_list()
elapsed_time = time.time() - start_time

print len(appended_list)
print appended_list[:10]
print elapsed_time, 'seconds'

start_time = time.time()
added_list = add_word_list()
elapsed_time = time.time() - start_time

print len(added_list)
print added_list[:10]
print elapsed_time, 'seconds'

"""

output : 
['aa', 'aah', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'aardvark']

0.022796869278 seconds
113809
['aa', 'aah', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'aardvark']

61.8892769814 seconds

First method wins , hands down _| |_
"""