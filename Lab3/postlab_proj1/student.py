"""
File: student.py
Resources to manage a student's name and test scores.
"""


class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)


    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

  


    """NEW ADDED DUNDER FUNCTIONS"""
    def __eq__(self, other):
        """Returns True if the two Student objects have the same name, False otherwise."""
        return self.getAverage() == other.getAverage()


    def __lt__(self, other):
        """Test if the name of self is less than the name of other."""
        return self.getAverage() < other.getAverage()


    def __ge__(self, other):
        """Test if the name of self is greater than or equal to the name of other."""
        return self.getAverage() >= other.getAverage()

def main():

    """A simple test."""
    student1 = Student("Dazai", 5)
    student2 = Student("Gojo", 5)
    student3 = Student("Anya", 5)


    for i in range(1, 6):
        student1.setScore(i, 80)
        student2.setScore(i, 90)
        student3.setScore(i, 70)
      
    print(student1)
    print(student2)
    print(student3)

    # Testing equality
    print(f"\nIs {student1.getName()} equal to {student2.getName()}? {student1 == student2}")
    print(f"Is {student1.getName()} equal to {student3.getName()}? {student1 == student3}")

    # Testing less than
    print(f"\nIs {student1.getName()} less than {student2.getName()}? {student1 < student2}")
    print(f"Is {student1.getName()} less than {student3.getName()}? {student1 < student3}")

    # Testing greater than or equal to
    print(f"\nIs {student1.getName()} greater than or equal to {student2.getName()}? {student1 >= student2}")
    print(f"Is {student1.getName()} greater than or equal to {student3.getName()}? {student1 >= student3}")

if __name__ == "__main__":
    main()
