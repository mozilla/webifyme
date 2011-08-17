# -*- coding: utf-8 -*-
import re
from django.utils.translation import ugettext as _


def get_community_object(referral_domain):
    community_objects = {
        'digg': {
            'name': 'DIGG Button',
            'tooltip': _(u'Now this is trending. Can you Digg it? I knew you could.'),
            'file_name': '1755_site_0149.png'
        },
        'reddit': {
            'name': 'Reddit Button',
            'tooltip': _(u'Change is happening, and you can be part of it right now.'),
            'file_name': '1755_site_0150.png'
        },
        'stumbleupon': {
            'name': 'Stumbleupon Button',
            'tooltip': _(u'Oh hey, look at that. This internet really is a vast, all-encompassing thing where anything is possible, isn’t it?'),
            'file_name': '1755_site_0151.png'
        },
        'facebook': {
            'name': 'Facebook Button',
            'tooltip': _(u'You “Like” us, you really, really “Like” us! (Hey, we like you, too.) Thank you for being a friend.'),
            'file_name': '1755_site_0152.png'
        },
        'twitter': {
            'name': 'Twitter Button',
            'tooltip': _(u'140 characters isn’t enough to say how glad we are to count you among our followers. We think of you more as a “walk-besider”'),
            'file_name': '1755_site_0153.png'
        },
        'buzzfeed': {
            'name': 'Buzzfeed Button',
            'tooltip': _(u'LOL OMG WTF! You, dear friend, are an expert at virulence, and you grace us with your very presence. Tell your friends!'),
            'file_name': '1755_site_0154.png'
        },
        'slashdot': {
            'name': 'Slashdot Button',
            'tooltip': _(u'”You’re a Super Geek! Super Geek! You’re Super Geeky.” At least that’s what Rick James would say, if he knew you.'),
            'file_name': '1755_site_0155.png'
        },
        'qq': {
            'name': 'QQ Button',
            'tooltip': _(u'200 million users can’t be wrong. Make that 250 million. '),
            'file_name': '1755_site_0156.png'
        },
        'orkut': {
            'name': 'Orkut Button',
            'tooltip': _(u'Social networking, with a really nice tan.'),
            'file_name': '1755_site_0157.png'
        },
        'frrvrr': {
            'name': 'Frrvrr Button',
            'tooltip': _(u'Start the Conversation!'),
            'file_name': '1755_site_0178.png'
        }
    }

    if referral_domain:
        for domain in community_objects:
            x = re.search(domain, referral_domain)
            if x:
                return community_objects[domain]
                break
        return False


def get_browser_object(user_agent_string):

    search_strings = [
        ('Firefox/4.0b', 'firefox-beta'),
        ('Firefox/3', 'firefox'),
        ('Chrome', 'chrome'),
        ('Safari', 'safari'),
        ('MSIE', 'ie')
    ]

    browser_objects = {
        'firefox-beta': {
            'name': 'Firefox Necklace',
            'tooltip': _(u'Oh hey, what’s up Firefox Beta user? Thank you for all of your help, your feedback has been invaluable.  Here’s a special totem, just for you.'),
            'file_name': '1755_site_0168.png'
        },
        'firefox': {
            'name': 'Toy Robot',
            'tooltip': _(u'Hello intrepid Firefox 3 user! You’ve been with us for a long time, and we’re excited to share the new Firefox with you. Until then, accept this trusty robot as a symbol of our appreciation.'),
            'file_name': '1755_site_0169.png'
        },
        'safari': {
            'name': 'Toy Compass',
            'tooltip': _(u'Hi Safari user! We’re glad you came by to check out what’s new in Firefox &mdash; give the snappier browser a shot, you’ll like life in the fast lane. Until then, please accept this compass, you Internet Magellan.'),
            'file_name': '1755_site_0170.png'
        },
        'chrome': {
            'name': 'Chrome Rock',
            'tooltip': _(u'Howdy Chrome user! Glad you came by to check out our shiny new browser. Give Firefox a shot; you’ll like life in the faster lane. Until then, here’s a nice chrome stone just for you.'),
            'file_name': '1755_site_0171.png'
        },
        'ie': {
            'name': 'Dinosaur toy',
            'tooltip': _(u'Internet Explorer! You sure are. Glad you’re here, checking out Mozilla Firefox. We hope this means you’ll give a new browser a try. Here’s a completely unrelated totem, in the meantime.'),
            'file_name': '1755_site_0172.png'
        }
    }

    browser_code = False

    for regex, browser in search_strings:
        result = re.search(regex, user_agent_string)
        if result:
            browser_code = browser
            break

    if browser_code in browser_objects:
        return browser_objects[browser_code]
    return False


def get_easter_egg(email_address):
    email_objects = {
        'mozilla.com': {
            'name': 'Mozilla Sticker',
            'tooltip': _(u'Yes you did. And this is the reward.'),
            'file_name': '1755_site_0195.png'
        },
        'barbariangroup.com': {
            'name': 'Swedish Fish™',
            'tooltip': _(u'Heeey Barbarian. It’s gonna be awesome™!'),
            'file_name': '1755_site_0173.png'
        },
        'google.com': {
            'name': 'Binoculars',
            'tooltip': _(u'We think “don’t be evil” is about the best advice we’ve ever heard.'),
            'file_name': '1755_site_0174.png'
        },
        'microsoft.com': {
            'name': 'Paper Clippy',
            'tooltip': _(u'It looks like you’re taking an Internet Quiz. Do you need help with that?'),
            'file_name': '1755_site_0175.png'
        },
        'apple.com': {
            'name': 'Apple',
            'tooltip': _(u'May this Apple never tarnish. Nice of you to come visit.'),
            'file_name': '1755_site_0176.png'
        },
        'gizmodo.com': {
            'name': 'Mystery Box',
            'tooltip': _(u'This is like a nerd Rorschach test. You KNOW what’s in the box.'),
            'file_name': '1755_site_0177.png'
        },
        'engadget.com': {
            'name': 'Mystery Box',
            'tooltip': _(u'This is like a nerd Rorschach test. You KNOW what’s in the box.'),
            'file_name': '1755_site_0177.png'
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
            'tooltip': _(u'Quick: look out your window. Any purple mountains’ majesty? Amber waves of grain? We wouldn’t be surprised, because you’re in the U-S-A!'),
            'file_name': '1755_site_0139.png'
        },
        'br': {
            'name': 'Figa',
            'tooltip': _(u'A powerful gift that brings good fortune &mdash; that’s exactly what we hope to bring to you.'),
            'file_name': '1755_site_0140.png'
        },
        'de': {
            'name': 'Berlin Charm',
            'tooltip': _(u'Once a symbol of division, the Brandenburg Gate now stands for unity and a new beginning.'),
            'file_name': '1755_site_0141.png'
        },
        'es': {
            'name': 'The Bull',
            'tooltip': _(u'There’s a reason they say “strong like ox” &mdash; it’s the symbol of pure, unrelenting power.'),
            'file_name': '1755_site_0142.png'
        },
        'fr': {
            'name': 'The Eiffel Tower',
            'tooltip': _(u'Hey, we’re French. What did you expect, cheese?'),
            'file_name': '1755_site_0143.png'
        },
        'gb': {
            'name': 'London Bus',
            'tooltip': _(u'Oh, how I wish we still had those lovely old busses, with a platform you could just hop on and off from. We didn’t fall, much.'),
            'file_name': '1755_site_0144.png'
        },
        'ru': {
            'name': 'Matryoshka Doll',
            'tooltip': _(u'A fitting symbol for both Russia and the Internet, the Matryoshka is beloved by young and old alike and tourists are pretty hot for it too.'),
            'file_name': '1755_site_0145.png'
        },
        'it': {
            'name': 'Corno Gobbo',
            'tooltip': _(u'A powerful lucky charm that covers all the angles &mdash; rub his hump for good luck!'),
            'file_name': '1755_site_0146.png'
        },
        'cn': {
            'name': 'Jade Dragon',
            'tooltip': _(u'The Jade guards you with its formidable powers, and brings luck to your abode.'),
            'file_name': '1755_site_0147.png'
        },
        'pl': {
            'name': 'National Patch',
            'tooltip': _(u'Proud symbol of our land, the majestic eagle has persevered through the ages and withstood many a test. '),
            'file_name': '1755_site_0148.png'
        }
    }
    if country_code in country_objects:
        return country_objects[country_code]
    return False
