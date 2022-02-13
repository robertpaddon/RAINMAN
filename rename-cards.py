import os
files = ['cards-dataset/' + f for f in os.listdir('cards-dataset')]

#print(files)

kinds = {
	"ace": 'A',
	"2": '2',
	"3": '3',
	"4": '4',
	"5": '5',
	"6": '6',
	"7": '7',
	"8": '8',
	"9": '9',
	"10": '10',
	"jack": 'J',
	"queen": 'Q',
	"king": 'K',
}


suites = {
	"clubs": 'c',
	"hearts": 'h',
	"diamonds": 'd',
	"spades": 's',
}


for file in files:
	#print(file)
	kind = file.split('_')
	kind = kind[0]
	kind = kind.split('/')[1]
	kind = kinds[kind]

	suite = file.split('_')
	suite = suite[2]
	suite = suite.split('.')[0]
	suite = suites[suite]

	newfile = 'updated-cards/' + kind + suite +'.png'

	command = 'cp ' + file + ' ' + newfile
	os.system(command)



