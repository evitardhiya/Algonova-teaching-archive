from time import sleep

print('Selamat datang di Quiz Game!')
print('Ayo jawab pertanyaan dan lihat apakah kamu berhasil lolos!')
print("✅ Benar: +10 poin | ❌ Salah: -10 poin")
print('READY?')
sleep(2)
print('GOOO!!\n')

# Daftar pertanyaan dan jawaban
pertanyaan_list = [
    {"soal": "Apa ibukota dari Jepang?",
        "opsi": "A. Kyoto\nB. Tokyo\nC. Osaka\nD. Nagoya",
        "jawaban": "b"},
    {"soal": "Makanan favorit kelinci?",
        "opsi": "A. Wortel\nB. Daging\nC. Ikan\nD. Pepaya",
        "jawaban": "a"},
    {"soal": "Hewan apa yang jalannya paling lambat?",
        "opsi": "A. Kucing\nB. Kuda\nC. Siput\nD. Ayam",
        "jawaban": "c"},
    {"soal": "Apa warna langit saat siang hari?",
        "opsi": "A. Kuning\nB. Merah\nC. Biru\nD. Ungu",
        "jawaban": "c"},
    {"soal": "Apa yang bisa terbang tanpa sayap?",
        "opsi": "A. Angin\nB. Kucing\nC. Pisang\nD. Ikan",
        "jawaban": "a"},
    {"soal": "Kalau kamu bawa es krim ke matahari, apa yang terjadi?",
        "opsi": "A. Jadi batu\nB. Tetap dingin\nC. Meleleh\nD. Membeku",
        "jawaban": "c"},
    {"soal": "Kucing biasanya bersuara apa?",
        "opsi": "A. Kukuruyuk\nB. Guk guk\nC. Meong\nD. Moo",
        "jawaban": "c"},
    {"soal": "Kalau kamu ketawa terus, kamu jadi...",
        "opsi": "A. Menangis\nB. Ketawa\nC. Ngambek\nD. Marah",
        "jawaban": "b"}]

point = 0

# Gunakan loop untuk menampilkan pertanyaan
for i, soal in enumerate(pertanyaan_list, start=1):
    print(i, soal['soal'])
    print(soal['opsi'])
    jawaban = input('Jawabanmu: ').lower()
    if jawaban == soal['jawaban']:
        print("Benar!")
        point += 10
    else:
        print("Salah!")
        point -= 10
    print("Point kamu saat ini:", point, '\n')

# Hasil akhir
print("Permainan selesai! Total poin kamu adalah:", point)
if point >= 70:
    print("Keren sekali!!")
elif point >= 30:
    print("Welll, cukup bagusss")
else:
    print("Yahh, coba lagi yaa!!")