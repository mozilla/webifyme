# -*- coding: utf-8 -*- 
import re

def get_community_object(referral_domain):
    community_objects = {
        'digg': {
            'name': 'DIGG Button',
            'tooltip': """Now this is trending. Can you Digg it? I knew you could.""",
            'file_name': '1755_Site_0149.png'
        },
        'reddit': {
            'name': 'Reddit Button',
            'tooltip': """Change is happening, and you  can be part of it right now .""",
            'file_name': '1755_Site_0150.png'
        },
        'stumbleupon': {
            'name': 'Stumbleupon Button',
            'tooltip': """Oh hey, look at that. This internet really is a vast, all-encompassing thing where anything is possible, isn’t it?""",
            'file_name': '1755_Site_0151.png'
        },
        'facebook': {
            'name': 'Facebook Button',
            'tooltip': """You “Like” us, you really, really “Like” us! (Hey, we like you, too.) Thank you for being a friend.""",
            'file_name': '1755_Site_0152.png'
        },
        'twitter': {
            'name': 'Twitter Button',
            'tooltip': """140 characters isn’t enough to say how glad we are to count you among our followers. We think of you more as a “walk-besider”""",
            'file_name': '1755_Site_0153.png'
        },
        'buzzfeed': {
            'name': 'Buzzfeed Button',
            'tooltip': """LOL OMG WTF! You, dear friend, are an expert at virulence, and you grace us with your very presence. Tell your friends!""",
            'file_name': '1755_Site_0154.png'
        },
        'slashdot': {
            'name': 'Slashdot Button',
            'tooltip': """”You’re a Super Geek! Super Geek! You’re Super Geeky.” At least that’s what Rick James would say, if he knew you.""",
            'file_name': '1755_Site_0155.png'
        },
        'qq': {
            'name': 'QQ Button',
            'tooltip': """200 million users can’t be wrong. Make that 250 million. """,
            'file_name': '1755_Site_0156.png'
        },
        'orkut': {
            'name': 'Orkut Button',
            'tooltip': """Social networking, with a really nice tan.""",
            'file_name': '1755_Site_0157.png'
        },
        'frrvrr': {
            'name': 'Frrvrr Button',
            'tooltip': """Start the Conversation!""",
            'file_name': '1755_Site_0178.png'
        }
    }
    
    if referral_domain:
        for domain in community_objects:
            x = re.search(domain, referral_domain)
            if x:
                return community_objects[domain]
                break;
        return False
        
        
        
def get_browser_object(user_agent_string):
    
    search_strings = [
        ('Firefox/4.0b', 'firefox-beta'),
        ('Firefox/3', 'firefox'),
        ('Safari', 'safari'),
        ('MSIE', 'ie'),
        ('Chrome', 'chrome')
    ]
    
    browser_objects = {
        'firefox-beta': {
            'name': 'Firefox Necklace',
            'tooltip': """Oh hey, what’s up Firefox Beta user? Thank you for all of your help, your feedback has been invaluable.  Here’s a special totem, just for you.""",
            'file_name': '1755_Site_0168.png'
        },
        'firefox': {
            'name': 'Toy Robot',
            'tooltip': """Hello intrepid Firefox 3 user! You’ve been with us for a long time, and we’re excited to share Firefox 4 with you. Until then, accept this trusty robot as a symbol of our appreciation.""",
            'file_name': '1755_Site_0169.png'
        },
        'safari': {
            'name': 'Toy Compass',
            'tooltip': """Hi Safari user! We’re glad you came by to check out what’s new in Firefox 4 - give the snappier browser a shot, you’ll like life in the fast lane. Until then, please accept this compass, you Internet Magellan.""",
            'file_name': '1755_Site_0170.png'
        },
        'chrome': {
            'name': 'Chrome Rock',
            'tooltip': """Howdy Chrome user! Glad you came by to check out our shiny new browser. Give Firefox 4 a shot; you’ll like life in the faster lane. Until then, here’s a nice chrome stone just for you.""",
            'file_name': '1755_Site_0171.png'
        },
        'ie': {
            'name': 'Dinosaur toy',
            'tooltip': """Internet Explorer! You sure are. Glad you’re here, checking out Mozilla Firefox. We hope this means you’ll give a new browser a try. Here’s a completely unrelated totem, in the meantime.""",
            'file_name': '1755_Site_0172.png'
        }
    }
    
    browser_code = False
    
    for regex, browser in search_strings:
        result = re.search(regex, user_agent_string)
        if result:
            browser_code = browser
            break;

    if browser_code in browser_objects:
        return browser_objects[browser_code]
    return False




def get_easter_egg(email_address):
    email_objects = {
        'mozilla.com': {
            'name': 'Mozilla Sticker',
            'tooltip': """Yes you did. And this is the reward.""",
            'file_name': '1755_Site_0195.png'
        },
        'barbariangroup.com': {
            'name': 'Swedish Fish™',
            'tooltip': """Heeey Barbarian. It’s gonna be awesome™!""",
            'file_name': '1755_Site_0173.png'
        },
        'google.com': {
            'name': 'Binoculars',
            'tooltip': """We think “don’t be evil” is about the best advice we’ve ever heard.""",
            'file_name': '1755_Site_0174.png'
        },
        'microsoft.com': {
            'name': 'Paper Clippy',
            'tooltip': """It’s looks like you’re taking an Internet Quiz. Do you need help with that?""",
            'file_name': '1755_Site_0175.png'
        },
        'apple.com': {
            'name': 'Apple',
            'tooltip': """May this Apple never tarnish. Nice of you to come visit.""",
            'file_name': '1755_Site_0176.png'
        },
        'gizmodo.com': {
            'name': 'Mystery Box',
            'tooltip': """This is like a nerd Rorschach test. You KNOW what’s in the box.""",
            'file_name': '1755_Site_0177.png'
        },
        'engadget.com': {
            'name': 'Mystery Box',
            'tooltip': """This is like a nerd Rorschach test. You KNOW what’s in the box.""",
            'file_name': '1755_Site_0177.png'
        }
    }
    
    clean_domain = re.search('(\w+).com', email_address)
    if clean_domain:
        if clean_domain.group(0) in email_objects:
            return email_objects[clean_domain.group(0)]
    return False
    
    
def get_country_object(country_code):
    country_objects = {
        'en': {
            'name': 'Statue of Liberty',
            'tooltip': """Quick: look out your window. Any purple mountains’ majesty? Amber waves of grain? We wouldn’t be surprised, because you’re in the U-S-A!""",
            'file_name': '1755_Site_0139.png'
        },
        'br': {
            'name': 'Figa',
            'tooltip': """A powerful gift that brings good fortune - that’s exactly what we hope to bring to you.""",
            'file_name': '1755_Site_0140.png'
        },
        'de': {
            'name': 'Berlin Charm',
            'tooltip': """Once a symbol of division, the Brandenburg Gate now stands for unity and a new beginning.""",
            'file_name': '1755_Site_0141.png'
        },
        'es': {
            'name': 'The Bull',
            'tooltip': """There’s a reason they say “strong like ox” - it’s the symbol of pure, unrelenting power.""",
            'file_name': '1755_Site_0142.png'
        },
        'fr': {
            'name': 'The Eiffel Tower',
            'tooltip': """Hey, we’re French. What did you expect, cheese?""",
            'file_name': '1755_Site_0143.png'
        },
        'gb': {
            'name': 'London Bus',
            'tooltip': """Oh, how I wish we still had those lovely old busses, with a platform you could just hop on and off from. We didn’t fall, much.""",
            'file_name': '1755_Site_0144.png'
        },
        'ru': {
            'name': 'Matryoshka Doll',
            'tooltip': """A fitting symbol for both Russia and the Internet,the Matryoshka is beloved by young and old alike and tourists are pretty hot for it too.""",
            'file_name': '1755_Site_0145.png'
        },
        'it': {
            'name': 'Corno Gobbo',
            'tooltip': """A powerful lucky charm that covers all the angles - rub his hump for good luck!""",
            'file_name': '1755_Site_0146.png'
        },
        'cn': {
            'name': 'Jade Dragon',
            'tooltip': """The Jade guards you with its formidable powers, and brings luck to your abode.""",
            'file_name': '1755_Site_0147.png'
        },
        'pl': {
            'name': 'National Patch',
            'tooltip': """Proud symbol of our land, the majestic eagle has persevered through the ages and withstood many a test. """,
            'file_name': '1755_Site_0148.png'
        }
    }
    if country_code in country_objects:
        return country_objects[country_code]
    return False