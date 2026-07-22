class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([tweetId, self.time])
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        users=list(self.following[userId])
        users.append(userId)
        pq=[]
        for user in users:
            for tweetid, time in self.tweets[user]:
                heappush(pq, (-time, tweetid))

        ans=[]
        while pq:
            _ , ele=heappop(pq)
            ans.append(ele)
            if len(ans)==10:
                break
        return ans 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)