import requests
import json

if __name__ == '__main__':
    with open('prologue.md', 'r') as handle:
        prologue = handle.read()
    quote = lambda s: '`%s`' % s
    proxies =  { 
        'http': 'socks5://localhost:1080',
        'https': 'socks5://localhost:1080'
    }
    url = 'https://summerofcode.withgoogle.com/api/program/current/organization/?page=1&page_size=50'
    output = open('README.md', 'w', encoding='utf-8')
    output.write(prologue)
    while url is not None:
        obj = requests.get(url, proxies=proxies).json()
        url = obj['next']
        for item in obj['results']:
            output.write('\n## [%s](%s)\n' % (item['name'], item['website_url']))
            output.write('\n**%s**\n' % item['precis'])
            output.write('\n### Metadata\n')
            output.write('\n[View ideas list](%s)\n' % item['ideas_list'])
            output.write('\n* Category: ' + item['category'])
            output.write('\n* Techonology: %s' % ', '.join(map(quote, item['technology_tags'])))
            output.write('\n* Topics: %s' % ', '.join(map(quote, item['topic_tags'])))
            output.write('\n* Tags: %s' % ', '.join(map(quote, item['proposal_tags'])))
            if item['contact_method'] is not None:
                output.write('\n* Contact: %s' % item['contact_method'])
            if item['mailing_list'] is not None:
                output.write('\n* Mailing List: %s' % item['mailing_list'])
            if item['twitter_url'] is not None:
                output.write('\n* Twitter: %s' % item['twitter_url'])
            if item['blog_url'] is not None:
                output.write('\n* Blog: %s' % item['blog_url'])
            if item['primary_open_source_license'] is not None:
                output.write('\n* Primary Open Source License: %s' % item['primary_open_source_license'])
            output.write('\n')
            output.write('\n### Description\n')
            output.write('\n%s\n' % item['description'])
            if item['application_instructions'] is not None:
                output.write('\n### Application Instructions\n')
                output.write('\n* Twitter: %s' % item['application_instructions'])
    print('Done.')
