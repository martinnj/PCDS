import string
import random

# Settings for generation
lengthOfSkillGeneration = 20
LengthOfLanguageGeneration = 3

#skillsList = [("Programming", 2), ("SQL", 3), ("Databases", 4), ("Database Design", 6), ("Software Design", 7), ("Computer Science", 9), ("Software Development", 33), ("Java", 34), ("Eclipse", 35), ("Erlang", 36), ("SML", 37), ("Tcl-Td", 38), ("Data Warehousing", 39), ("Oracle Warehouse Bildeid", 40), ("Toad", 41), ("XML", 42), ("Arch Linux", 44), ("Haskell", 46), ("Matlab", 47), ("C", 49), ("Algorithms", 50), ("Distributed Systems", 52), ("Object Oriented Dsigid", 53),("LaTeX",5)]
arrBad = ['2g1c', '2 girls 1 cup', 'acrotomophilia', 'anal', 'anilingus', 'anus', 'arsehole', 'ass', 'asshole', 'assmunch', 'auto erotic', 'autoerotic', 'babeland', 'baby batter', 'ball gag', 'ball gravy', 'ball kicking', 'ball licking', 'ball sack', 'ball sucking', 'bangbros', 'bareback', 'barely legal', 'barenaked', 'bastardo', 'bastinado', 'bbw', 'bdsm', 'beaver cleaver', 'beaver lips', 'bestiality', 'bi curious', 'big black', 'big breasts', 'big knockers', 'big tits', 'bimbos', 'birdlock', 'bitch', 'black cock', 'blonde action', 'blonde on blonde action', 'blow j', 'blow your l', 'blue waffle', 'blumpkin', 'bollocks', 'bondage', 'boner', 'boob', 'boobs', 'booty call', 'brown showers', 'brunette action', 'bukkake', 'bulldyke', 'bullet vibe', 'bung hole', 'bunghole', 'busty', 'butt', 'buttcheeks', 'butthole', 'camel toe', 'camgirl', 'camslut', 'camwhore', 'carpet muncher', 'carpetmuncher', 'chocolate rosebuds', 'circlejerk', 'cleveland steamer', 'clit', 'clitoris', 'clover clamps', 'clusterfuck', 'cock', 'cocks', 'coprolagnia', 'coprophilia', 'cornhole', 'cum', 'cumming', 'cunnilingus', 'cunt', 'darkie', 'date rape', 'daterape', 'deep throat', 'deepthroat', 'dick', 'dildo', 'dirty pillows', 'dirty sanchez', 'dog style', 'doggie style', 'doggiestyle', 'doggy style', 'doggystyle', 'dolcett', 'domination', 'dominatrix', 'dommes', 'donkey punch', 'double dong', 'double penetration', 'dp action', 'eat my ass', 'ecchi', 'ejaculation', 'erotic', 'erotism', 'escort', 'ethical slut', 'eunuch', 'faggot', 'fecal', 'felch', 'fellatio', 'feltch', 'female squirting', 'femdom', 'figging', 'fingering', 'fisting', 'foot fetish', 'footjob', 'frotting', 'fuck', 'fucking', 'fuck buttons', 'fudge packer', 'fudgepacker', 'futanari', 'g-spot', 'gang bang', 'gay sex', 'genitals', 'giant cock', 'girl on', 'girl on top', 'girls gone wild', 'goatcx', 'goatse', 'gokkun', 'golden shower', 'goo girl', 'goodpoop', 'goregasm', 'grope', 'group sex', 'guro', 'hand job', 'handjob', 'hard core', 'hardcore', 'hentai', 'homoerotic', 'honkey', 'hooker', 'hot chick', 'how to kill', 'how to murder', 'huge fat', 'humping', 'incest', 'intercourse', 'jack off', 'jail bait', 'jailbait', 'jerk off', 'jigaboo', 'jiggaboo', 'jiggerboo', 'jizz', 'juggs', 'kike', 'kinbaku', 'kinkster', 'kinky', 'knobbing', 'leather restraint', 'leather straight jacket', 'lemon party', 'lolita', 'lovemaking', 'make me come', 'male squirting', 'masturbate', 'menage a trois', 'milf', 'missionary position', 'motherfucker', 'mound of venus', 'mr hands', 'muff diver', 'muffdiving', 'nambla', 'nawashi', 'negro', 'neonazi', 'nig nog', 'nigga', 'nigger', 'nimphomania', 'nipple', 'nipples', 'nsfw images', 'nude', 'nudity', 'nympho', 'nymphomania', 'octopussy', 'omorashi', 'one cup two girls', 'one guy one jar', 'orgasm', 'orgy', 'paedophile', 'panties', 'panty', 'pedobear', 'pedophile', 'pegging', 'penis', 'phone sex', 'piece of shit', 'piss pig', 'pissing', 'pisspig', 'playboy', 'pleasure chest', 'pole smoker', 'ponyplay', 'poof', 'poop chute', 'poopchute', 'porn', 'porno', 'pornography', 'prince albert piercing', 'pthc', 'pubes', 'pussy', 'queaf', 'raghead', 'raging boner', 'rape', 'raping', 'rapist', 'rectum', 'reverse cowgirl', 'rimjob', 'rimming', 'rosy palm', 'rosy palm and her 5 sisters', 'rusty trombone', 's&m', 'sadism', 'scat', 'schlong', 'scissoring', 'semen', 'sex', 'sexo', 'sexy', 'shaved beaver', 'shaved pussy', 'shemale', 'shibari', 'shit', 'shota', 'shrimping', 'slanteye', 'slut', 'smut', 'snatch', 'snowballing', 'sodomize', 'sodomy', 'spic', 'spooge', 'spread legs', 'strap on', 'strapon', 'strappado', 'strip club', 'style doggy', 'suck', 'sucks', 'suicide girls', 'sultry women', 'swastika', 'swinger', 'tainted love', 'taste my', 'tea bagging', 'threesome', 'throating', 'tied up', 'tight white', 'tit', 'tits', 'titties', 'titty', 'tongue in a', 'topless', 'tosser', 'towelhead', 'tranny', 'tribadism', 'tub girl', 'tubgirl', 'tushy', 'twat', 'twink', 'twinkie', 'two girls one cup', 'undressing', 'upskirt', 'urethra play', 'urophilia', 'vagina', 'venus mound', 'vibrator', 'violet blue', 'violet wand', 'vorarephilia', 'voyeur', 'vulva', 'wank', 'wet dream', 'wetback', 'white power', 'women rapping', 'wrapping men', 'wrinkled starfish', 'xx', 'xxx', 'yaoi', 'yellow showers', 'yiffy', 'zoophilia']

def getSkills():
    """
    Reads the file skills.txt and creates a list of tuples on the form:
    (skillName, id)
    """
    out = []
    i = 0
    for line in open("skills.txt"):
        out.append((line.strip(), i))
        i += 1
    return out

def getLanguages():
    """
    Reads the file languages.txt and creates a list of tuples on the form:
    (language, id)
    """
    out = []
    i = 0
    for line in open("languages.txt"):
        out.append((line.strip(), i))
        i += 1
    return out

def randomString(allSkills):
    word = ''.join(random.choice(string.ascii_uppercase) for i in range(12))
    skill = random.choice(allSkills)
    if (random.randint(0,1) == 0):
        return word
    else:
        return skill

def randomDirt():
    return arrBad[random.randint(0, len(arrBad)-1)]

def generateSkills(dirt):
    allSkills = getSkills()
    generated = []
    i = 0
    while(i < lengthOfSkillGeneration):
        if dirt:
            generated.append((randomDirt(),i))
        else:
            generated.append(randomString(allSkills))
        i += 1
    return generated

def generateLanguages():
    generated = []
    languages = getLanguages()
    for i in range(LengthOfLanguageGeneration):
        generated.append((random.choice(languages),i))
    return generated

# print generateRandomSkills()
