#TUGAS 2 KELOMPOK
array=[]
total=0
n=int(input("masukkan banyak nilai : "))
for x in range(0,n):
      nilai=float(input("masukkan nilai ke-{} : ".format (x+1)))
      array.append(nilai)
print(f'list array = {array}')
for x in range(0,n):         
    nilai=int(input("tambahkan nilai: ".format(x+1)))
    array.append(nilai)
    print(array)
print()
print('list akhir: ')
print(array)
akhir=array
def remove(akhir,i):
        first=akhir[:i]
        last=akhir[i+1:]
        return first+last
i=int(input("\nMasukkan index yang ingin dihapus: "))
result=remove(akhir,i)
t=remove(akhir,i)
print("\nSetelah index",i, "dihapus : ")
print (t)
p=int(input("\nMasukkan index yang ingin dicari: "))
k=t
print("\nIndex",p,"menunjukkan",k[p])










   
