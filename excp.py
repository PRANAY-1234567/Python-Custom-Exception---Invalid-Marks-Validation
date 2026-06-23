class InvalidMarksException(Exception):
    def __iinit__(self, marks):
        self.marks = marks

    def __str__(self):
        return f"Invalid marks : {self.marks}"
    
def check_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksException(marks)
    
try:
    marks = int(input("Enter the marks(0-100) : "))
    check_marks(marks)
    print("Valid marks entered")

except InvalidMarksException as e:
    print(e)
