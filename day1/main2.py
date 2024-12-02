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
    max = 0;
    if int(nums1[nums1.__len__()-1]) > int(nums2[nums2.__len__()-1]):
        max = nums1[nums1.__len__()-1]
    else:
        max = nums2[nums2.__len__()-1]
    max = int(max)
    nums3 = [0]*max*2
    nums4 = [0]*max*2
    print(nums3.__len__())
    for x in nums1:
        x = int(x)
        nums3[x]+=1
    for x in nums2:
        x = int(x)
        nums4[x]+=1

    sum=0
    for x in range(nums3.__len__()):
        sum+= x*nums3[x]*nums4[x]
    print("Wynik: ",sum)

