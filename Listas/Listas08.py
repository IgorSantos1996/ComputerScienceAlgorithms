from random import randint, random


def has_duplicates(listinha):
    t = list(listinha)
    t.sort()
    for z in range(len(t)-1):
        if t[z] == t[z+1]:
            return True
    return False


def random_days (n):
    t = []
    for i in range(n):
        bday = randint(1, 365)
        t.append(bday)
    return t

def count_matches(num_students, num_simulations):
    contador = 0
    for i in range(num_simulations):
        t = random_days(num_students)
        if has_duplicates(t):
            contador = contador + 1
        return contador

def main():
    """Runs the birthday simulation and prints the number of matches."""
    num_students = 200
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


if __name__ == '__main__':
    main()