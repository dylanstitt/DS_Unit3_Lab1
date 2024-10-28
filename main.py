# Dylan Stitt
# Unit 3 Lab 1
# While vs. Recursion

def sample(num):
    if num == 0:
        print("\nBASE CASE REACHED\n")
        return

    print(f"Recursing; num = {num}")
    sample(num-1)
    print(f"Returning; num = {num}")
    return

def whileSubstitute(num):
    nums = []
    while num != 0:
        print(f"Recursing (While); num = {num}")
        nums.append(num)
        num -= 1

    print("\nBASE CASE REACHED\n")
    count = len(nums)-1
    while count >= 0:
      print(f"Returning; num = {nums[count]}")
      count -= 1

def main():
    sample(5)
    print()
    whileSubstitute(5)


if __name__ == '__main__':
    main()
