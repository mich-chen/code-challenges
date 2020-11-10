from typing import List

from collections import deque
def canReach(arr: List[int], start: int) -> bool:

    q = deque([start])

    while q:
        idx = q.popleft()
        if arr[idx] < 0:
            continue
        if arr[idx] == 0:
            return True
        else:
            # mark as seen
            arr[idx] = -arr[idx]
            # add to queue if new index is within bounds
            q.append(idx + arr[idx]) if 0 <= (idx + arr[idx]) < len(arr) else None
            q.append(idx - arr[idx]) if 0 <= (idx - arr[idx]) < len(arr) else None

    return False


if __name__ == '__main__':
    
    print(canReach([4,2,3,0,3,1,2], 5))  # True
    print(canReach([4,2,3,0,3,1,2], 0))  # True
    print(canReach([3,0,2,1,2], 2))  # False
    