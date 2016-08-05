(ns wordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn wordcount [options]
   [
    ;; spout configuration
    {"tweet-spout" (python-spout-spec
          options
          "spouts.tweets.Tweets"
          ["tweet"]
          )
    }
    ;; bolt configuration
    {"parse-bolt" (python-bolt-spec
          options
          {"tweet-spout" :shuffle}
          "bolts.parse.ParseTweet"
          ["word"]
          :p 2)
     "count-bolt" (python-bolt-spec
          options
          {"parse-bolt" :shuffle}
          "bolts.wordcount.WordCounter"
          ["word" "count"]
          :p 2)
    }
  ]
)

