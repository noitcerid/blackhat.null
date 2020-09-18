from classes.Contents import Contents
from classes.Qualification import Qualification
from classes.Server import Server
from classes.Employee import Employee
from classes.Company import Company
from classes.Network import Network
from classes.Disk import Disk
from setup import *

# q1 = Qualification("Network Security", "Class 1")
# q1 = QUALIFICATIONS[1]
# e1 = Employee(4, "Jim", "Bond", "999-88-7777", "123-123-1234", "9876 Somewhere St.", "St. Louis", "MO", "11111", None,
#               None, 0, q1)
#
# s1contents = Contents(["File A.txt", "File B.txt", "File C.jpg"])
# s2contents = Contents([["1234", "John Smith", 123.45], ["2345", "Suzie Sanders", 524.12]])
# s3contents = Contents([str(e1), ["Jim", "Jones", "123 Middle Rd.", "Indianapolis", "IN"]])
#
# s1 = Server(1, "Server A", "file", "192.192.192.192", 1, s1contents)
# s2 = Server(2, "Server B", "bank", "10.10.10.10", 2, s2contents)
# s3 = Server(3, "Server C", "database", "10.80.3.18", 2, s3contents)
#
# print("----------------------")
# print(s1)
# print(s2)
# print(s3)
#
# e2 = Employee(1, "Bob", "Smith", "111-22-3333", "111-222-3333", "123 Anywhere Rd.", "Orlando", "FL", "32830", None,
#               "Network Engineer", 123200.00, q1)
#
# c1 = Company(1, "Bob's Computer Services", "Fixing your computer problems since 1992!", 4, 100000, 1992, [e2])
# print("----------------------")
# print(e2)
# print("----------------------")
# print(c1)
# print("----------------------")

# n1 = Network("Gigawatts Wifi B v1", "Wireless B Adapter", 100, 1, 1, 1)
# d1 = Disk("MaxSpace Slow HDD", "Standard Slow HDD", 100, 1, 10, 20)

# print("----------------------")
# print(n1.name)
# print("----------------------")
# print(n1.bandwidth)

# Print Setup Details
print(
    f"Loading data set into blackhat.null...\n"
    f"Companies:\t\t{len(COMPANIES)}\n"
    f"Employees:\t\t{len(EMPLOYEES)}\n"
    f"Store Items:\t{len(MEMORY) + len(NETWORKS) + len(PROCESSORS)}\n"
    f"- Memory:\t\t{len(MEMORY)}\n"
    f"- Network:\t\t{len(NETWORKS)}\n"
    f"- Processors:\t{len(PROCESSORS)}\n"
    f"Qualifications:\t{len(QUALIFICATIONS)}\n"
    f"Servers:\t\t{len(SERVERS)}\n"
    f"Data loaded successfully!"
)
