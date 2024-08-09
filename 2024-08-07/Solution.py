class Solution:
    def numberToWords(self, num: int) -> str:
        lessthan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def converter(n):
            if n == 0:
                return ""
            elif n < 20:
                return lessthan20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + converter(n % 10)
            else:
                return lessthan20[n // 100] + " Hundred " + converter(n % 100)

        def numbertoword(num):
            if num == 0:
                return "Zero"
            
            res = ""
            for i in range(len(thousands)):
                if num % 1000 != 0:
                    res = converter(num % 1000) + thousands[i] + " " + res
                num //= 1000
            
            return res.strip()

        return numbertoword(num)