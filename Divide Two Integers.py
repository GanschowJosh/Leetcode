class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for the problem constraints
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Compute the sign of the result
        sign = 1 if (dividend > 0) == (divisor > 0) else -1

        # Take the absolute values
        dividend, divisor = abs(dividend), abs(divisor)

        # Result starts from 0
        quotient = 0

        # While the dividend is greater or equal to the divisor
        while dividend >= divisor:
            # Start from a divisor and a multiple of 1
            current_divisor, multiple = divisor, 1

            # While the dividend is greater or equal to the current divisor
            while dividend >= current_divisor:
                # Subtract the current divisor from the dividend
                dividend -= current_divisor

                # Add the current multiple to the quotient
                quotient += multiple

                # Double the current divisor and its multiple
                current_divisor <<= 1
                multiple <<= 1

        # Return the final quotient, with the correct sign
        return sign * quotient
