import logging
import requests
import os
import threading

def download_gambar(url=None):
    counter = 0
    while True:
        counter = counter + 1
        ff = requests.get(url)
        tipe = dict()
        tipe['image/png']='png'
        tipe['image/jpg']='jpg'
        tipe['image/jpeg']='jpg'
        content_type = ff.headers['Content-Type']
        # logging.warning(content_type)
        if (content_type in list(tipe.keys())):
            # while True:
            namafile = os.path.basename(url)
            ekstensi = tipe[content_type]
            logging.warning(f"writing {namafile}.{ekstensi} counter {counter}")
            fp = open(f"{namafile}.{ekstensi}","wb")
            fp.write(ff.content)
            fp.close()
            # time.sleep(1)
        else:
            return False
    return

url = ["https://cm1.narvii.com/7290/be7edfb04d351d9044d3ebd40e8acf8e3a648384_00.jpg","https://pbs.twimg.com/profile_images/1165237768324358144/-vyLKy9h_400x400.jpg","https://pbs.twimg.com/profile_images/1218915501427945478/kTd1IxoB.jpg"]

for i in url:
    t = threading.Thread(target=download_gambar,args=(i,))
    t.start()