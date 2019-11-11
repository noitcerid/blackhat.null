from classes.Server import Server
from classes.Employee import Employee
from classes.Company import Company

# s1contents = ["File A.txt", "File B.txt", "File C.jpg"]
# s2contents = [["1234", "John Smith", 123.45], ["2345", "Suzie Sanders", 524.12]]
# s3contents = [["Chris", "Potter", "1234 Anywhere Rd.", "Orlando", "FL"],
#               ["Jim", "Jones", "123 Middle Rd.", "Indianapolis", "IN"]]
#
# s1 = Server(1, "Server A", "file", "192.192.192.192", 1, s1contents)
# s2 = Server(2, "Server B", "bank", "10.10.10.10", 2, s2contents)
# s3 = Server(3, "Server C", "database", "10.80.3.18", 2, s3contents)
#
# print(s1)
# print(s2)
# print(s3)

e1 = Employee(1, "Bob", "Smith", "111-22-3333", "111-222-3333", "123 Anywhere Rd.", "Orlando", "FL", "32830", None,
              "Network Engineer", 123200.00, ["Network Security, Class 1"])

c1 = Company(1, "Bob's Computer Services", "Fixing your computer problems since 1992!", 4, 100000, 1992, [e1])

print(e1)
print(c1)
