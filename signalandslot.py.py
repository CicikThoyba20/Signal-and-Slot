import sys#import system
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def topLayout(window):
    label = QLabel("Bangun Datar Segitiga")#judul
    label.setStyleSheet("color : orange")
    label.setAlignment(Qt.AlignCenter)#membuat align ditengah
    layout1 = QVBoxLayout()#membuat layout vertikal
    layout1.addWidget(label)#menambahkan widget
    return layout1#mengembalikan nilai layout

def hitungSegitiga(window):
    groupbox = QGroupBox("Menghitung Luas Segitiga", window)#membuat grupbox
    labelRusuk = QLabel("Panjang Alas Segitiga: ")#membuat label 
    global rusuk#agar variabel suhu bisa diakses fungsi lain
    labelRusuk2 = QLabel("Panjang Tinggi Segitiga: ")#membuat label dengan nama labelrusuk2
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global rusuk2
    rusuk = QLineEdit()#widget inputan
    rusuk2 = QLineEdit()#widget inputan
    btn = QPushButton("Hitung")#membuat tombol
    btn.setStyleSheet("background: orange")
    btn.clicked.connect(segitiga)#ketika tombol di klik akan connect ke segitiga
    # Membuat Form Layout Dan Menambahkan widget
    layout = QVBoxLayout()
    layout1 = QGridLayout()
    layout1.addWidget(labelRusuk)
    layout1.addWidget(rusuk)
    layout2 = QGridLayout()
    layout2.addWidget(labelRusuk2)
    layout2.addWidget(rusuk2)
    layout.addLayout(layout1)
    layout.addLayout(layout2)
    layout.addWidget(btn)
    groupbox.setLayout(layout)
    return groupbox

def segitiga():
    try:
        vRusuk = rusuk.text()
        vRusuk2 = rusuk2.text()
        hDatar = (0.5*int(vRusuk) * int(vRusuk2))#rumus
        hasilDatar.setText(str(hDatar))
        rusuk.setText("")
        rusuk2.setText("")
    except ValueError:
        pass
    

def Tampil(window):
    groupbox = QGroupBox("Hasil Operasi", window)# Membuat Grupbox
    labelDatar = QLabel("Luas Segitiga: ")#membuat label dengan nama labeldatar
    global hasilDatar
    #widget inputan
    hasilDatar = QLineEdit()
    hasilDatar.setReadOnly(True)
    layout1 = QFormLayout()#membuat form
    layout1.addRow(labelDatar,hasilDatar)
    groupbox.setLayout(layout1)
    return groupbox

def window_go():#fungsi
    app = QApplication(sys.argv)#inisialisasi app dengan parameter sys.argv
    window = QWidget()
    GLayout = QGridLayout()#inisialisasi gridlayout
    # Menambahkan Widget GroupBox Ke gridLayout
    GLayout.addLayout(topLayout(window),0,0,1 ,2)#menambahkan layout toplayout ke window
    GLayout.addWidget(hitungSegitiga(window), 2, 0,1,0)#menambahkan widget hitung segitiga ke window
    GLayout.addWidget(Tampil(window), 4, 0,1,0)#mwnambahkan widget tampil
    window.setLayout(GLayout)#setting layout utama ke gridlayout
    window.setGeometry(100,100,100,100)#ukuran window
    window.setWindowTitle("PyQt5")#judul window
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    window_go()
