if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    Snd_Max=0
    max_value=max(arr)
    for i in range(len(arr)-1):    
       if int(arr[i])>Snd_Max and arr[i]!=max_value:
           Snd_Max=arr[i]

          
           
    print(Snd_Max)