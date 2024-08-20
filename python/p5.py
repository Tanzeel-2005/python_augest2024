#accept average score from the student of his previous exam and print his result as follows:
#0 tp 49 is fail
#50 to 74 is second
#75 to 90 is first class
#91 to 100 is distinction
#also check for invalid score
avg_marks=int(input("Enter the average score of your previous exam"))

if (avg_marks>=91 and avg_marks<=100):
     print("distinction")
elif (avg_marks>=75 and avg_marks<=90):
    print("first class")
elif avg_marks>=50 and avg_marks<=74:
    print("second")
elif avg_marks>=0 and avg_marks>=49:
    print("fail")
else:
    print("Invalid score")

