class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = []

        for x in nums:
            temp = ""
            for n in str(x):
                temp += str(mapping[int(n)])
            mapped.append(int(temp))
        
        return [p[0] for p in sorted(zip(nums,mapped), key=lambda x: x[1])]