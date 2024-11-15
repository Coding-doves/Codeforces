# Number of test cases to run
archery = int(input())
resp = []

# Loop to receive n Number of test cases
for num in range(archery):
    # Targets and number of times to query target list
    target, query = map(int, input().split())
    
    # Receive target list of test cases once
    target_list = list(map(int, input().split())) # Convert to integer

    for _ in range(query):
        l, r = map(int, input().split())

        query_size, score = len(target_list[l - 1: r]), sum(target_list[l - 1: r])
        if query_size % 2 != 0:
            if query_size == 1:
                robin_score = target_list[l - 1]
                sheriff_score = 0
            else:
                if score % 2 != 0:
                    robin_score = (score + 1) // 2
                    sheriff_score = robin_score - 1
                else:
                    robin_score = score // 2
                    sheriff_score = robin_score
        else:
            if score % 2 != 0:
                robin_score = (score + 1) // 2
                sheriff_score = robin_score - 1
            else:
                robin_score = score // 2
                sheriff_score = robin_score

        resp.append("NO" if robin_score > sheriff_score else "YES")
    
for r in resp:
    print(r)
