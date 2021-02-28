# Nama : Giovani Anggasta
# NIM : 13519155
# Kelas : K3
# Deskripsi : Aplikasi topological sort pada pengelompokan matkul per semester

# fungsi untuk memasukkan matkul dan syarat dari file ke dalam array
def fromFile (namaFile):
    daftarMatkul = []
    openFile = open(namaFile, 'r')
    readFile = openFile.readlines()
    for line in readFile:
        clean = line.replace('.','').split(',')
        mata_kuliah = [matkul.strip() for matkul in clean] 
        daftarMatkul.append(mata_kuliah)
    return daftarMatkul

# fungsi untuk mendapatkan masing2 matkul
def getEachMatkul (daftarMatkul):
    eachMatkul = []
    for matkul in daftarMatkul:
        for i in range(len(matkul)):
            if (i == 0):
                eachMatkul.append(matkul[i])
    return eachMatkul

# fungsi untuk mendapatkan syarat dari masing2 matkul
def getSyarat (daftarMatkul):
    for matkul in daftarMatkul:
        for i in range(len(matkul)):
            if (i == 0):
                matkul.remove(matkul[i])
    return daftarMatkul

# fungsi untuk membuat dictionary antara masing2 matkul dengan syaratnya
def setDictMatkul (eachMatkul, syaratMatkul):
    dictMatkul = dict(zip(eachMatkul,syaratMatkul))
    return dictMatkul

# fungsi untuk mengecek apakah jumlah semua syarat sudah nol atau belum
def isAllNol (banyakSyarat):
    condition = True
    for syarat in banyakSyarat:
        if (int(banyakSyarat[syarat]) > 0):
            condition = False
            break
    return condition

# fungsi untuk mengembalikan matkul yang tidak mempunyai syarat
def matkulNoSyarat (dictMatkul, banyakSyarat):
    tanpaSyarat = []
    for eachMatkul in dictMatkul:
        if (banyakSyarat[eachMatkul] == 0):
            tanpaSyarat.append(eachMatkul)
    return tanpaSyarat

def topologicalSort (dictMatkul):
    # hitung berapa banyak syarat dari tiap matkul
    banyakSyarat = {eachMatkul : 0 for eachMatkul in dictMatkul}
    for eachMatkul in dictMatkul:
        for syaratMatkul in dictMatkul[eachMatkul]:
            banyakSyarat[eachMatkul] += 1

    # mencari matkul tanpa syarat
    tanpaSyarat = matkulNoSyarat(dictMatkul, banyakSyarat)
    
    # masukkin matkul tanpa syarat ke list urutan matkul
    urutanMatkul = []
    urutanMatkul.append(tanpaSyarat)

    MatkulSemester = []
    MatkulTemporari = []
    
    # memasukkan matkul lain ke dalam list urutan matkul
    nol = isAllNol(banyakSyarat)
    MatkulTemporari = []
    while(not(nol)):
        for eachMatkul in dictMatkul:
            if(banyakSyarat[eachMatkul] > 0):
                for need in dictMatkul[eachMatkul]:
                    for i in tanpaSyarat:
                        if((need == i) and (banyakSyarat[eachMatkul] > 0)):
                            banyakSyarat[eachMatkul] -= 1

        '''______________________________________________'''
        MatkulSemester = []
        for eachMatkul in dictMatkul:
            if(banyakSyarat[eachMatkul]==0):
                MatkulSemester.append(eachMatkul)
        MatkulTemporari=MatkulTemporari+[value for value in MatkulSemester if value in tanpaSyarat] 
        tanpaSyarat=list(set(tanpaSyarat)|set(MatkulSemester))
        for i in MatkulTemporari:
            if i in tanpaSyarat:
                tanpaSyarat.remove(i)
        urutanMatkul.append(MatkulSemester)
        nol = isAllNol(banyakSyarat)
        hapusMatkul(urutanMatkul)
    return urutanMatkul

# fungsi untuk menghapus matkul yang double
def hapusMatkul(urutanMatkul):
    panjang = len(urutanMatkul)
    for i in range (len(urutanMatkul)):
        for j in urutanMatkul[i]:
            for k in range (i+1,panjang):
                if j in urutanMatkul[k]:
                    urutanMatkul[k].remove(j)
    return urutanMatkul

# prosedur untuk menampilkan matkul per semester
def printMatkul(urutanMatkul):
    for i in range(len(urutanMatkul)):
        print("Semester ", i+1, " : ", end='')
        for j in urutanMatkul[i]:
            print(j," ",end='')
        print('')
    
# main
namaFile = input("Masukkan nama file : ")
direct = '../test/'
daftarMatkul = fromFile(direct+namaFile)
eachMatkul = getEachMatkul(daftarMatkul)
syaratMatkul = getSyarat(daftarMatkul)
dictMatkul = setDictMatkul(eachMatkul,syaratMatkul)
urutanMatkul = topologicalSort(dictMatkul)
printMatkul(urutanMatkul)