from os import mkdir
from os.path import exists
import pickle


class Filer:
    def __init__(self, dictname="unnamed_dict"):
        self.my_name = dictname
        if not exists(dictname):
            mkdir(dictname)
    def __getitem__(self, item):
        path = "{}/{}".format(self.my_name, item)
        value = ""
        with open(path, "rb") as f:
            file_data = f.read()
            value = pickle.loads(file_data)
        return value
    def __setitem__(self, item, value):
        path = "{}/{}".format(self.my_name, item)
        with open(path, "wb") as f:
            file_data = pickle.dumps(value)
            f.write(file_data)

if __name__ == "__main__":
    filer_dict = Filer("cats")
    filer_dict["Megan"] = {"weight": 12}
    print(filer_dict["Megan"])  # -> {'weight': 0}
    print(type(filer_dict["Megan"]))  # -> dict