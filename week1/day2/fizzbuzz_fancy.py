#!/usr/bin/python

def fizzbuzz(num_range, terms):
	for i in num_range:
		out_sound = []
		for div, sound in terms.items():
			if i%div==0:
				out_sound.append(sound)
		if len(out_sound) > 0:
			print(''.join(out_sound))
		else:
			print(i)


fizzbuzz(range(101), {3: 'Fizz', 5:'Buzz', 7:'Bam', 11:'Whack'})

