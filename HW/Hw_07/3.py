import pickle
import dill


class User:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __repr__(self):
        return f"{self.id}:{self.first_name} {self.last_name} <{self.phone}>"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"


with open("users.pickled", "rb") as f:
    result = pickle.load(f)

my_list = ["5:Mohammad Kavoshi <09123456789>", "11:Reza Kavoshi <09363456789>", "87:Akbar Samiri <09123456789>",
           "22:Taha Mojtabaii <09193456789>", "67:Sadat Karmaii <09363456789>", "1:Javid Elahi <09193456789>",
           "2:Karim Rezai <09193456789>", "77:Salar Mohammadi <09373456789>"]
my_dict = {}
for i in my_list:
    x = i.split(":")
    my_dict[int(x[0])] = x[1]
my_sort = sorted(my_dict)
dict_2 = {}

with open("output-q-3-1.txt", "w") as f:
    for j in my_sort:
        dict_2[j] = my_dict[j]
        f.write(f"{j}:{my_dict[j]}\n")

with open("output-q-3-2.txt", "w") as f:
    filter_number = "919"
    for value in dict_2:
        if filter_number in dict_2[value]:
            f.write(f"filter by filter number : {dict_2[value]}")

obj1 = User("1", "Masoud", "Zandi", "09120572655")
my_dill = dill.dumps(obj1.fullname())
with open("output-q-3-3.dill", "wb") as f:
    f.write(my_dill)
