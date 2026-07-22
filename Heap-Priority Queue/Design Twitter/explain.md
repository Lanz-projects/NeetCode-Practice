# Design Twitter

## 🔍 Problem Summary

Design a simplified version of Twitter that supports posting tweets, following and unfollowing users, and retrieving the 10 most recent tweets visible to a user.

A user's news feed should include tweets from themselves and everyone they follow, ordered from most recent to least recent. The main challenge is efficiently merging tweets from multiple users without repeatedly sorting every tweet in the system.

---

## 🧠 Key Insight

Each user's tweets are already stored in chronological order, so we only need to merge the most recent tweets from each followed user.

A heap makes this efficient by always selecting the newest available tweet. Whenever a tweet is removed from the heap, the next most recent tweet from that same user is added, allowing us to merge multiple tweet lists without sorting them all together.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Gather every tweet from the user and all followed users into one list.
- Sort the combined list by timestamp and return the 10 most recent tweets.
- This repeatedly sorts large collections of tweets, making news feed retrieval inefficient.

### 2. Better Approach

- Store each user's tweets in chronological order along with a timestamp.
- Keep a mapping of which users each person follows.
- When retrieving the news feed, ensure the user follows themselves so their own tweets are included.
- Insert the most recent tweet from each followed user into a heap.
- Repeatedly remove the newest tweet from the heap and add its ID to the result.
- If that user has older tweets remaining, insert the next most recent one into the heap.
- Continue until 10 tweets have been collected or no tweets remain.

This approach performs a k-way merge of multiple sorted tweet lists, allowing the newest tweets to be retrieved without sorting every available tweet. Posting, following, and unfollowing all run in **O(1)** time. Retrieving the news feed takes **O((F + 10) log F)** time, where `F` is the number of followed users, and uses **O(F)** additional space for the heap.

---

## 🧪 Final Code (Python)

```python
class Twitter(object):

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        minHeap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)
```
