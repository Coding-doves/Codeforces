# Number of test cases to run
archery = int(input())
resp = []
# Loop to receive n Number of test cases
for num in range(archery):
    # Targets and number of times to query target list
    target, query = input().split(" ")
    
    # Receive target list of test cases
    target_list = input().split(" ")
    if len(target_list) != int(target):
        print(f"Enter {target} numbers")

    # Loop through n number of queries checking if sheriff have a winning or tie chance
    for _ in range(int(query)):
        l, r = input().split(" ")
        # Subset target_list based on query
        nums = sorted(target_list[int(l) - 1:int(r)], reverse=True)

        # Check Sheriff chances of winning/tie
        robin = 0
        sheriff = 0
        # Loop through test case/subset list
        for n in range(len(nums)):
            if n % 2 == 0:
                robin += int(nums[n])
            else:
                sheriff += int(nums[n])

        resp.append("NO" if robin > sheriff else "YES")

for r in resp:
    print(r)
