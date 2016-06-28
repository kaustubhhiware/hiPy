import random

def length(listed):
    """
        return length of list
    """
    count = 0
    for item in listed:
        count += 1
    return count

    
def has_duplicates(listed):
    """
        check for duplicates
        Birthday paradox!
    """
    for index in range(length(listed)):
        
        j = index+1
        while j!=length(listed):
            
            if listed[j]==listed[index]:
            #duplicate spotted!
                return True 
            j += 1
    return False


def random_bdays(n):
    """
    
        Returns a list of integers between 1 and 365, with length (n)
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)

    return t


def count_matches(students, samples):
    """

        check how many samples have repeated birthdays
    """
    count = 0
    for i in range(samples):
        t = random_bdays(students)
        if has_duplicates(t):
            count += 1
    return count

#23 is a great number for birthday paradox
num_students = raw_input("Enter number of students there :")
num_students = int(num_students)

num_times = raw_input("Hoe many simulations : ")
num_times = int(num_times)

count = count_matches(num_students,num_times)

chance = 100.0*count/num_times
print 'Chances of 2 people sharing their birthdays : ',chance


