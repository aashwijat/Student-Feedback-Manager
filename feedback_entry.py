## FEEDBACK ENTRY PYTHON FILE

print("---STUDENT FEEDBACK FORM---")

##student details
print("Enter Your Details")
name = str(input("Name : "))
course = str(input("Course : "))
srn = str(input("SRN : "))

## subject wise feedback entry
print("Enter Your Feedback")
jt = str(input("Feedback for Java Technologies : "))
ecom = str(input("Feedback for E-commerce Development : "))
se = str(input("Feedback for Software Engineering : "))
vcs = str(input("Feedback for Version Control Systems : "))
cie = str(input("Feedback for Entrepreneurship : "))

## feedback summary
print("---FEEDBACK SUMMARY---")
print("Java Technologies : ",jt)
print("E-commerce Development : ",ecom)
print("Software Engineering : ",se)
print("Version Control System : ", vcs)
print("Entrepreneurship : ",cie)
