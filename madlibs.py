# String Concatenation

# youtube_link = "https://github.com/gurucl"


# print("Please subscribe to " + youtube_link )

# print("Please subscribe to {}".format(youtube_link) )

# print(f"Please subscribe to {youtube_link}"  )

name = input("name: ")
technology = input("technology: ")
year = input("year: ")
creator = input("creator: ")
feel = input("feel: ")

madlib = f"I'm {name}, I learnt {technology} in the year {year} which is created by {creator}. \
Thanks to {creator} you made my career and life and my thoughts. I feel {feel}"

print(madlib)