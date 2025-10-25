class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([tweetId, self.time])
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        ans=[]
        ind=[]
        pq=[]
        for i in self.following[userId]:
            ind.append([i, len(self.tweets[i])-1])
        ind.append([userId, len(self.tweets[userId])-1])
        for i in range(len(ind)):
            user=ind[i][0]
            last=ind[i][1]
            for ele in self.tweets[user]:
                heappush(pq, [-ele[1], ele[0]])
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