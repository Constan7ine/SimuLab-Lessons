# coding=utf-8

madlib_template = """I enjoy long, {0} walks on the beach, getting {1} in the rain and serendipitous encounters with {2}.
I really like pina coladas mixed with {3}, and romantic, candle-lit {4}.
I am looking for {5} and beauty in the form of a {6} goddess.
I would prefer if she knew how to cook, clean, and wash my {7}."""

def GetWord(prompt, completion):
	word = raw_input(prompt)
	print("You are {}% complete!".format(completion/8.0*100.0))
	return word

adjective = GetWord("Adjective: ", 1)
verb = GetWord("Verb Ending in 'ed': ", 2)
pluralNoun1 = GetWord("Plural Noun: ", 3)
liquid = GetWord("Liquid: ", 4)
pluralNoun2 = GetWord("Plural Noun: ", 5)
noun = GetWord("Noun: ", 6)
nationality = GetWord("Nationality: ", 7)
pluralNoun3 = GetWord("Plural Noun: ", 8)

print(madlib_template.format(adjective, verb, pluralNoun1, liquid, pluralNoun2, noun, nationality, pluralNoun3))

