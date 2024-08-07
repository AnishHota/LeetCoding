class Solution:
    def numberToWords(self, num: int) -> str:
        d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }
        n = len(str(num))
        nu = str(num)
        tri = []
        temp = ""
        for i in range(n-1,-1,-1):
            temp += nu[i]
            temp_lis = []
            if len(temp)==3:
                temp = temp[::-1]
                if int(temp[0])!=0:
                    temp_lis.append(d[int(temp[0])] + " " +d[100])
                if int(temp[1:]) in d and int(temp[1:])!=0:
                    temp_lis.append(d[int(temp[1:])])
                else:
                    if int(temp[1])!=0:
                        temp_lis.append(d[int(temp[1]+'0')])
                    if int(temp[2])!=0:
                        temp_lis.append(d[int(temp[2])])
                tri.append(" ".join(temp_lis))
                temp = ""
        
        if temp!="":
            temp = temp[::-1]
            temp_lis = []
            if int(temp) in d:
                temp_lis.append(d[int(temp)])
            elif len(temp)==2:
                temp_lis.append(d[int(temp[0]+'0')])
                temp_lis.append(d[int(temp[1])])
            else:
                temp_lis.append(d[int(temp[0])])
            
            tri.append(" ".join(temp_lis))
        
        k = len(tri)
        ans = ""
        while tri:
            temp = tri.pop()
            temp = temp.strip()
            if temp!="":
                if k==4:
                    temp += " "+"Billion"
                elif k==3:
                    temp += " "+"Million"
                elif k==2:
                    temp += " "+"Thousand"
                ans = ans.strip()+" "+temp.strip()
            k-=1

        return ans.strip()




