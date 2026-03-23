"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "hyped",
    "lit",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "overwhelming",
    "worst",
    "nervous",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "Highkey hyped for the concert tonight 🤩",
    "No cap, this is the worst movie I've ever seen 😭",
    "Tonight is about to be lit 🔥🔥🔥",
    "I absolutely love getting stuck in traffic 🙃",
    "so done with this week, can't wait for it to be over 😩",
    "Im so happy",
    "im so sad",
    "That exam was overwhelming",
    "I feel happy and excited today",
    "I feel sad and tired today",
    "I absolutely love waiting in long lines 🙃",
    "I am okay, nothing special",
    "I am stressed but still hopeful",
    "im lowkey nervous",

]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "positive",  # "Highkey hyped for the concert tonight 🤩"
    "negative",  # "No cap, this is the worst movie I've ever seen 😭"
    "positive",  # "Tonight is about to be lit 🔥🔥🔥"
    "negative",  # "I absolutely love getting stuck in traffic 🙃"
    "negative",  # "so done with this week, can't wait for it to be over 😩"
    "positive",  # "Im so happy"
    "negative",  # "im so sad"
    "negative",  # "That exam was overwhelming"
    "positive",  # "I feel happy and excited today"
    "negative",  # "I feel sad and tired today"
    "negative",  # "I absolutely love waiting in long lines 🙃"
    "neutral",   # "I am okay, nothing special"
    "mixed",     # "I am stressed but still hopeful"
    "negative",  # "im lowkey nervous"
]
# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
