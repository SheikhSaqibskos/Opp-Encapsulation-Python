class Student:
    def __init__(self, name, grade):
        self.name = name          # Public attribute
        self._grade = grade       # Protected attribute
        self.__percentage = 90    # Private attribute

    def display_info(self):
        print("Name:", self.name)
        print("Grade:", self._grade)

    def show_percentage(self):
        print("Percentage:", self.__percentage)

# Create object
s1 = Student("Ali", "A")

s1.display_info()
s1.show_percentage()

# Access levels
print("\nPublic:", s1.name)           # ✅ works
print("Protected:", s1._grade)        # ⚠ works but should be avoided
# print(s1.__percentage)              # ❌ Error (private)
print("Private (via name mangling):", s1._Student__percentage)  # ✅ works but not recommended
