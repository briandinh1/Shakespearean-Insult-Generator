import sys
import random
from Tkinter import *


prefix = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish', 'cockered',
          'clouted', 'craven', 'currish', 'dankish', 'dissembling', 'droning',
          'errant', 'fawning', 'fobbing', 'froward', 'frothy', 'gleeking', 'goatish',
          'gorbellied', 'impertinent', 'infectious', 'jarring', 'loggerheaded', 'lumpish',
          'mammering', 'mangled', 'mewling', 'paunchy', 'pribbling', 'puking', 'puny',
          'qualling', 'rank', 'reeky', 'roguish', 'ruttish', 'saucy', 'spleeny',
          'spongy', 'surly', 'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous',
          'warped', 'wayward', 'weedy', 'yeasty', 'cullionly', 'fusty', 'caluminous',
          'wimpled', 'burly-boned', 'misbegotten', 'odiferous', 'poisonous', 'fishified',
          'wart-necked', 'cavernous', 'vile', 'sour', 'nippy']

middle = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed', 'boil-brained',
          'clapper-clawed', 'clay-brained', 'common-kissing', 'crook-pated',
          'dismal-dreaming', 'dizzy-eyed', 'doghearted', 'dread-bolted', 'earth-vexing',
          'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed', 'fly-bitten',
          'folly-fallen', 'fool-born', 'full-gorged', 'guts-griping', 'half-faced',
          'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed', 'ill-breeding',
          'ill-nurtured', 'knotty-pated', 'milk-livered', 'motley-minded', 'onion-eyed',
          'plume-plucked', 'pottle-deep', 'pox-marked', 'reeling-ripe', 'rough-hewn',
          'rude-growing', 'rump-fed', 'shard-borne', 'sheep-biting', 'spur-galled',
          'swag-bellied', 'tardy-gatied', 'tickle-brained', 'toad-spotted', 'unchin-snouted',
          'weather-bitten', 'whoreson', 'malmsey-nosed', 'rampallian', 'lily-livered',
          'scurvy-valiant', 'brazen-faced', 'unwash\'d', 'bunch-back\'d', 'leaden-footed',
          'muddy-mettled', 'pigeon-liver\'d', 'scale-sided', 'lard-bloated', 'dank',
          'ale-soused', 'bald-arsed', 'hollow-mouthed', 'gouty-legged', 'copper-nosed',
          'long-nosed']

suffix = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig', 'bugbear', 'bum-bailey',
          'canker-blossom', 'clack-dish', 'clotpole', 'coxcomb', 'codpiece', 'death-token',
          'dewberry', 'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker', 'fustilarian',
          'giglet', 'gudgeon', 'haggard', 'harpy', 'hedge-pig', 'horn-beast', 'hugger-mugger',
          'joithead', 'lewdster', 'lout', 'maggot-pie', 'malt-worm', 'mammet', 'measle',
          'minnow', 'miscreant', 'moldwarp', 'mumble-news', 'nut-hook', 'pigeon-egg',
          'pignut', 'puttok', 'pumpion', 'ratsbane', 'scut', 'skainsmate', 'strumpet',
          'varlot', 'vassal', 'whey-face', 'wagtail', 'knave', 'blind-worm', 'popinjay',
          'scullian', 'jolt-head', 'malcontent', 'devil-monk', 'toad', 'rascal', 
          'basket-cockle', 'tooth-hole', 'strumpet', 'ninnycock', 'polecat', 'cucumber',
          'tarse', 'wittol', 'rascal', 'bull-head', 'reprobate']


class Generator:
    def __init__(self):
        self.root = Tk()
        self.root.title('Shakespearean Insult Generator - Brian Dinh')
        self.root.minsize(width=500, height=180)
        self.root.maxsize(width=500, height=180)
        self.textBox = Label(self.root, bg="white", height=5, width=50, justify=CENTER, relief=SUNKEN)
        self.textBox.pack(side=TOP, pady=10)
        self.generateButton = Button(self.root, text='Generate Text', height=2, width=15, command=self.generateText)
        self.generateButton.pack(side=BOTTOM, pady=10)

    def runGUI(self):
        self.root.mainloop()

    def generateText(self):
        chance = random.randint(0,100)
        if chance > 5:  
            self.textBox.configure(text=self.generate())
        else:
            self.textBox.configure(text=self.surprise())

    def generate(self):
        return 'Thou ' + random.choice(prefix) + ' ' + random.choice(middle) + ' ' + random.choice(suffix)
        
    
    def surprise(self):
        return 'Thou art a nice person' 
        
        


def main():
    generator = Generator()
    generator.runGUI()



if __name__ == "__main__":
    main()
