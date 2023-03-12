import pandas as pd 

data = pd.read_csv('data.csv')

data_jabatan = []

for index, karyawan in data.iterrows():
    if 8000000 <= karyawan['Gaji'] <= 9000000:
        karyawan['Jabatan'] = 'Officer'
    elif 10000000 <= karyawan['Gaji'] <= 11000000:
        karyawan['Jabatan'] = 'Supervisor'
    elif 12000000 <= karyawan['Gaji'] <= 14000000:
        karyawan['Jabatan'] = 'Asisten Manajer'
    elif karyawan['Gaji'] >= 15000000:
        karyawan['Jabatan'] = 'Manajer'
    else:
        karyawan['Jabatan'] = 'Tidak Ada'
    
    data_jabatan.append(karyawan['Jabatan'])

data['Jabatan'] = data_jabatan

print('\n<------------------------------------------------------------------------------>')
print(data)
print('<------------------------------------------------------------------------------>')

gaji_terbesar = None
gaji_terkecil = None

for index, karyawan in data.iterrows():
    if gaji_terbesar is None or gaji_terbesar < karyawan['Gaji']:
        gaji_terbesar = karyawan['Gaji']
    if gaji_terkecil is None or gaji_terkecil > karyawan['Gaji']:
        gaji_terkecil = karyawan['Gaji']

print('\n<-------------------------------->')
print(f' Gaji Terbesar = ', gaji_terbesar)
print(f' Gaji Terkecil = ', gaji_terkecil)
print('<-------------------------------->\n')