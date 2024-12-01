file = open("./input.txt","r");
nums1 = []
nums2 = []
for line in file:
    line = line.split("   ")
    nums1.append(line[0])
    nums2.append(line[1])
if len(nums1) != len(nums2):
    print("he?")
else:
    nums1.sort()
    nums2.sort()
    sum=0
    for x in range(nums1.__len__()):
        a = abs(int(nums1[x])-int(nums2[x]))
        sum+=a
    print("wynik: ",sum)

