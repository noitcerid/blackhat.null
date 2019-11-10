from Server import Server

s1contents = ["File A.txt", "File B.txt", "File C.jpg"]
s2contents = [["1234", "John Smith", 123.45], ["2345", "Suzie Sanders", 524.12]]
s3contents = [["Chris", "Potter", "1234 Anywhere Rd.", "Orlando", "FL"],
              ["Jim", "Jones", "123 Middle Rd.", "Indianapolis", "IN"]]

s1 = Server(1, "Server A", "file", "192.192.192.192", 1, s1contents)
s2 = Server(2, "Server B", "bank", "10.10.10.10", 2, s2contents)
s3 = Server(3, "Server C", "database", "10.80.3.18", 2, s3contents)

print(s1)
print(s2)
print(s3)
