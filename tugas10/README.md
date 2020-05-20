# Tugas 10

1. Pull update terbaru
2. Jalankan async_server.py pada port 9002, 9003, 9004, 9005 (lihat pada BackendList)
3. Jalankan file lb.py, jalankan di port 44444
4. Jalankan browser, akseslah http://localhost:44444/page.html
5. Lihatlah di log program, bahwa setiap request akan dilayani oleh backend yang bergantian
6. Lakukan performance test seperti pada tugas 9, bandingkan penggunaan load balancer dengan async_server dengan server_thread_http pada folder progjar5
7. Buatlah tabel hasilnya

<h2>Jawaban</h2>

<li> Jalankan runserver.sh (async_server.py server dengan port 9002, 9003, 9004, 9005)</li>
<img src="https://github.com/atikakiki/PROGJAR_05111740000015/blob/master/tugas10/SS/jalan_runserver.PNG"></img>
<li> Jalankan lb.py (load balancer)</li>
<img src="https://github.com/atikakiki/PROGJAR_05111740000015/blob/master/tugas10/SS/jalan_lb.PNG"></img>
<li> Mengakses http://localhost:44444/page.html pada browser</li>
<img src="https://github.com/atikakiki/PROGJAR_05111740000015/blob/master/tugas10/SS/jalan_html.PNG"></img>
<li> Log Program </li>
<img src="https://github.com/atikakiki/PROGJAR_05111740000015/blob/master/tugas10/SS/jalan_lb.PNG"></img>
<li> Performance test dengan Konkurensi = 1, 50, 250, 500, 750, 1000</li>
<img src="https://github.com/atikakiki/PROGJAR_05111740000015/blob/master/tugas10/SS/server_thread_table.PNG"></img>
<img src="https://github.com/atikakiki/PROGJAR_05111740000015/blob/master/tugas10/SS/server_async_table.PNG"></img>
<img src="https://github.com/atikakiki/PROGJAR_05111740000015/blob/master/tugas10/SS/server_async_lb_table.PNG"></img>
