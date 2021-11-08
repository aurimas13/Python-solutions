# Solution of Exercise 40 - Exercise_40.py
#
# Uploaded by Aurimas A. Nausedas on 11/23/20.
# Updated by Aurimas A. Nausedas on 11/06/21.

class Song(object):

	def __init__(self, lyrics, anthem):
		self.lyrics = lyrics
		self.anthem = anthem

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def anthem_no_idea(self):
		for value in self.anthem:
			print "And the country is: " + value

happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"], "Poland")

bulls_on_parade = Song(["They rally around the family",
				 "With rockets full of shells"], "India")

whatever = Song(["Try to understand",
				 "Self, lyrics, self, lyrics",
				 "I think I get it. Do I?",
				 "I think I do!"], "Croatia")

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

whatever.sing_me_a_song()

Song(["Nothing"], ["Lithuania"]).anthem_no_idea()
