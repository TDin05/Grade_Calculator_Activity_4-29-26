#i made this myself using online compiler
#I also used w3school for syntax, claude for comprehension, and the compiler has auto fill
#that was probably take like a lot of minus point huh
#and yes I passed this in a laptop after the electricity cameback
#lastly, no I can't use the laptop without electricity it's battery is fried
# acts as a reference from failed to passed
grade_thresholds = (
    (90, 100, "A", "Excellent"),
    (80, 89,  "B", "Good"),
    (70, 79,  "C", "Satisfactory"),
    (60, 69,  "D", "Needs Improvement"),
    (0,  59,  "F", "Failed"),
)
passing_grade = 60   # 60 and above = PASSED

# compare the input grade on the thresholds
def get_grade_info(score):
    for low, high, letter, remarks in grade_thresholds:
        if low <= score <= high:
            return letter, remarks
    return "F", "Failed"
#make sure grade in put doesn't go under 0 or over 100(thanks for the suggestion sir)
def input_grade(subject):
    while True:#loops the code till you put proper number
        grade = float(input(f"  Enter grade for {subject} (0–100): "))
        if 0 <= grade <= 100:#needed to be satisfied for the while loop to stop
            return grade#stops the loop
        print("  Grade must be between 0 and 100. Try again.")

# main actual grade calcu
print("=" * 65)
print("                     STUDENT GRADE CALCULATOR")
print("=" * 65)
name    = input("Student name   : ").strip()
section = input("Year / Section : ").strip()

# collect subjects into a LIST (the number of subject impacts the needed to be named and grades to input so be cautious)
subjects = []#empty so when you put in a new sub there's no un necessary stuff other than the one you gave

# do not I repeat do not put high number of subject if you are using a compiler it will slow down the process
print(f"\nHow many subjects does {name} have?")
while True:
    count = int(input("Number of subjects: "))
    if count >= 1:
        break
    print("Must be at least 1.")#make sure that the subject is not 0 (I didn't put any limit on how high the number tho)

print()
for i in range(count):
    sub_name = input(f"Subject {i+1} name: ").strip()#the +1 makes it so its not 0123 but 1234
    grade    = input_grade(sub_name)
    subjects.append((sub_name, grade))#to add a new sub in a list
    print()

# display the results, it sometime causes the console to be stuck in online compilers run so becareful of dat (it probably because my device is slow)
print("\n" + "=" * 65)
print(f"                 REPORT CARD — {name}  |  {section}")
print("=" * 65)
print(f"  {'Subject':<20} {'Grade':>6}  {'Letter':^6}  {'Remarks':<18}  Status")
print("-" * 65)
#this are for each tupple that was collected during the eniter run/loop
passed_count = 0
failed_count = 0
total_grade  = 0

for sub_name, grade in subjects:
    letter, remarks = get_grade_info(grade)#calling the code above
    status = "PASSED" if grade >= passing_grade else "FAILED"
    if grade >= passing_grade:
        passed_count += 1
    else:
        failed_count += 1
    total_grade += grade
    print(f"  {sub_name:<20} {grade:>6.1f}  {letter:^6}  {remarks:<18}  {status}") # for showing the entire sub name and grades given by the student(i is neat that the aligning commands in js can be used in this)

average = total_grade / count

print("=" * 65)
print(f"  Total subjects : {count}")
print(f"  Passed         : {passed_count}")
print(f"  Failed         : {failed_count}")
print(f"  Average grade  : {average:.1f}")
print(f"  Overall result : {'PASSED ALL SUBJECTS' if failed_count == 0 else 'FAILED IN SOME SUBJECTS'}")
print("=" * 65) #shows the overall results like the ones in the reportcard that cause our parents to beat us up

#I passed this using vscode since I can use my laptop now anyway I know may minus kasi may assist ng ai and a third party site
#Tabamo, Dhayle P.