#test grading program
test_score = int(input("Please enter your test score: "))
if test_score > 40:
    print("E grade")
if test_score > 50:
    print("D grade")
if test_score > 60:
    print("C grade")
if test_score > 70:
    print("B grade")
if test_score > 80:
    print("A grade")
else:
    print("Fail")
