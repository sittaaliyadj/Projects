# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
print()
print('===============================================')
print('                 Linear Search                 ')
print('===============================================')
def binary():
    arr=[]
    list_cnt=input("Berapa Banyak Data Yang Diinput : ")
    print()
    for i in range(int(list_cnt)):
        ### need to convert the value returned by input()
        arr.append(input("Masukkan Data Ke-" +str(i+1)+" : "))
        ##here we are using append method of list

    print()
    print("Data Awal : ")
    print(arr)
    print()
    x=input('Data yang ingin dicari : ')
    def binary_search(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0
            while low <= high:
                    mid = (high + low) // 2
                    # If x is greater, ignore left half
                    if arr[mid] < x:
                            low = mid + 1
                    # If x is smaller, ignore right half
                    elif arr[mid] > x:
                            high = mid - 1
                    # means x is present at mid
                    else:
                            return mid
           # If we reach here, then the element was not present
            return -1

    # Function call
    result = binary_search(arr, x)

    if result != -1:
            print("Elemen ditemukan di index ke-", str(result))
    else:
            print("Elemen tidak ditemukan")

    x=(int(input("\nApakah ingin mengulangi program? (1.YA/2.TIDAK) : ")))
    while x==1:
        binary()
        x=(int(input("Apakah ingin mengulangi program? (1.YA/2.TIDAK) : ")))
    else:
        print("Terima kasih")
binary()	

