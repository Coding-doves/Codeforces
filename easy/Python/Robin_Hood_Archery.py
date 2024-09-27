# Number of test cases to run
archery = int(input())
resp = []

# Loop to receive n Number of test cases
for num in range(archery):
    # Targets and number of times to query target list
    target, query = input().split(" ")
    target, query = int(target), int(query)
    
    # Receive target list of test cases
    target_list = list(map(int, input().split(" "))) # Convert to integer
    if len(target_list) != target:
        print(f"Enter {target} numbers")
        continue

    # Loop through n number of queries checking if sheriff have a winning or tie chance
    for _ in range(query):
        l, r = input().split(" ")
        l, r = int(l), int(r)

        # Check if the query range is valid
        if l < 1 or r > len(target_list):
            print("Invalid query range")
            continue  # Skip this query if the range is invalid

        # Subset target_list based on query
        nums = sorted(target_list[l - 1:r], reverse=True)

        # Check Sheriff chances of winning/tie
        robin = 0
        sheriff = 0
        # Loop through test case/subset list
        for n in range(len(nums)):
            if n % 2 == 0:
                robin += nums[n]
            else:
                sheriff += nums[n]

        resp.append("NO" if robin > sheriff else "YES")

for r in resp:
    print(r)
