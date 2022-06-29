#higher order function returning another function

marks = [90, 94, 84, 78]

def get_avg_marks():
    return lambda marks_data : sum(marks_data)/len(marks_data)

avg_func = get_avg_marks()   
print(avg_func(marks)) 