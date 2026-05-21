# {userid (1) : all the tweets 10, 30 etc.}
# userId (1): follows xyz
# userid(2): follows abc

# getNewsFeed(2):
# abc
# for a b c, get all tweets, put them into pq of len 10
# return pq

class Twitter:

    def __init__(self):
        # Maps userId to set of users they follow (including themselves)
        self.user_id_follower_map = {}
        # Maps userId to list of (timestamp, tweetId) tuples
        self.user_id_tweet_map = {}
        # Global counter to track tweet recency (higher = more recent)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add tweet with current counter as timestamp
        if userId in self.user_id_tweet_map:
            self.user_id_tweet_map[userId].append((self.counter, tweetId))
        else:
            # First time user posts: initialize both tweet map and follower map
            self.user_id_tweet_map[userId] = [(self.counter, tweetId)]
            # Users always follow themselves so they see their own tweets
            self.user_id_follower_map[userId] = set([userId])
        # Increment counter for next tweet (more recent tweets have higher counter)
        self.counter = self.counter + 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # If user doesn't exist, return empty feed
        if userId not in self.user_id_follower_map:
            return []
        
        # Min heap to track the 10 most recent tweets
        # Heap elements: (timestamp, tweetId, userId)
        q = []
        
        # Get all users this person follows (includes themselves)
        followers = self.user_id_follower_map[userId]
        
        # Add ALL tweets from all followed users to the heap
        for follower in followers:
            # Get tweets from this followed user
            if follower in self.user_id_tweet_map:
                tweetIds = self.user_id_tweet_map[follower]
                for tweetid in tweetIds:
                    # Push (timestamp, tweetId, userId) to heap
                    heapq.heappush(q, (tweetid[0], tweetid[1], follower))
                    # Keep heap size <= 10 by removing smallest (oldest) tweet
                    if len(q) > 10:
                        heapq.heappop(q)
        
        # Extract tweets from heap and reverse to get most recent first
        answer = []
        while q:
            # Pop tuple and get tweetId (index 1)
            answer.append(heapq.heappop(q)[1])
        # Min heap pops smallest first, so reverse to get most recent
        answer.reverse()
        return answer

    def follow(self, followerId: int, followeeId: int) -> None:
        # Can't follow yourself (no-op)
        if followerId == followeeId:
            return 
        
        # Add followee to follower's follow set
        if followerId in self.user_id_follower_map:
            self.user_id_follower_map[followerId].add(followeeId)
        else:
            # First time follower is following someone: create their follow set
            self.user_id_follower_map[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Can't unfollow yourself (no-op)
        if followerId == followeeId:
            return 
        
        # Remove followee from follower's follow set if they exist
        if followerId in self.user_id_follower_map:
            if followeeId in self.user_id_follower_map[followerId]:
                self.user_id_follower_map[followerId].remove(followeeId)