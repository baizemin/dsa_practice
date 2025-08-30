def tower_of_hanoi(source,aux,dest,n):
    if n==1:
        print(f"move disk 1 from {source} to {dest}")
        return
    tower_of_hanoi(source,dest,aux,n-1)
    print(f"move disk {n} from {source} to {dest}")
    tower_of_hanoi(aux,source,dest,n-1)
n = 3
tower_of_hanoi("a","b","c",3)