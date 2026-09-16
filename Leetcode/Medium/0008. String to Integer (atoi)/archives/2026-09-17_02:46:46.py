class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Ignore leading whitespaces
        position = 0
        while position < len(s) and s[position] == " ":
            position += 1

        # 2. Determine signedness
        sign = 1
        if position < len(s) and s[position] == "-":
            sign *= -1
            position += 1
        elif position < len(s) and s[position] == "+":
            position += 1

        # 3. Read actual digits
        number = 0
        while position < len(s) and s[position].isdigit():
            number = number * 10 + int(s[position])
            position += 1

        # 4. Apply sign
        final = number * sign

        # 5. Apply range
        if final > 2147483647:
            final = 2147483647
        elif final < -2147483648:
            final = -2147483648

        return final