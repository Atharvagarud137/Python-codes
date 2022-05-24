d={}
number_of_students = int(input("Enter number of students : "))
print('Enter {} student names and marks'.format(number_of_students))
d = dict(input().split() for i in range(number_of_students))
for keys in d.keys():
    d[keys]=int(d[keys])
top_scorer = max(zip(d.values(), d.keys()))[1]
top_scorer_marks = max(zip(d.values(), d.keys()))[0]
lowest_scorer = min(zip(d.values(), d.keys()))[1]
lowest_scorer_marks = min(zip(d.values(), d.keys()))[0]
passing_marks = 12
passed_students=0
for value in d.values():
    if value>=passing_marks:
        passed_students+=1
failed_students=number_of_students-passed_students
print('Top scorer is {} with {} marks'.format(top_scorer,top_scorer_marks))
print('Lowest scorer is {} with {} marks'.format(lowest_scorer,lowest_scorer_marks))
print('Number of students passed: {}'.format(passed_students))
print('Number of students failed: {}'.format(failed_students))
