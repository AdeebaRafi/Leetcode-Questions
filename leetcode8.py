class Solution:
    def myAtoi(self, s):

        # Step 1: Remove leading whitespaces
        number = s.strip()

        # Step 2: Handle sign
        positive = True
        if number.startswith('-'):
            positive = False
            number = number[1:]  # Remove the negative sign
        elif number.startswith('+'):
            number = number[1:]  # Remove the positive sign

        # Step 3: Remove leading zeros
        number = number.lstrip('0')

        # Step 4: Extract valid digits
        valid_digits = ""
        for char in number:
            if char.isdigit():
                valid_digits += char
            else:
                break

        # Step 5: Handle empty or invalid input
        if not valid_digits:
            return 0  # No valid number to process

        # Step 6: Convert to integer
        result = int(valid_digits)
        if not positive:
            result = -result  # Apply negative sign

        # Step 7: Clamp to 32-bit range
        return self.round_to_32_bit(result)

    def round_to_32_bit(self, num):
        # Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num