pages = [1,11,12,13,14,15,37,38,70]
# 1, 11-15, 37-38, 70

result = ""
i = 0
while i < len(pages)-1:
    print(i)
    if pages[i]+1 == pages[i+1]:
        j = i
        result += f"{pages[i]}"
        while j < len(pages):
            print(j)
            if pages[j] +1 == pages[j+1]:
                j += 1
            else:
                result += f"-{pages[j]},"
                break
        i = j 
    else:
        result += f"{pages[i]}, "
    i += 1
result += f"{pages[i]}, "
print(result)