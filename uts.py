#membuat data mahasiswa

#memasukkan data pada list
def mahasiswa_input(data1, data2, no):
    while True:
        data1.append(input('masukkan %s mahasiswa : '%data2))
        if len(data1[i]) == no:
            break
        else:
            data1.pop(i)
            continue
#variabel
i = a = b = 0
nm_mhs=[]
nim=[]
kelas=[]
jurusan=[]
angkatan=[]

while True:
    print('mahasiswa data ke - ', i+1)
    nm_mhs.append(input('masukkan nama mahasiswa '))
    mahasiswa_input(nim, 'NIM', 10)
    mahasiswa_input(kelas, 'KELAS(A-D)', 1)
    mahasiswa_input(jurusan,'JURUSAN(TI,MI)', 2)
    if jurusan[i] == 'TI':
        jurusan[i] = 'TEKNIK INFORMATIKA'
        a+=1
    elif jurusan[i] == 'MI':
        jurusan[i] = 'Management Informatika'
        b+=1
    else:
        print('data salah')
        jurusan.pop(i)
        nm_mhs.pop(i)
        kelas.pop(i)
        nim.pop(i)
        continue
    mahasiswa_input(angkatan, "angkatan ", 4)
    ulangi=""
    while ulangi!=('y' or 't'):
        ulangi = input("input lagi ?y/t: ")
        if ulangi == 'y':
            i+=1
        elif ulangi == 't':
            break
        else:
            continue
    if ulangi == 't':
        break
    continue

print(" daftar mahasiswa ")
print('no nama     nim    kelas        jurusan        angkatan ')

for data in range (len(nim)):
    print(data+1,nm_mhs[data], "\t",nim[data],"\t",kelas[data],"\t", jurusan[data],"\t", angkatan[data], "\t")
    print('Total jurusan Teknik informatika = ',a,'orang\n')
    print('Total jurusan Management Informatika = ',b,'orang\n')
    

