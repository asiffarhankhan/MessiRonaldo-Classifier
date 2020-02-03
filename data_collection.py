import os
import requests
import time

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
m_path = os.path.join('dataset/messi_images_link.txt')
r_path = os.path.join('dataset/ronaldo_images_link.txt')
m_total = 1
r_total = 1

for url in open(r_path):

    try:
        r = requests.get(url,headers={'User-Agent': user_agent}, timeout = 60)
        path = open('dataset/train/ronaldo/ronaldo_{}.jpeg'.format(r_total),'wb')
        path.write(r.content)
        print('[SUCCESS] downloadead file: ronaldo_{}'.format(r_total))
        path.close()

    except Exception as e:
        print('\nERROR: ronaldo_{} could not be downloaded\n'.format(r_total))
        print('\n',e)

    finally:
        r_total += 1

for url in open(m_path,'rb'):
    
    try:
        r = requests.get(url, headers={'User-Agent': user_agent}, timeout = 60)
        path = open('dataset/train/messi/messi_{}.jpeg'.format(m_total),'wb')
        path.write(r.content)
        print('[SUCCESS] downloadead file: messi_{}'.format(m_total))
        path.close()

    except Exception as e:
        print('\nERROR: messi_{} could not be downloaded\n'.format(m_total))
        print('\n',e)

    finally:
        m_total += 1