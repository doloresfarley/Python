phone_number = int(input())

# Use % to get the desired rightmost digits. Ex: The rightmost 2 digits of 572 is gotten by 572 % 100, which is 72.
lower = phone_number % 10000000
high_lower = lower // 10000
low_lower = lower % 10000
print(lower)
print(high_lower)
print(low_lower)
#Hint: Use // to shift right by the desired amount.
# Ex: Shifting 572 right by 2 digits is done by 572 // 100,
# which yields 5. (Recall integer division discards the fraction).
higher = phone_number // 10000000
print(higher)

print(f'({higher}) {high_lower}-{low_lower}')