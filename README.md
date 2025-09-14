# Minpro1
Nama: Muhammad Arza Dwiarto Anugerah  
Nim : 2509116007  
Sistem Informasi A  
  
Tentang kode saya:  
Saya membuat kode untuk sistem informasi tarif tol yang dimana nantinya kita bisa mengetahui tarif tol berdasarkan daerah,jalan tol dan golongan kendaraan. Saya juga menambahkan menu untuk menambahkan data jalan tol baru pada daerah tertentu dan juga melakukan update atau mengubah tarif tol terhadap golongan kendaraan tertentu.  
  
Pada baris 1-6 menampilkan menu dan melakukan input menu.  
pada baris 9-19 jika memilih menu cek tarif tol akan menampilkan daftar daerah dan melakukan input untuk daerah yang dipilih.
pada baris 21-110 adalah bagian dimana kita akan melakukan input jalan tol dan golongan kendaraan lalu program akan menampilkan tarif tol.  
pada baris 112-120 jika memilih menu menambahkan data jalan tol.  
pada baris 122-162 adalah bagian dimana kita akan melakukan input data jalan tol yang ingin ditambahkan.  
pada baris 165-173 jika memilih menu mengupdate atau merubah tarif tol.  
pada baris 175-237 adalah bagian dimana kita melakukan input tarif tol yang ingin diubah.  

**Flowchart**:  
Hal 1  

<img width="511" height="658" alt="hal1" src="https://github.com/user-attachments/assets/52eb508a-ee27-47d7-86cb-e0d452808bf5" />   

Hal 2    

<img width="510" height="522" alt="hal2" src="https://github.com/user-attachments/assets/e3f11578-fe57-4db3-8d0f-fbcd715042d4" />  

Hal 3    

<img width="500" height="512" alt="hal3" src="https://github.com/user-attachments/assets/50a8bb50-5736-44a4-9ad5-0eb0413e6125" />  

Hal 4    

<img width="502" height="511" alt="hal4" src="https://github.com/user-attachments/assets/079b8327-9b44-49bb-8b20-9db6921e0a07" />  

Hal 5    

<img width="675" height="614" alt="hal5" src="https://github.com/user-attachments/assets/89a05971-6c14-486b-9a2b-189859c3eae0" />  

Hal 6    

<img width="479" height="617" alt="hal6" src="https://github.com/user-attachments/assets/f41625e0-b97e-4f10-ad20-626b62864466" />  

Hal 7  

<img width="193" height="271" alt="hal7" src="https://github.com/user-attachments/assets/707a0079-143e-475a-adf6-f578c0f98cd2" />  

Hal 8  

<img width="164" height="180" alt="hal8" src="https://github.com/user-attachments/assets/b93ddb4e-ba92-40b5-86e8-bdd4a9eb82cd" />  

**Kode program saya :**  
Pada baris ini akan menampilkan pilihan menu menggunakan kode angka, setelah itu kita harus melakukan input menggunakan angka karena pada bagian input sudah di buat menjadi tipe data integer, jikalau melakukan input yang merupakan tipe data string akan menjadi error.  
<img width="332" height="119" alt="Kode1" src="https://github.com/user-attachments/assets/c73ca4e1-96e1-494d-854a-2d3ace763502" />  

Ini tampilan menu lanjutan jika kita ingin melakukan cek tarif tol berdasarkan daerah,jalan tol dan golongan kendaraan nya. Pada bagian ini juga saya meletakkan tupple untuk daerah karena data ini tidak ingin saya lakukan perubahan, lalu kita akan melakukan input lagi berdasarkan kode angka daerah yang ada, saya sengaja meletakkan "" dan "Daerah" pada awal bebrapa list dan tupple saya supaya index nya bisa langsung dari 1.
<img width="554" height="222" alt="Kode2" src="https://github.com/user-attachments/assets/c351771c-58a4-4806-b267-22d8b2922101" />  

Kemudian berikut adalah kdoe untuk tiap daerah yang dipilih, jadi setelah melakukan input daerah pada menu sebelumnya kita akan melakukan lagi input jalan tol berdasarkan menu yang disediakan, nah setelah itu lanjut melakukan input untuk golongan kendaraan berdasarkan list yang ditampilkan, lalu untuk menentukan output nya sesuai dengan hasil inputan dan list yang ada saya menggunakan List[input] untuk menentukan index nya.
<img width="819" height="480" alt="Kode3" src="https://github.com/user-attachments/assets/b6b737fc-0fff-4ce9-ae26-ca24bccb477b" />  
<img width="926" height="424" alt="Kode4" src="https://github.com/user-attachments/assets/e74a4262-a3d9-41e3-80bd-b2a9ef1bdeae" />  
<img width="1045" height="368" alt="Kode5" src="https://github.com/user-attachments/assets/c0fc006a-01e5-4609-bd70-ee26c3cd3d23" />  
<img width="812" height="407" alt="Kode6" src="https://github.com/user-attachments/assets/f1e32011-a349-4c31-b07a-a20d96f58802" />  

Ini tampilan menu lanjutan jika kita ingin menambahkan data jalan tol. 
<img width="538" height="174" alt="Kode7" src="https://github.com/user-attachments/assets/511be42c-16a9-44be-87e6-18fdabc861f3" />  

kemudian berikut adalah kode untuk tiap daerah yang dipilih, disini saya menggunakan append dari inputan untuk menambahkan hasil inputan ke dalam list.  
<img width="667" height="185" alt="Kode8" src="https://github.com/user-attachments/assets/e33f2ef8-b564-492c-8d7a-a6afb8acbb4d" />  
<img width="655" height="177" alt="Kode9" src="https://github.com/user-attachments/assets/b65fd2f2-01f7-474a-b7bf-96551e5d6dab" />  
<img width="660" height="182" alt="Kode10" src="https://github.com/user-attachments/assets/192422cd-baa2-45d1-9969-bdedafb577f8" />  
<img width="648" height="211" alt="Kode11" src="https://github.com/user-attachments/assets/617efa49-8f56-430d-be5c-dee6bdfed7bc" />  

Ini tampilan menu lanjutan jika kita ingin merubah tarif tol pada daerah tertentu.  
<img width="542" height="178" alt="Kode12" src="https://github.com/user-attachments/assets/c145b7ee-70d0-4be4-88b0-3fb7f89a9f78" />   

Berikut kode untuk merubah tarif tol pada daerah yang sudah dipilih,  untuk di list ini saya langsung menggunakan List[index] agar langsung menampilkan tarif berdasarkan data di list tarif tol dan disini saya menggunakan list[input1] = input2 jadi pada input1 itu kita memasukkan index pada data yang ada lalu akan digantikan dengan input2 yang mana input 2 itu sendiri adalah harga atau tarif baru nya jadi tarif baru akan diletakkan pada index input1 untuk mengganti tarif nya.  
<img width="755" height="287" alt="Kode13" src="https://github.com/user-attachments/assets/9c161bca-78f5-4c2a-b437-1c147c4820d6" />  
<img width="757" height="292" alt="Kode14" src="https://github.com/user-attachments/assets/eb715925-7308-4707-8dad-167f98836667" />  
<img width="756" height="283" alt="Kode15" src="https://github.com/user-attachments/assets/d193a352-a72a-47c0-8817-fc1108b89c56" />  
<img width="755" height="366" alt="Kode16" src="https://github.com/user-attachments/assets/3613333f-216b-46c2-8bad-35a4a41809b7" />  

**Berikut hasil output dari program saya:**  
<img width="704" height="459" alt="Output1" src="https://github.com/user-attachments/assets/321cc8ac-73ce-4b01-839d-82d6dd91ab57" />  
<img width="708" height="316" alt="Output2" src="https://github.com/user-attachments/assets/d0b04fa5-142a-463b-9240-b267ab74b13d" />  
<img width="702" height="411" alt="Output3" src="https://github.com/user-attachments/assets/044efa32-30c6-45dd-aff4-b1cf63377418" />  
<img width="716" height="127" alt="OutputTvalid" src="https://github.com/user-attachments/assets/8bdb23d7-2504-49f1-8813-bed272474fcc" />




































