# File name: solutions_41-60.py
# Author: Michael Chunko
# Date created: 6/7/19
# Python Version: 3.7

# This file contains the algorithms used for solving problems 21 through 40 (inclusive) from projecteuler.net

import math
import time
import helpers
from itertools import permutations


def problem_41():
    """ Return the largest n-digit pandigital prime. """

    # We assume that a number can be at most 9-digit pandigital for this exercise.
    # Some simple math shows us that all 8- and 9-digit pandigital numbers are divisible by 3 and thus cannot be prime,
    # so we make our upperbound 7 digits
    primes = helpers.eratosthenes_sieve(7654321)

    while primes:
        if helpers.is_pandigital(primes[-1], len(str(primes[-1]))):
            return primes[-1]
        else:
            primes.remove(primes[-1])

    pass


def problem_42():
    """ Return how many words have a word value equal to a triangle number.
        A word value is the sum of the word's alphabetical values, e.g. ABC has a word value of 1+2+3=6.
        A triangle number is equal to 0.5n(n+1). """
    num_words = 0  # number of words that are triangle numbers
    words = ["A", "ABILITY", "ABLE", "ABOUT", "ABOVE", "ABSENCE", "ABSOLUTELY", "ACADEMIC", "ACCEPT", "ACCESS",
             "ACCIDENT", "ACCOMPANY", "ACCORDING", "ACCOUNT", "ACHIEVE", "ACHIEVEMENT", "ACID", "ACQUIRE", "ACROSS",
             "ACT", "ACTION", "ACTIVE", "ACTIVITY", "ACTUAL", "ACTUALLY", "ADD", "ADDITION", "ADDITIONAL", "ADDRESS",
             "ADMINISTRATION", "ADMIT", "ADOPT", "ADULT", "ADVANCE", "ADVANTAGE", "ADVICE", "ADVISE", "AFFAIR",
             "AFFECT", "AFFORD", "AFRAID", "AFTER", "AFTERNOON", "AFTERWARDS", "AGAIN", "AGAINST", "AGE", "AGENCY",
             "AGENT", "AGO", "AGREE", "AGREEMENT", "AHEAD", "AID", "AIM", "AIR", "AIRCRAFT", "ALL", "ALLOW", "ALMOST",
             "ALONE", "ALONG", "ALREADY", "ALRIGHT", "ALSO", "ALTERNATIVE", "ALTHOUGH", "ALWAYS", "AMONG", "AMONGST",
             "AMOUNT", "AN", "ANALYSIS", "ANCIENT", "AND", "ANIMAL", "ANNOUNCE", "ANNUAL", "ANOTHER", "ANSWER", "ANY",
             "ANYBODY", "ANYONE", "ANYTHING", "ANYWAY", "APART", "APPARENT", "APPARENTLY", "APPEAL", "APPEAR",
             "APPEARANCE", "APPLICATION", "APPLY", "APPOINT", "APPOINTMENT", "APPROACH", "APPROPRIATE", "APPROVE",
             "AREA", "ARGUE", "ARGUMENT", "ARISE", "ARM", "ARMY", "AROUND", "ARRANGE", "ARRANGEMENT", "ARRIVE", "ART",
             "ARTICLE", "ARTIST", "AS", "ASK", "ASPECT", "ASSEMBLY", "ASSESS", "ASSESSMENT", "ASSET", "ASSOCIATE",
             "ASSOCIATION", "ASSUME", "ASSUMPTION", "AT", "ATMOSPHERE", "ATTACH", "ATTACK", "ATTEMPT", "ATTEND",
             "ATTENTION", "ATTITUDE", "ATTRACT", "ATTRACTIVE", "AUDIENCE", "AUTHOR", "AUTHORITY", "AVAILABLE",
             "AVERAGE", "AVOID", "AWARD", "AWARE", "AWAY", "AYE", "BABY", "BACK", "BACKGROUND", "BAD", "BAG", "BALANCE",
             "BALL", "BAND", "BANK", "BAR", "BASE", "BASIC", "BASIS", "BATTLE", "BE", "BEAR", "BEAT", "BEAUTIFUL",
             "BECAUSE", "BECOME", "BED", "BEDROOM", "BEFORE", "BEGIN", "BEGINNING", "BEHAVIOUR", "BEHIND", "BELIEF",
             "BELIEVE", "BELONG", "BELOW", "BENEATH", "BENEFIT", "BESIDE", "BEST", "BETTER", "BETWEEN", "BEYOND", "BIG",
             "BILL", "BIND", "BIRD", "BIRTH", "BIT", "BLACK", "BLOCK", "BLOOD", "BLOODY", "BLOW", "BLUE", "BOARD",
             "BOAT", "BODY", "BONE", "BOOK", "BORDER", "BOTH", "BOTTLE", "BOTTOM", "BOX", "BOY", "BRAIN", "BRANCH",
             "BREAK", "BREATH", "BRIDGE", "BRIEF", "BRIGHT", "BRING", "BROAD", "BROTHER", "BUDGET", "BUILD", "BUILDING",
             "BURN", "BUS", "BUSINESS", "BUSY", "BUT", "BUY", "BY", "CABINET", "CALL", "CAMPAIGN", "CAN", "CANDIDATE",
             "CAPABLE", "CAPACITY", "CAPITAL", "CAR", "CARD", "CARE", "CAREER", "CAREFUL", "CAREFULLY", "CARRY", "CASE",
             "CASH", "CAT", "CATCH", "CATEGORY", "CAUSE", "CELL", "CENTRAL", "CENTRE", "CENTURY", "CERTAIN",
             "CERTAINLY", "CHAIN", "CHAIR", "CHAIRMAN", "CHALLENGE", "CHANCE", "CHANGE", "CHANNEL", "CHAPTER",
             "CHARACTER", "CHARACTERISTIC", "CHARGE", "CHEAP", "CHECK", "CHEMICAL", "CHIEF", "CHILD", "CHOICE",
             "CHOOSE", "CHURCH", "CIRCLE", "CIRCUMSTANCE", "CITIZEN", "CITY", "CIVIL", "CLAIM", "CLASS", "CLEAN",
             "CLEAR", "CLEARLY", "CLIENT", "CLIMB", "CLOSE", "CLOSELY", "CLOTHES", "CLUB", "COAL", "CODE", "COFFEE",
             "COLD", "COLLEAGUE", "COLLECT", "COLLECTION", "COLLEGE", "COLOUR", "COMBINATION", "COMBINE", "COME",
             "COMMENT", "COMMERCIAL", "COMMISSION", "COMMIT", "COMMITMENT", "COMMITTEE", "COMMON", "COMMUNICATION",
             "COMMUNITY", "COMPANY", "COMPARE", "COMPARISON", "COMPETITION", "COMPLETE", "COMPLETELY", "COMPLEX",
             "COMPONENT", "COMPUTER", "CONCENTRATE", "CONCENTRATION", "CONCEPT", "CONCERN", "CONCERNED", "CONCLUDE",
             "CONCLUSION", "CONDITION", "CONDUCT", "CONFERENCE", "CONFIDENCE", "CONFIRM", "CONFLICT", "CONGRESS",
             "CONNECT", "CONNECTION", "CONSEQUENCE", "CONSERVATIVE", "CONSIDER", "CONSIDERABLE", "CONSIDERATION",
             "CONSIST", "CONSTANT", "CONSTRUCTION", "CONSUMER", "CONTACT", "CONTAIN", "CONTENT", "CONTEXT", "CONTINUE",
             "CONTRACT", "CONTRAST", "CONTRIBUTE", "CONTRIBUTION", "CONTROL", "CONVENTION", "CONVERSATION", "COPY",
             "CORNER", "CORPORATE", "CORRECT", "COS", "COST", "COULD", "COUNCIL", "COUNT", "COUNTRY", "COUNTY",
             "COUPLE", "COURSE", "COURT", "COVER", "CREATE", "CREATION", "CREDIT", "CRIME", "CRIMINAL", "CRISIS",
             "CRITERION", "CRITICAL", "CRITICISM", "CROSS", "CROWD", "CRY", "CULTURAL", "CULTURE", "CUP", "CURRENT",
             "CURRENTLY", "CURRICULUM", "CUSTOMER", "CUT", "DAMAGE", "DANGER", "DANGEROUS", "DARK", "DATA", "DATE",
             "DAUGHTER", "DAY", "DEAD", "DEAL", "DEATH", "DEBATE", "DEBT", "DECADE", "DECIDE", "DECISION", "DECLARE",
             "DEEP", "DEFENCE", "DEFENDANT", "DEFINE", "DEFINITION", "DEGREE", "DELIVER", "DEMAND", "DEMOCRATIC",
             "DEMONSTRATE", "DENY", "DEPARTMENT", "DEPEND", "DEPUTY", "DERIVE", "DESCRIBE", "DESCRIPTION", "DESIGN",
             "DESIRE", "DESK", "DESPITE", "DESTROY", "DETAIL", "DETAILED", "DETERMINE", "DEVELOP", "DEVELOPMENT",
             "DEVICE", "DIE", "DIFFERENCE", "DIFFERENT", "DIFFICULT", "DIFFICULTY", "DINNER", "DIRECT", "DIRECTION",
             "DIRECTLY", "DIRECTOR", "DISAPPEAR", "DISCIPLINE", "DISCOVER", "DISCUSS", "DISCUSSION", "DISEASE",
             "DISPLAY", "DISTANCE", "DISTINCTION", "DISTRIBUTION", "DISTRICT", "DIVIDE", "DIVISION", "DO", "DOCTOR",
             "DOCUMENT", "DOG", "DOMESTIC", "DOOR", "DOUBLE", "DOUBT", "DOWN", "DRAW", "DRAWING", "DREAM", "DRESS",
             "DRINK", "DRIVE", "DRIVER", "DROP", "DRUG", "DRY", "DUE", "DURING", "DUTY", "EACH", "EAR", "EARLY", "EARN",
             "EARTH", "EASILY", "EAST", "EASY", "EAT", "ECONOMIC", "ECONOMY", "EDGE", "EDITOR", "EDUCATION",
             "EDUCATIONAL", "EFFECT", "EFFECTIVE", "EFFECTIVELY", "EFFORT", "EGG", "EITHER", "ELDERLY", "ELECTION",
             "ELEMENT", "ELSE", "ELSEWHERE", "EMERGE", "EMPHASIS", "EMPLOY", "EMPLOYEE", "EMPLOYER", "EMPLOYMENT",
             "EMPTY", "ENABLE", "ENCOURAGE", "END", "ENEMY", "ENERGY", "ENGINE", "ENGINEERING", "ENJOY", "ENOUGH",
             "ENSURE", "ENTER", "ENTERPRISE", "ENTIRE", "ENTIRELY", "ENTITLE", "ENTRY", "ENVIRONMENT", "ENVIRONMENTAL",
             "EQUAL", "EQUALLY", "EQUIPMENT", "ERROR", "ESCAPE", "ESPECIALLY", "ESSENTIAL", "ESTABLISH",
             "ESTABLISHMENT", "ESTATE", "ESTIMATE", "EVEN", "EVENING", "EVENT", "EVENTUALLY", "EVER", "EVERY",
             "EVERYBODY", "EVERYONE", "EVERYTHING", "EVIDENCE", "EXACTLY", "EXAMINATION", "EXAMINE", "EXAMPLE",
             "EXCELLENT", "EXCEPT", "EXCHANGE", "EXECUTIVE", "EXERCISE", "EXHIBITION", "EXIST", "EXISTENCE", "EXISTING",
             "EXPECT", "EXPECTATION", "EXPENDITURE", "EXPENSE", "EXPENSIVE", "EXPERIENCE", "EXPERIMENT", "EXPERT",
             "EXPLAIN", "EXPLANATION", "EXPLORE", "EXPRESS", "EXPRESSION", "EXTEND", "EXTENT", "EXTERNAL", "EXTRA",
             "EXTREMELY", "EYE", "FACE", "FACILITY", "FACT", "FACTOR", "FACTORY", "FAIL", "FAILURE", "FAIR", "FAIRLY",
             "FAITH", "FALL", "FAMILIAR", "FAMILY", "FAMOUS", "FAR", "FARM", "FARMER", "FASHION", "FAST", "FATHER",
             "FAVOUR", "FEAR", "FEATURE", "FEE", "FEEL", "FEELING", "FEMALE", "FEW", "FIELD", "FIGHT", "FIGURE", "FILE",
             "FILL", "FILM", "FINAL", "FINALLY", "FINANCE", "FINANCIAL", "FIND", "FINDING", "FINE", "FINGER", "FINISH",
             "FIRE", "FIRM", "FIRST", "FISH", "FIT", "FIX", "FLAT", "FLIGHT", "FLOOR", "FLOW", "FLOWER", "FLY", "FOCUS",
             "FOLLOW", "FOLLOWING", "FOOD", "FOOT", "FOOTBALL", "FOR", "FORCE", "FOREIGN", "FOREST", "FORGET", "FORM",
             "FORMAL", "FORMER", "FORWARD", "FOUNDATION", "FREE", "FREEDOM", "FREQUENTLY", "FRESH", "FRIEND", "FROM",
             "FRONT", "FRUIT", "FUEL", "FULL", "FULLY", "FUNCTION", "FUND", "FUNNY", "FURTHER", "FUTURE", "GAIN",
             "GAME", "GARDEN", "GAS", "GATE", "GATHER", "GENERAL", "GENERALLY", "GENERATE", "GENERATION", "GENTLEMAN",
             "GET", "GIRL", "GIVE", "GLASS", "GO", "GOAL", "GOD", "GOLD", "GOOD", "GOVERNMENT", "GRANT", "GREAT",
             "GREEN", "GREY", "GROUND", "GROUP", "GROW", "GROWING", "GROWTH", "GUEST", "GUIDE", "GUN", "HAIR", "HALF",
             "HALL", "HAND", "HANDLE", "HANG", "HAPPEN", "HAPPY", "HARD", "HARDLY", "HATE", "HAVE", "HE", "HEAD",
             "HEALTH", "HEAR", "HEART", "HEAT", "HEAVY", "HELL", "HELP", "HENCE", "HER", "HERE", "HERSELF", "HIDE",
             "HIGH", "HIGHLY", "HILL", "HIM", "HIMSELF", "HIS", "HISTORICAL", "HISTORY", "HIT", "HOLD", "HOLE",
             "HOLIDAY", "HOME", "HOPE", "HORSE", "HOSPITAL", "HOT", "HOTEL", "HOUR", "HOUSE", "HOUSEHOLD", "HOUSING",
             "HOW", "HOWEVER", "HUGE", "HUMAN", "HURT", "HUSBAND", "I", "IDEA", "IDENTIFY", "IF", "IGNORE",
             "ILLUSTRATE", "IMAGE", "IMAGINE", "IMMEDIATE", "IMMEDIATELY", "IMPACT", "IMPLICATION", "IMPLY",
             "IMPORTANCE", "IMPORTANT", "IMPOSE", "IMPOSSIBLE", "IMPRESSION", "IMPROVE", "IMPROVEMENT", "IN",
             "INCIDENT", "INCLUDE", "INCLUDING", "INCOME", "INCREASE", "INCREASED", "INCREASINGLY", "INDEED",
             "INDEPENDENT", "INDEX", "INDICATE", "INDIVIDUAL", "INDUSTRIAL", "INDUSTRY", "INFLUENCE", "INFORM",
             "INFORMATION", "INITIAL", "INITIATIVE", "INJURY", "INSIDE", "INSIST", "INSTANCE", "INSTEAD", "INSTITUTE",
             "INSTITUTION", "INSTRUCTION", "INSTRUMENT", "INSURANCE", "INTEND", "INTENTION", "INTEREST", "INTERESTED",
             "INTERESTING", "INTERNAL", "INTERNATIONAL", "INTERPRETATION", "INTERVIEW", "INTO", "INTRODUCE",
             "INTRODUCTION", "INVESTIGATE", "INVESTIGATION", "INVESTMENT", "INVITE", "INVOLVE", "IRON", "IS", "ISLAND",
             "ISSUE", "IT", "ITEM", "ITS", "ITSELF", "JOB", "JOIN", "JOINT", "JOURNEY", "JUDGE", "JUMP", "JUST",
             "JUSTICE", "KEEP", "KEY", "KID", "KILL", "KIND", "KING", "KITCHEN", "KNEE", "KNOW", "KNOWLEDGE", "LABOUR",
             "LACK", "LADY", "LAND", "LANGUAGE", "LARGE", "LARGELY", "LAST", "LATE", "LATER", "LATTER", "LAUGH",
             "LAUNCH", "LAW", "LAWYER", "LAY", "LEAD", "LEADER", "LEADERSHIP", "LEADING", "LEAF", "LEAGUE", "LEAN",
             "LEARN", "LEAST", "LEAVE", "LEFT", "LEG", "LEGAL", "LEGISLATION", "LENGTH", "LESS", "LET", "LETTER",
             "LEVEL", "LIABILITY", "LIBERAL", "LIBRARY", "LIE", "LIFE", "LIFT", "LIGHT", "LIKE", "LIKELY", "LIMIT",
             "LIMITED", "LINE", "LINK", "LIP", "LIST", "LISTEN", "LITERATURE", "LITTLE", "LIVE", "LIVING", "LOAN",
             "LOCAL", "LOCATION", "LONG", "LOOK", "LORD", "LOSE", "LOSS", "LOT", "LOVE", "LOVELY", "LOW", "LUNCH",
             "MACHINE", "MAGAZINE", "MAIN", "MAINLY", "MAINTAIN", "MAJOR", "MAJORITY", "MAKE", "MALE", "MAN", "MANAGE",
             "MANAGEMENT", "MANAGER", "MANNER", "MANY", "MAP", "MARK", "MARKET", "MARRIAGE", "MARRIED", "MARRY", "MASS",
             "MASTER", "MATCH", "MATERIAL", "MATTER", "MAY", "MAYBE", "ME", "MEAL", "MEAN", "MEANING", "MEANS",
             "MEANWHILE", "MEASURE", "MECHANISM", "MEDIA", "MEDICAL", "MEET", "MEETING", "MEMBER", "MEMBERSHIP",
             "MEMORY", "MENTAL", "MENTION", "MERELY", "MESSAGE", "METAL", "METHOD", "MIDDLE", "MIGHT", "MILE",
             "MILITARY", "MILK", "MIND", "MINE", "MINISTER", "MINISTRY", "MINUTE", "MISS", "MISTAKE", "MODEL", "MODERN",
             "MODULE", "MOMENT", "MONEY", "MONTH", "MORE", "MORNING", "MOST", "MOTHER", "MOTION", "MOTOR", "MOUNTAIN",
             "MOUTH", "MOVE", "MOVEMENT", "MUCH", "MURDER", "MUSEUM", "MUSIC", "MUST", "MY", "MYSELF", "NAME", "NARROW",
             "NATION", "NATIONAL", "NATURAL", "NATURE", "NEAR", "NEARLY", "NECESSARILY", "NECESSARY", "NECK", "NEED",
             "NEGOTIATION", "NEIGHBOUR", "NEITHER", "NETWORK", "NEVER", "NEVERTHELESS", "NEW", "NEWS", "NEWSPAPER",
             "NEXT", "NICE", "NIGHT", "NO", "NOBODY", "NOD", "NOISE", "NONE", "NOR", "NORMAL", "NORMALLY", "NORTH",
             "NORTHERN", "NOSE", "NOT", "NOTE", "NOTHING", "NOTICE", "NOTION", "NOW", "NUCLEAR", "NUMBER", "NURSE",
             "OBJECT", "OBJECTIVE", "OBSERVATION", "OBSERVE", "OBTAIN", "OBVIOUS", "OBVIOUSLY", "OCCASION", "OCCUR",
             "ODD", "OF", "OFF", "OFFENCE", "OFFER", "OFFICE", "OFFICER", "OFFICIAL", "OFTEN", "OIL", "OKAY", "OLD",
             "ON", "ONCE", "ONE", "ONLY", "ONTO", "OPEN", "OPERATE", "OPERATION", "OPINION", "OPPORTUNITY",
             "OPPOSITION", "OPTION", "OR", "ORDER", "ORDINARY", "ORGANISATION", "ORGANISE", "ORGANIZATION", "ORIGIN",
             "ORIGINAL", "OTHER", "OTHERWISE", "OUGHT", "OUR", "OURSELVES", "OUT", "OUTCOME", "OUTPUT", "OUTSIDE",
             "OVER", "OVERALL", "OWN", "OWNER", "PACKAGE", "PAGE", "PAIN", "PAINT", "PAINTING", "PAIR", "PANEL",
             "PAPER", "PARENT", "PARK", "PARLIAMENT", "PART", "PARTICULAR", "PARTICULARLY", "PARTLY", "PARTNER",
             "PARTY", "PASS", "PASSAGE", "PAST", "PATH", "PATIENT", "PATTERN", "PAY", "PAYMENT", "PEACE", "PENSION",
             "PEOPLE", "PER", "PERCENT", "PERFECT", "PERFORM", "PERFORMANCE", "PERHAPS", "PERIOD", "PERMANENT",
             "PERSON", "PERSONAL", "PERSUADE", "PHASE", "PHONE", "PHOTOGRAPH", "PHYSICAL", "PICK", "PICTURE", "PIECE",
             "PLACE", "PLAN", "PLANNING", "PLANT", "PLASTIC", "PLATE", "PLAY", "PLAYER", "PLEASE", "PLEASURE", "PLENTY",
             "PLUS", "POCKET", "POINT", "POLICE", "POLICY", "POLITICAL", "POLITICS", "POOL", "POOR", "POPULAR",
             "POPULATION", "POSITION", "POSITIVE", "POSSIBILITY", "POSSIBLE", "POSSIBLY", "POST", "POTENTIAL", "POUND",
             "POWER", "POWERFUL", "PRACTICAL", "PRACTICE", "PREFER", "PREPARE", "PRESENCE", "PRESENT", "PRESIDENT",
             "PRESS", "PRESSURE", "PRETTY", "PREVENT", "PREVIOUS", "PREVIOUSLY", "PRICE", "PRIMARY", "PRIME",
             "PRINCIPLE", "PRIORITY", "PRISON", "PRISONER", "PRIVATE", "PROBABLY", "PROBLEM", "PROCEDURE", "PROCESS",
             "PRODUCE", "PRODUCT", "PRODUCTION", "PROFESSIONAL", "PROFIT", "PROGRAM", "PROGRAMME", "PROGRESS",
             "PROJECT", "PROMISE", "PROMOTE", "PROPER", "PROPERLY", "PROPERTY", "PROPORTION", "PROPOSE", "PROPOSAL",
             "PROSPECT", "PROTECT", "PROTECTION", "PROVE", "PROVIDE", "PROVIDED", "PROVISION", "PUB", "PUBLIC",
             "PUBLICATION", "PUBLISH", "PULL", "PUPIL", "PURPOSE", "PUSH", "PUT", "QUALITY", "QUARTER", "QUESTION",
             "QUICK", "QUICKLY", "QUIET", "QUITE", "RACE", "RADIO", "RAILWAY", "RAIN", "RAISE", "RANGE", "RAPIDLY",
             "RARE", "RATE", "RATHER", "REACH", "REACTION", "READ", "READER", "READING", "READY", "REAL", "REALISE",
             "REALITY", "REALIZE", "REALLY", "REASON", "REASONABLE", "RECALL", "RECEIVE", "RECENT", "RECENTLY",
             "RECOGNISE", "RECOGNITION", "RECOGNIZE", "RECOMMEND", "RECORD", "RECOVER", "RED", "REDUCE", "REDUCTION",
             "REFER", "REFERENCE", "REFLECT", "REFORM", "REFUSE", "REGARD", "REGION", "REGIONAL", "REGULAR",
             "REGULATION", "REJECT", "RELATE", "RELATION", "RELATIONSHIP", "RELATIVE", "RELATIVELY", "RELEASE",
             "RELEVANT", "RELIEF", "RELIGION", "RELIGIOUS", "RELY", "REMAIN", "REMEMBER", "REMIND", "REMOVE", "REPEAT",
             "REPLACE", "REPLY", "REPORT", "REPRESENT", "REPRESENTATION", "REPRESENTATIVE", "REQUEST", "REQUIRE",
             "REQUIREMENT", "RESEARCH", "RESOURCE", "RESPECT", "RESPOND", "RESPONSE", "RESPONSIBILITY", "RESPONSIBLE",
             "REST", "RESTAURANT", "RESULT", "RETAIN", "RETURN", "REVEAL", "REVENUE", "REVIEW", "REVOLUTION", "RICH",
             "RIDE", "RIGHT", "RING", "RISE", "RISK", "RIVER", "ROAD", "ROCK", "ROLE", "ROLL", "ROOF", "ROOM", "ROUND",
             "ROUTE", "ROW", "ROYAL", "RULE", "RUN", "RURAL", "SAFE", "SAFETY", "SALE", "SAME", "SAMPLE", "SATISFY",
             "SAVE", "SAY", "SCALE", "SCENE", "SCHEME", "SCHOOL", "SCIENCE", "SCIENTIFIC", "SCIENTIST", "SCORE",
             "SCREEN", "SEA", "SEARCH", "SEASON", "SEAT", "SECOND", "SECONDARY", "SECRETARY", "SECTION", "SECTOR",
             "SECURE", "SECURITY", "SEE", "SEEK", "SEEM", "SELECT", "SELECTION", "SELL", "SEND", "SENIOR", "SENSE",
             "SENTENCE", "SEPARATE", "SEQUENCE", "SERIES", "SERIOUS", "SERIOUSLY", "SERVANT", "SERVE", "SERVICE",
             "SESSION", "SET", "SETTLE", "SETTLEMENT", "SEVERAL", "SEVERE", "SEX", "SEXUAL", "SHAKE", "SHALL", "SHAPE",
             "SHARE", "SHE", "SHEET", "SHIP", "SHOE", "SHOOT", "SHOP", "SHORT", "SHOT", "SHOULD", "SHOULDER", "SHOUT",
             "SHOW", "SHUT", "SIDE", "SIGHT", "SIGN", "SIGNAL", "SIGNIFICANCE", "SIGNIFICANT", "SILENCE", "SIMILAR",
             "SIMPLE", "SIMPLY", "SINCE", "SING", "SINGLE", "SIR", "SISTER", "SIT", "SITE", "SITUATION", "SIZE",
             "SKILL", "SKIN", "SKY", "SLEEP", "SLIGHTLY", "SLIP", "SLOW", "SLOWLY", "SMALL", "SMILE", "SO", "SOCIAL",
             "SOCIETY", "SOFT", "SOFTWARE", "SOIL", "SOLDIER", "SOLICITOR", "SOLUTION", "SOME", "SOMEBODY", "SOMEONE",
             "SOMETHING", "SOMETIMES", "SOMEWHAT", "SOMEWHERE", "SON", "SONG", "SOON", "SORRY", "SORT", "SOUND",
             "SOURCE", "SOUTH", "SOUTHERN", "SPACE", "SPEAK", "SPEAKER", "SPECIAL", "SPECIES", "SPECIFIC", "SPEECH",
             "SPEED", "SPEND", "SPIRIT", "SPORT", "SPOT", "SPREAD", "SPRING", "STAFF", "STAGE", "STAND", "STANDARD",
             "STAR", "START", "STATE", "STATEMENT", "STATION", "STATUS", "STAY", "STEAL", "STEP", "STICK", "STILL",
             "STOCK", "STONE", "STOP", "STORE", "STORY", "STRAIGHT", "STRANGE", "STRATEGY", "STREET", "STRENGTH",
             "STRIKE", "STRONG", "STRONGLY", "STRUCTURE", "STUDENT", "STUDIO", "STUDY", "STUFF", "STYLE", "SUBJECT",
             "SUBSTANTIAL", "SUCCEED", "SUCCESS", "SUCCESSFUL", "SUCH", "SUDDENLY", "SUFFER", "SUFFICIENT", "SUGGEST",
             "SUGGESTION", "SUITABLE", "SUM", "SUMMER", "SUN", "SUPPLY", "SUPPORT", "SUPPOSE", "SURE", "SURELY",
             "SURFACE", "SURPRISE", "SURROUND", "SURVEY", "SURVIVE", "SWITCH", "SYSTEM", "TABLE", "TAKE", "TALK",
             "TALL", "TAPE", "TARGET", "TASK", "TAX", "TEA", "TEACH", "TEACHER", "TEACHING", "TEAM", "TEAR",
             "TECHNICAL", "TECHNIQUE", "TECHNOLOGY", "TELEPHONE", "TELEVISION", "TELL", "TEMPERATURE", "TEND", "TERM",
             "TERMS", "TERRIBLE", "TEST", "TEXT", "THAN", "THANK", "THANKS", "THAT", "THE", "THEATRE", "THEIR", "THEM",
             "THEME", "THEMSELVES", "THEN", "THEORY", "THERE", "THEREFORE", "THESE", "THEY", "THIN", "THING", "THINK",
             "THIS", "THOSE", "THOUGH", "THOUGHT", "THREAT", "THREATEN", "THROUGH", "THROUGHOUT", "THROW", "THUS",
             "TICKET", "TIME", "TINY", "TITLE", "TO", "TODAY", "TOGETHER", "TOMORROW", "TONE", "TONIGHT", "TOO", "TOOL",
             "TOOTH", "TOP", "TOTAL", "TOTALLY", "TOUCH", "TOUR", "TOWARDS", "TOWN", "TRACK", "TRADE", "TRADITION",
             "TRADITIONAL", "TRAFFIC", "TRAIN", "TRAINING", "TRANSFER", "TRANSPORT", "TRAVEL", "TREAT", "TREATMENT",
             "TREATY", "TREE", "TREND", "TRIAL", "TRIP", "TROOP", "TROUBLE", "TRUE", "TRUST", "TRUTH", "TRY", "TURN",
             "TWICE", "TYPE", "TYPICAL", "UNABLE", "UNDER", "UNDERSTAND", "UNDERSTANDING", "UNDERTAKE", "UNEMPLOYMENT",
             "UNFORTUNATELY", "UNION", "UNIT", "UNITED", "UNIVERSITY", "UNLESS", "UNLIKELY", "UNTIL", "UP", "UPON",
             "UPPER", "URBAN", "US", "USE", "USED", "USEFUL", "USER", "USUAL", "USUALLY", "VALUE", "VARIATION",
             "VARIETY", "VARIOUS", "VARY", "VAST", "VEHICLE", "VERSION", "VERY", "VIA", "VICTIM", "VICTORY", "VIDEO",
             "VIEW", "VILLAGE", "VIOLENCE", "VISION", "VISIT", "VISITOR", "VITAL", "VOICE", "VOLUME", "VOTE", "WAGE",
             "WAIT", "WALK", "WALL", "WANT", "WAR", "WARM", "WARN", "WASH", "WATCH", "WATER", "WAVE", "WAY", "WE",
             "WEAK", "WEAPON", "WEAR", "WEATHER", "WEEK", "WEEKEND", "WEIGHT", "WELCOME", "WELFARE", "WELL", "WEST",
             "WESTERN", "WHAT", "WHATEVER", "WHEN", "WHERE", "WHEREAS", "WHETHER", "WHICH", "WHILE", "WHILST", "WHITE",
             "WHO", "WHOLE", "WHOM", "WHOSE", "WHY", "WIDE", "WIDELY", "WIFE", "WILD", "WILL", "WIN", "WIND", "WINDOW",
             "WINE", "WING", "WINNER", "WINTER", "WISH", "WITH", "WITHDRAW", "WITHIN", "WITHOUT", "WOMAN", "WONDER",
             "WONDERFUL", "WOOD", "WORD", "WORK", "WORKER", "WORKING", "WORKS", "WORLD", "WORRY", "WORTH", "WOULD",
             "WRITE", "WRITER", "WRITING", "WRONG", "YARD", "YEAH", "YEAR", "YES", "YESTERDAY", "YET", "YOU", "YOUNG",
             "YOUR", "YOURSELF", "YOUTH"]
    triangle_nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]  # starting off with the given numbers

    def next_triangle_num():
        """ Find the next triangle number not yet calculated. """
        n = len(triangle_nums) + 1
        triangle_nums.append(n * (n + 1) // 2)

    for word in words:
        total = 0
        for letter in word:  # Find word value
            total += ord(letter) - 64

        while total > triangle_nums[-1]:  # Greater than the highest calculated triangle number
            next_triangle_num()

        if total in triangle_nums:
            num_words += 1

    return num_words


def problem_43():
    """ Return the sum of all 0 to 9 pandigital numbers such that (where d_1 is the 1st digit, d_2 is the 2nd, etc.)
        d_2d_3d_4 is divisible by 2,
        d_3d_4d_5 is divisible by 3,
        d_4d_5d_6 is divisible by 5,
        ...
        d_8d_9d_10 is divisible by 17. """

    # From some basic mathematical analysis, we get that d_4 must be even, d_3 + d_4 + d_5 is divisible by 3,
    # d_6 is equal to 5 (since otherwise it would be 0 but that would mean d_6d_7d_8 is never divisible by 11.
    # We can refine our search space further and rather easily get the precise numbers meeting this definition.
    # For interest's sake, we do not refine the search space this far
    
    total = 0
    pandigitals = list(permutations(range(0, 10)))
    divisors = [7, 11, 13, 17]
    for num in pandigitals:
        if num[3] % 2 != 0 or num[5] != 5 or (num[2] + num[3] + num[4]) % 3 != 0:
            continue

        for i in range(0, len(divisors)):  # Check all divisions
            if ((num[i + 4] * 100) + (num[i + 5] * 10) + num[i + 6]) % divisors[i] != 0:
                break
        else:  # Run only if num is divisible by everything in divisors
            for i in range(9, -1, -1):  # Convert num to a proper number and add it to total
                total += num[i] * math.pow(10, 10 - i - 1)

    return int(total)


def problem_45():
    """ Return the first triangle number (after 40755) that is also pentagonal and hexagonal.
        Triangle   t_n = n(n+1)/2
        Pentagonal p_n = n(3n-1)/2
        Hexagonal  h_n = n(2n-1) """

    n = 285 + 1  # The n corresponding to t_n = 40755 can be found to be 285

    while True:
        t_n = (n * (n + 1)) // 2
        p_n = helpers.quadratic(3, -1, -t_n * 2)[1]
        if int(p_n) == p_n:  # Checking that t_n is also a pentagonal number
            h_n = helpers.quadratic(2, -1, -t_n)[1]
            if int(h_n) == h_n:  # Checking that t_n is also a hexagonal number
                return t_n
        n += 1


if __name__ == "__main__":
    start_time = time.time()
    print(problem_43())
    print("--- %s seconds ---" % (time.time() - start_time))
