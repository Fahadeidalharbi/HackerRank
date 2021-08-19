if __name__ == '__main__':
    list_students_score=[]
    for _ in range(0,int(input())):
        list_students_score.append([input(),float(input())])
    second_lowest_grade = sorted(list(set([score for name, score in list_students_score])))[1]
    for name,score in sorted(list1):
        if score==second_lowest_grade:
            print(name)
            