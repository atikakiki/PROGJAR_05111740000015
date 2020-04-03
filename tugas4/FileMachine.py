import json
from Handler import Handler

'''
---------- PROTOCOL FORMAT --------------

string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : COMMAND *spasi* PARAMETER *spasi* PARAMETER ...

FITUR

1. Upload File
   Untuk menambahkan (upload) file ke dalam folder "file"
   request     : upload
   parameter   : namafile *spasi* isifile
   response    : berhasil -> ok
                 gagal -> error

2. Download File
   Untuk mengambil (download) file dari folder "file"
   request     : download
   parameter   : namafile
   response    : berhasil -> ok
                 gagal -> error

3. Melihat List File
   Untuk melihat daftar file yang ada di dalam folder "file"
   request     : list
   parameter   : -
   response    : daftar nama file di dalam folder "file"

 Jika command tidak dikenali akan merespon dengan ERRCMD

'''

h = Handler()

class FileMachine:
    def proses(self,data):
        str = data.split(" ")
        try:
            command = str[0].strip()
            if(command=='upload'):
                filename = str[1].strip()
                data = str[2].strip()
                d = data.encode()
                print("Upload file")
                print("Uploading",filename)
                h.upload(filename,d)
                return "Upload success"

            elif(command=='download'):
                filename = str[1].strip()
                print("Download file")
                print("Downloading",filename)
                result = h.download(filename)
                return result

            elif(command=='list'):
                print("Lihat isi folder file")
                result = h.lihat_list()
                res = {"isi folder file":result}
                return json.dumps(res)
                
            else:
                return "ERRCMD"

        except:
            return "Error"

if __name__=='__main__':
    fm = FileMachine()


