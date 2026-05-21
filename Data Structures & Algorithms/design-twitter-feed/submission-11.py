class Twitter:

    def __init__(self):
        self.user_id_follower_map = {}
        self.user_id_tweet_map = {}
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.user_id_tweet_map:
            self.user_id_tweet_map[userId].append((self.counter, tweetId))
        else:
            self.user_id_tweet_map[userId] = [(self.counter, tweetId)]
            self.user_id_follower_map[userId] = set([userId])
        self.counter = self.counter+1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_id_follower_map:
            return []
        q = []
        followers = self.user_id_follower_map[userId]
        for follower in followers:
            tweetIds = self.user_id_tweet_map[follower]
            for tweetid in tweetIds:
                heapq.heappush(q, (tweetid[0], tweetid[1], follower))
                if len(q) > 10:
                    heapq.heappop(q)
        answer = []
        while q:
            answer.append(heapq.heappop(q)[1])
        answer.reverse()
        return answer

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId :
            return 
        if followerId in self.user_id_follower_map:
            self.user_id_follower_map[followerId].add(followeeId)
        else:
            self.user_id_follower_map[followerId] = set([followeeId])

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId :
            return 
        if followerId in self.user_id_follower_map:
            if followeeId in self.user_id_follower_map[followerId]:
                self.user_id_follower_map[followerId].remove(followeeId)                

        
# {userid (1) : all the tweets 10, 30 etc.}
# userId (1): follows xyz
# userid(2): follows abc

# getNewsFeed(2):
# abc
# for a b c, get all tweets, put them into pq of len 10
# return pq
