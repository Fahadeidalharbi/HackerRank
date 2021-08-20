if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    length_score= len(student_marks.get(query_name))
    sum_of_score= sum(student_marks.get(query_name))/length_score
    print('{0:.2f}'.format(sum_of_score))
