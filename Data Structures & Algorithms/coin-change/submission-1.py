class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #bfs

        queue = [(0,0)]
        least = -1
        seen = set()
        while len(queue) != 0:
            currAmount, coinCount = queue.pop(0)
            if currAmount in seen:
                continue
            if currAmount > amount:
                continue
            if currAmount == amount:
                return coinCount
            seen.add(currAmount)
            
            for coin in coins:
                queue.append((currAmount+coin, coinCount+1))
            
        return -1
