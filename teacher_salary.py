"""
Extra Challenge: Teacher’s Salary

b. A school has asked you to write a program that will calculate teachers' salaries.

The program should ask the user to enter the teacher’s name, the number of periods taught in a month,
and the rate per period. The monthly salary is calculated by multiplying the
number of periods by the monthly rate. The current monthly rate per period is $20.

If a teacher has more than 100 periods in a month,
everything above 100 is overtime. Overtime is $25 per period.

For example, if a teacher has taught 105 periods, their monthly gross salary should be 2,125.

Write a function called your_salary that calculates a teacher’s gross salary.

The function should return the teacher’s name, periods taught, and gross salary.

Here is how you should format your output:

Teacher: John Kelly

Periods: 105

Gross salary:2,125
"""


def your_salary():
    name = input("Enter the teacher's name: ")
    rate = int(input("Enter the rate per period: "))
    periods = float(input("Enter the number of periods: "))

    if periods > 100:
        gross_salary = (100 * rate) + ((periods - 100) * (rate + 5))
    else:
        gross_salary = periods * rate
    return f"\nTeacher: {name}\nPeriods: {periods}\nGross salary: {gross_salary}"


if __name__ == "__main__":
    print(your_salary())
