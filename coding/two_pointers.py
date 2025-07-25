#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from functools import singledispatch

@singledispatch
def singledispatch_function(_):
    return

@singledispatch_function.register
def checkListInteger(input_case: list):
    if type(input_case).__name__ != "list":
        return f"custom error: {input_case} is {type(input_case).__name__} not list"
    if len(input_case) == 0:
        return f"custom error: {input_case} is empty" 
    maximum = 10_000_000
    minimum = -10_000_000
    for value in input_case:
        turn_string = str(value)
        if not turn_string.lstrip('-+').isdigit():
            return f"custom error: {value} is not a integer"
        if value >= maximum or minimum >= value:
            return f"custom error: {value} is out of range"
    return True

@singledispatch_function.register
def checkInteger(input_number: int):
    turn_string = str(input_number).lstrip('-+')
    if not str.isdigit(turn_string):
         return f"custom error: {input_number} is {type(input_number).__name__} not integer"
    return True

# https://leetcode.com/problems/is-subsequence/description/
# Is Subsequence, easy
class IsSubsequence:
    def subsequence(self, string_one, string_two):
        numsIter = iter(string_two)
        return all(character in numsIter for character in string_one)

is_ds = IsSubsequence()
def get_is(_):
    print("Is Subsequence")
    print("happy path")
    print(is_ds.subsequence("abc", "ahbgdc"))
    print(is_ds.subsequence("ace", "abcde"))
    print(is_ds.subsequence("a", "apple"))
    print(is_ds.subsequence("b", "banana"))
    print(is_ds.subsequence("dog", "dodog"))
    print(is_ds.subsequence("cat", "concatenate"))
    print(is_ds.subsequence("fan", "financial"))
    print(is_ds.subsequence("rain", "brainstorming"))
    print(is_ds.subsequence("sun", "sunshine"))
    print(is_ds.subsequence("key", "monkey"))

    print()

    print("corner case")
    print(is_ds.subsequence("", ""))
    print(is_ds.subsequence("a", ""))
    print(is_ds.subsequence("z", "a"))
    print(is_ds.subsequence("aaaa", "aaa"))
    print(is_ds.subsequence("abc", "acb"))
    print(is_ds.subsequence("longstring", "short"))
    print(is_ds.subsequence("xyz", "x"))
    print(is_ds.subsequence("a"*100, "a"*10000))
    print(is_ds.subsequence("abc", "ab"))
    print(is_ds.subsequence("abc", "abcabcabc"))

    print()

    if input("Next: 352 edge cases \ncontinue: ").strip().lower() != "y":
        return

    print()

    print("edge case")
    edges = [
        ("a" * 10**7, "a" * 10**8),
        (None, "string"),
        (123, "number"),
        ("test"[-100:], "negative"),
        ("\ud800", "surrogate\ud800pair"),
        ("\udcff", "surr\udcffgate"),
        ("a" * 10000, "a" * 10000),
        ("x" * (2**31), "overflow"),
        ("", "divide" + "a" * 0),
        ("path\\to", "path\\to\\file"),
        ("café", "caf\xe9"),
        ("é", "e\u0301"),
        ("ABC", "abc"),
        ("ß", "straße"),
        ("\ufeff", "bom\ufeffmark"),
        ("abcdefghijklmnopqrstuvwxyz", "azbycxdwevfugthsirjqkplomn"),
        ("buffer" * 10**6, "b"),
        ("sys" * (2**20), "system"),
        ("loop", "l" + "o" * 10**6 + "op"),
        ("invalid\x00", "null\x00byte"),
        ("key", "k" + "e" * 10**5 + "y"),
        ("iter", "i" * 10**4 + "ter"),
        ("gen", "g" * 10**3 + "en"),
        ("interrupt", "i" * 10**7 + "nterrupt"),
        ("∞", "infinity∞"),
        ("import", "imp" + "o" * 10**5 + "rt"),
        ("io", "i" + "\r\n" * 10**4 + "o"),
        ("env", "e" + "$" * 10**3 + "nv"),
        ("windows\r\n", "windows\r\n\r\n"),
        ("block", "b" + "\x00" * 10**3 + "lock"),
        ("child", "c" + "\x01" * 10**3 + "hild"),
        ("connect", "c" + ":" * 10**3 + "onnect"),
        ("pipe", "p" + "|" * 10**3 + "ipe"),
        ("file", "f" + "/" * 10**3 + "ile"),
        ("perm", "p" + "!" * 10**3 + "erm"),
        ("proc", "p" + "#" * 10**3 + "roc"),
        ("signal", "s" + "%" * 10**3 + "ignal"),
        ("dir", "d" + "\\" * 10**3 + "ir"),
        ("notdir", "n" + "." * 10**3 + "otdir"),
        ("empty", ""),
        ("full", "f" + "u" * 10**6 + "ll"),
        ("weak", "w" + "e" * 10**5 + "ak"),
        ("ref", "r" + "e" * 10**5 + "f"),
        ("syntax", "s{yn}tax"),
        ("indent", "\t\t\tindent"),
        ("tab", "\t \ttab"),
        ("unbound", "u" + "n" * 10**4 + "bound"),
        ("name", "n" + "a" * 10**4 + "me"),
        ("math", "m" + "+" * 10**3 + "ath"),
        ("assert", "a" + "=" * 10**3 + "ssert"),
        ("eof", "e" + "\x04" * 10**3 + "of"),
        ("lookup", "l" + "?" * 10**3 + "ookup"),
        ("async", "a" + "~" * 10**3 + "sync"),
        ("module", "m" + "@" * 10**3 + "odule"),
        ("resource", "r" + "&" * 10**3 + "esource"),
        ("deprecated", "d" + "^" * 10**3 + "eprecated"),
        ("pending", "p" + "*" * 10**3 + "ending"),
        ("runtime", "r" + "(" * 10**3 + "untime"),
        ("synwarn", "s" + ")" * 10**3 + "ynwarn"),
        ("user", "u" + "" * 10**3 + "uture"),
        ("impwarn", "i" + "[" * 10**3 + "mpwarn"),
        ("uniwarn", "u" + "]" * 10**3 + "niwarn"),
        ("bytes", "b" + "\\x" * 10**3 + "ytes"),
        ("sysres", "s" + ";" * 10**3 + "ysres"),
        ("compile", "c" + "'" * 10**3 + "ompile"),
        ("interp", "i" + '"' * 10**3 + "nterp"),
        ("optimize", "o" + "`" * 10**3 + "ptimize"),
        ("thread", "t" + "~" * 10**3 + "hread"),
        ("lock", "l" + "±" * 10**3 + "ock"),
        ("deadlock", "d" + "∞" * 10**3 + "eadlock"),
        ("stack", "s" + "↑" * 10**3 + "tack"),
        ("heap", "h" + "↓" * 10**3 + "eap"),
        ("segment", "s" + "→" * 10**3 + "egment"),
        ("access", "a" + "←" * 10**3 + "ccess"),
        ("protect", "p" + "↔" * 10**3 + "rotect"),
        ("align", "a" + "↕" * 10**3 + "lign"),
        ("cache", "c" + "⊕" * 10**3 + "ache"),
        ("network", "n" + "⊗" * 10**3 + "etwork"),
        ("database", "d" + "⊙" * 10**3 + "atabase"),
        ("config", "c" + "⊘" * 10**3 + "onfig"),
        ("validate", "v" + "⊚" * 10**3 + "alidate"),
        ("serialize", "s" + "⊛" * 10**3 + "erialize"),
        ("compress", "c" + "⊜" * 10**3 + "ompress"),
        ("encrypt", "e" + "⊝" * 10**3 + "ncrypt"),
        ("auth", "a" + "⊞" * 10**3 + "uth"),
        ("authz", "a" + "⊟" * 10**3 + "uthz"),
        ("token", "t" + "⊠" * 10**3 + "oken"),
        ("session", "s" + "⊡" * 10**3 + "ession"),
        ("cookie", "c" + "⋄" * 10**3 + "ookie"),
        ("header", "h" + "⋅" * 10**3 + "eader"),
        ("body", "b" + "⋆" * 10**3 + "ody"),
        ("stream", "s" + "⋇" * 10**3 + "tream"),
        ("overflow", "o" + "⋈" * 10**3 + "verflow"),
        ("underflow", "u" + "⋉" * 10**3 + "nderflow"),
        ("precision", "p" + "⋊" * 10**3 + "recision"),
        ("rounding", "r" + "⋋" * 10**3 + "ounding"),
        ("truncate", "t" + "⋌" * 10**3 + "runcate"),
        ("quantize", "q" + "⋍" * 10**3 + "uantize"),
        ("sample", "s" + "⋎" * 10**3 + "ample"),
        ("interpolate", "i" + "⋏" * 10**3 + "nterpolate"),
        ("extrapolate", "e" + "⋐" * 10**3 + "xtrapolate"),
        ("converge", "c" + "⋑" * 10**3 + "onverge"),
        ("diverge", "d" + "⋒" * 10**3 + "iverge"),
        ("stability", "s" + "⋓" * 10**3 + "tability"),
        ("accuracy", "a" + "⋔" * 10**3 + "ccuracy"),
        ("efficiency", "e" + "⋕" * 10**3 + "fficiency"),
        ("scalability", "s" + "⋖" * 10**3 + "calability"),
        ("performance", "p" + "⋗" * 10**3 + "erformance"),
        ("latency", "l" + "⋘" * 10**3 + "atency"),
        ("throughput", "t" + "⋙" * 10**3 + "hroughput"),
        ("bandwidth", "b" + "⋚" * 10**3 + "andwidth"),
        ("capacity", "c" + "⋛" * 10**3 + "apacity"),
        ("quota", "q" + "⋜" * 10**3 + "uota"),
        ("limit", "l" + "⋝" * 10**3 + "imit"),
        ("throttle", "t" + "⋞" * 10**3 + "hrottle"),
        ("ratelimit", "r" + "⋟" * 10**3 + "atelimit"),
        ("circuit", "c" + "⋠" * 10**3 + "ircuit"),
        ("retry", "r" + "⋡" * 10**3 + "etry"),
        ("backoff", "b" + "⋢" * 10**3 + "ackoff"),
        ("jitter", "j" + "⋣" * 10**3 + "itter"),
        ("skew", "s" + "⋤" * 10**3 + "kew"),
        ("drift", "d" + "⋥" * 10**3 + "rift"),
        ("sync", "s" + "⋦" * 10**3 + "ync"),
        ("asyncerr", "a" + "⋧" * 10**3 + "syncerr"),
        ("concurrency", "c" + "⋨" * 10**3 + "oncurrency"),
        ("parallel", "p" + "⋩" * 10**3 + "arallel"),
        ("distributed", "d" + "⋪" * 10**3 + "istributed"),
        ("cluster", "c" + "⋫" * 10**3 + "luster"),
        ("node", "n" + "⋬" * 10**3 + "ode"),
        ("partition", "p" + "⋭" * 10**3 + "artition"),
        ("replication", "r" + "⋮" * 10**3 + "eplication"),
        ("consistency", "c" + "⋯" * 10**3 + "onsistency"),
        ("integrity", "i" + "⋰" * 10**3 + "ntegrity"),
        ("corruption", "c" + "⋱" * 10**3 + "orruption"),
        ("checksum", "c" + "⋲" * 10**3 + "hecksum"),
        ("hash", "h" + "⋳" * 10**3 + "ash"),
        ("signature", "s" + "⋴" * 10**3 + "ignature"),
        ("certificate", "c" + "⋵" * 10**3 + "ertificate"),
        ("trust", "t" + "⋶" * 10**3 + "rust"),
        ("verification", "v" + "⋷" * 10**3 + "erification"),
        ("compliance", "c" + "⋸" * 10**3 + "ompliance"),
        ("audit", "a" + "⋹" * 10**3 + "udit"),
        ("log", "l" + "⋺" * 10**3 + "og"),
        ("metrics", "m" + "⋻" * 10**3 + "etrics"),
        ("monitoring", "m" + "⋼" * 10**3 + "onitoring"),
        ("alert", "a" + "⋽" * 10**3 + "lert"),
        ("notification", "n" + "⋾" * 10**3 + "otification"),
        ("escalation", "e" + "⋿" * 10**3 + "scalation"),
        ("recovery", "r" + "⌀" * 10**3 + "ecovery"),
        ("backup", "b" + "⌁" * 10**3 + "ackup"),
        ("restore", "r" + "⌂" * 10**3 + "estore"),
        ("migration", "m" + "⌃" * 10**3 + "igration"),
        ("upgrade", "u" + "⌄" * 10**3 + "pgrade"),
        ("downgrade", "d" + "⌅" * 10**3 + "owngrade"),
        ("rollback", "r" + "⌆" * 10**3 + "ollback"),
        ("deployment", "d" + "⌇" * 10**3 + "eployment"),
        ("configuration", "c" + "⌈" * 10**3 + "onfiguration"),
        ("initialization", "i" + "⌉" * 10**3 + "nitialization"),
        ("shutdown", "s" + "⌊" * 10**3 + "hutdown"),
        ("maintenance", "m" + "⌋" * 10**3 + "aintenance"),
        ("unavailable", "u" + "⌌" * 10**3 + "navailable"),
        ("overload", "o" + "⌍" * 10**3 + "verload"),
        ("starvation", "s" + "⌎" * 10**3 + "tarvation"),
        ("contention", "c" + "⌏" * 10**3 + "ontention"),
        ("priority", "p" + "⌐" * 10**3 + "riority"),
        ("scheduling", "s" + "⌑" * 10**3 + "cheduling"),
        ("loadbalancing", "l" + "⌒" * 10**3 + "oadbalancing"),
        ("failover", "f" + "⌓" * 10**3 + "ailover"),
        ("redundancy", "r" + "⌔" * 10**3 + "edundancy"),
        ("partitioning", "p" + "⌕" * 10**3 + "artitioning"),
        ("byzantine", "b" + "⌖" * 10**3 + "yzantine"),
        ("consensus", "c" + "⌗" * 10**3 + "onsensus"),
        ("leaderelection", "l" + "⌘" * 10**3 + "eaderelection"),
        ("splitbrain", "s" + "⌙" * 10**3 + "plitbrain"),
        ("quorum", "q" + "⌚" * 10**3 + "uorum"),
        ("majority", "m" + "⌛" * 10**3 + "ajority"),
        ("minority", "m" + "⌜" * 10**3 + "inority"),
        ("voting", "v" + "⌝" * 10**3 + "oting"),
        ("election", "e" + "⌞" * 10**3 + "lection"),
        ("campaign", "c" + "⌟" * 10**3 + "ampaign"),
        ("term", "t" + "⌠" * 10**3 + "erm"),
        ("expiration", "e" + "⌡" * 10**3 + "xpiration"),
        ("renewal", "r" + "⌢" * 10**3 + "enewal"),
        ("refresh", "r" + "⌣" * 10**3 + "efresh"),
        ("cacheinvalidation", "c" + "⌤" * 10**3 + "acheinvalidation"),
        ("staledata", "s" + "⌥" * 10**3 + "taledata"),
        ("versioning", "v" + "⌦" * 10**3 + "ersioning"),
        ("conflict", "c" + "⌧" * 10**3 + "onflict"),
        ("merge", "m" + "⌨" * 10**3 + "erge"),
        ("branching", "b" + "〈" * 10**3 + "ranching"),
        ("tagging", "t" + "〉" * 10**3 + "agging"),
        ("release", "r" + "⌫" * 10**3 + "elease"),
        ("hotfix", "h" + "⌬" * 10**3 + "otfix"),
        ("patch", "p" + "⌭" * 10**3 + "atch"),
        ("update", "u" + "⌮" * 10**3 + "pdate"),
        ("install", "i" + "⌯" * 10**3 + "nstall"),
        ("uninstall", "u" + "⌰" * 10**3 + "ninstall"),
        ("activation", "a" + "⌱" * 10**3 + "ctivation"),
        ("deactivation", "d" + "⌲" * 10**3 + "eactivation"),
        ("registration", "r" + "⌳" * 10**3 + "egistration"),
        ("unregistration", "u" + "⌴" * 10**3 + "nregistration"),
        ("subscription", "s" + "⌵" * 10**3 + "ubscription"),
        ("unsubscription", "u" + "⌶" * 10**3 + "nsubscription"),
        ("publication", "p" + "⌷" * 10**3 + "ublication"),
        ("discovery", "d" + "⌸" * 10**3 + "iscovery"),
        ("advertisement", "a" + "⌹" * 10**3 + "dvertisement"),
        ("announcement", "a" + "⌺" * 10**3 + "nnouncement"),
        ("broadcast", "b" + "⌻" * 10**3 + "roadcast"),
        ("multicast", "m" + "⌼" * 10**3 + "ulticast"),
        ("unicast", "u" + "⌽" * 10**3 + "nicast"),
        ("routing", "r" + "⌾" * 10**3 + "outing"),
        ("forwarding", "f" + "⌿" * 10**3 + "orwarding"),
        ("switching", "s" + "⍀" * 10**3 + "witching"),
        ("bridging", "b" + "⍁" * 10**3 + "ridging"),
        ("tunneling", "t" + "⍂" * 10**3 + "unneling"),
        ("proxy", "p" + "⍃" * 10**3 + "roxy"),
        ("gateway", "g" + "⍄" * 10**3 + "ateway"),
        ("firewall", "f" + "⍅" * 10**3 + "irewall"),
        ("intrusion", "i" + "⍆" * 10**3 + "ntrusion"),
        ("antivirus", "a" + "⍇" * 10**3 + "ntivirus"),
        ("malware", "m" + "⍈" * 10**3 + "alware"),
        ("spam", "s" + "⍉" * 10**3 + "pam"),
        ("phishing", "p" + "⍊" * 10**3 + "hishing"),
        ("fraud", "f" + "⍋" * 10**3 + "raud"),
        ("anomaly", "a" + "⍌" * 10**3 + "nomaly"),
        ("outlier", "o" + "⍍" * 10**3 + "utlier"),
        ("classification", "c" + "⍎" * 10**3 + "lassification"),
        ("clustering", "c" + "⍏" * 10**3 + "lustering"),
        ("regression", "r" + "⍐" * 10**3 + "egression"),
        ("prediction", "p" + "⍑" * 10**3 + "rediction"),
        ("forecasting", "f" + "⍒" * 10**3 + "orecasting"),
        ("optimization", "o" + "⍓" * 10**3 + "ptimization"),
        ("evolution", "e" + "⍔" * 10**3 + "volution"),
        ("genetic", "g" + "⍕" * 10**3 + "enetic"),
        ("neuralnetwork", "n" + "⍖" * 10**3 + "euralnetwork"),
        ("deeplearning", "d" + "⍗" * 10**3 + "eeplearning"),
        ("machinelearning", "m" + "⍘" * 10**3 + "achinelearning"),
        ("artificialintelligence", "a" + "⍙" * 10**3 + "rtificialintelligence"),
        ("naturallanguage", "n" + "⍚" * 10**3 + "aturallanguage"),
        ("computervision", "c" + "⍛" * 10**3 + "omputervision"),
        ("imageprocessing", "i" + "⍜" * 10**3 + "mageprocessing"),
        ("signalprocessing", "s" + "⍝" * 10**3 + "ignalprocessing"),
        ("datamining", "d" + "⍞" * 10**3 + "atamining"),
        ("bigdata", "b" + "⍟" * 10**3 + "igdata"),
        ("streaming", "s" + "⍠" * 10**3 + "treaming"),
        ("batchprocessing", "b" + "⍡" * 10**3),
        ("\U0010FFFF", "max\U0010FFFFunicode"),
        ("\uE000\uE001", "private\uE000use\uE001area"),
        ("a\uFE0F", "a\uFE0Fvariation"),
        ("e\u0300\u0301", "e\u0300\u0301combined"),
        ("\u202E", "rtl\u202Eoverride"),
        ("a\u200Bb", "a\u200Bzero\u200Bwidth\u200Bb"),
        ("\u221E", "infinity\u221Esymbol"),
        ("\U0001F44D\U0001F3FB", "thumbs\U0001F44D\U0001F3FBup"),
        ("\uD800test", "high\uD800surrogate"),
        ("\uDC00test", "low\uDC00surrogate"),
        ("\u0000\u0001", "control\u0000\u0001chars"),
        ("\uFFFD", "replacement\uFFFDchar"),
        ("\uFEFF\uFFFE", "bom\uFEFF\uFFFEvariations"),
        ("\u3000", "ideographic\u3000space"),
        ("\u00A0", "non\u00A0breaking\u00A0space"),
        ("soft\u00ADhyphen", "soft\u00ADhyphen"),
        ("\uFB50", "arabic\uFB50presentation"),
        ("\U00020000", "cjk\U00020000extension"),
        ("\uAC00", "hangul\uAC00syllable"),
        ("\u30FB", "katakana\u30FBdot"),
        ("\u1F00", "greek\u1F00extended"),
        ("\u0500", "cyrillic\u0500supplement"),
        ("\u1E00", "latin\u1E00extended"),
        ("\u2000", "general\u2000punctuation"),
        ("\u20AC", "euro\u20ACsymbol"),
        ("\u2200", "forall\u2200operator"),
        ("\u25A0", "black\u25A0square"),
        ("\u2600", "sun\u2600symbol"),
        ("\u2700", "dingbat\u2700symbol"),
        ("\u2E00", "supplemental\u2E00punctuation"),
        ("\uFE10", "vertical\uFE10form"),
        ("\uFE50", "small\uFE50form"),
        ("\uFF00", "fullwidth\uFF00form"),
        ("\uFFF0", "special\uFFF0block"),
        ("\U00010000", "linear\U00010000b"),
        ("\U00010330", "gothic\U00010330char"),
        ("\U00010400", "deseret\U00010400alphabet"),
        ("\U00010450", "shavian\U00010450alphabet"),
        ("\U00010480", "osmanya\U00010480script"),
        ("\U00010800", "cypriot\U00010800syllabary"),
        ("\U00010900", "phoenician\U00010900alphabet"),
        ("\U00010920", "lydian\U00010920alphabet"),
        ("\U00010A00", "kharoshthi\U00010A00script"),
        ("\U00012000", "cuneiform\U00012000script"),
        ("\U0001D000", "byzantine\U0001D000musical"),
        ("\U0001D100", "musical\U0001D100symbols"),
        ("\U0001D200", "ancient\U0001D200greek"),
        ("\U0001D300", "tai\U0001D300xuan"),
        ("\U0001D400", "math\U0001D400alphanumeric"),
        ("\U0001F000", "mahjong\U0001F000tiles"),
        ("\U0001F030", "domino\U0001F030tiles"),
        ("\U0001F0A0", "playing\U0001F0A0cards"),
        ("\U0001F300", "misc\U0001F300symbols"),
        ("\U0001F600", "emoticon\U0001F600face"),
        ("\U0001F680", "transport\U0001F680symbols"),
        ("\U0001F700", "alchemical\U0001F700symbols"),
        ("\U0001F780", "geometric\U0001F780extended"),
        ("\U0001F800", "arrows\U0001F800supplemental"),
        ("\U000E0000", "tag\U000E0000block"),
        ("\U000E0100", "variation\U000E0100supplement"),
        ("\U000F0000", "private\U000F0000area"),
        ("\U00100000", "private\U00100000area"),
        ("\U0010FFFE", "city15\U0010FFFEprivate")
    ]

    for eCase in edges:
        try:
            find_is = is_ds.removeDuplicates(eCase)
            if find_is != None:
                print(find_is)
        except Exception as error_message:
            print(type(error_message).__name__.replace("Error", " error").lower(), ":", eCase)


get_is(None)

print()

if input("Next: Two Sum II - Input Array Is Sorted\ncontinue: ").strip().lower() != "y":
    exit()

print()

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Two Sum II - Input Array Is Sorted, Medium
class TwoSumTwo:
    def twoSum(self, numbers, target):
        # numbers is list, target is integer
        checking = singledispatch_function(numbers)
        if checking is not True:
            print(checking)
            return
        checking = singledispatch_function(target)
        if checking is not True:
            print(checking)
            return        

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[right] + numbers[left]
            if total == target:
                return [left+1, right+1]
            elif target > total:
                left += 1
            else:
                right -= 1
        return f"can not find a match"

tst_ds = TwoSumTwo()
def get_tst(_):
    print("Two Sum II - Input Array Is Sorted")
    print("happy path")
    print(tst_ds.twoSum([2,7,11,15], 9))
    print(tst_ds.twoSum([2,3,4], 6))
    print(tst_ds.twoSum([-1,0], -1))
    print(tst_ds.twoSum([1,2,3,4,5], 8))
    print(tst_ds.twoSum([5,25,75], 100))
    print(tst_ds.twoSum([3,24,50,79,88,150,345], 200))
    print(tst_ds.twoSum([1,3,4,6,7,8,9], 13))
    print(tst_ds.twoSum([-5,-1,0,3,6], 5))
    print(tst_ds.twoSum([10,20,30,40,50], 90))
    print(tst_ds.twoSum([7,11,15,20,35], 22))
    print(tst_ds.twoSum([4,9,14,19,24], 33))
    print(tst_ds.twoSum([3,10,17,24,31], 41))
    
    print()

    print("corner case")
    print(tst_ds.twoSum([1,2], 3))
    print(tst_ds.twoSum([-1000,-999,-998], -1999))
    print(tst_ds.twoSum([998,999,1000], 1999))
    print(tst_ds.twoSum([-1000,1000], 0))
    print(tst_ds.twoSum([0,0], 0))
    print(tst_ds.twoSum([1,1], 2))
    print(tst_ds.twoSum([-5,-4,-3,-2,-1], -9))
    print(tst_ds.twoSum([0,0,3,4], 0))
    print(tst_ds.twoSum([1,1,1,1,1,1,2], 3))

    print()

    print("edge case")
    edges = [
        ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], 59),
        ([-500,-400,-300,-200,-100,0,100,200,300,400,500], 0),
        ([1,1,1,1,1,1,1,1,1,2], 3),
        ([-1,-1,-1,-1,-1,0,0,0,0,1], 0),
        ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 29),
        ([-1000,-999,-998,-997,-996,-995,-994,-993,-992,-991,-990,-989,-988,-987,-986,-985,-984,-983,-982,1000], 0),
        ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 1),
        ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,1000], 1001),
        ([999,999,999,999,999,999,999,999,999,1000], 1999),
        ([500,500,500,500,500,500,500,500,500,500], 1000),
        ([0,0,0,0,0,0,0,0,0,0], 0),
        ([-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000], -2000),
        ([1,999,999,999,999,999,999,999,999,999], 1000),
        ([1,3,5,7,9,11,13,15,17,19], 4),
        ([2,4,6,8,10,12,14,16,18,20], 6),
        ([-10,-8,-6,-4,-2,0,2,4,6,8], -2),
        ([100,200,300,400,500,600,700,800,900,1000], 1100),
        ([-100,-90,-80,-70,-60,-50,-40,-30,-20,-10], -190),
        ([1,10,100,1000], 1001),
        ([3,33,333], 36),
        ([7,77,777], 84),
        ([5,50,500], 55),
        ([9,99,999], 108),
        ([11,111], 122),
        ([13,131], 144),
        ([], 5),
        ([12], _),
        ([], _),
        ([1], 2),
        ([1,2,3], 10),
        ([3,2,1], 5),
        ([1,2,3,4], 0),
        ([1001,1002], 2003),
        ([-1001,-1000], -2001),
        ([1,2,3,4], 1001),
        ([1,2,3,4], -1001),
        ([1,2,2,1], 3),
    ]

    for eCase in edges:
        try:
            find_tst = tst_ds.twoSum(*eCase)
            if find_tst != None:
                print(find_tst)
        except Exception as error_message:
            print(type(error_message).__name__.replace("Error", " error".lower(), ":", eCase))

get_tst(None)
