# input bilangan yang akan dicari faktornya
bilangan = int(input("Masukan bilangan: "))
# mendefinisikan fungsi
def faktor(x):
# fungsi menerima hasil inputan dan mencetak hasil faktornya
    print("faktor dari",x,"Adalah: ")
    for A in range(1, x+1):
        if x % A == 0:
            print (A)
# memangil fungsi
faktor(bilangan)