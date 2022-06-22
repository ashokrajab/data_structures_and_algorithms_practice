nums1 = [1,2,3]
nums2 = [2,5,6]

m = 3
n = 3

last_insert = 0
nums1 = nums1[:m]
for i in range(0,n):
	has_inserted = False
	for j in range(last_insert, len(nums1)):
		if nums2[i]<=nums1[j]:
			nums1.insert(j, nums2[i])
			last_insert = j
			has_inserted = True
			break
	if not has_inserted:
		nums1.append(nums2[i])
		last_insert = len(nums1)-1

print(nums1)  