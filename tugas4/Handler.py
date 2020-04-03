import os

class Handler:
    def __init__(self):
        if not os.path.exists("file"):
            os.makedirs("file")
    def upload(self,filename=None,data=None):
        f = open("file/"+filename,"wb")
        f.write(data)
        return True
    def download(self,filename=None):
        f = open(filename,"rb")
        result = f.read()
        f.close()
        result = str(result, "utf-8")
        return result
    def lihat_list(self):
        list_file = os.listdir("file")
        f = []
        for filename in list_file:
            f.append(filename)
        return f

if __name__=='__main__':
    h = Handler()
            