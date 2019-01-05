 from bs4 import BeautifulSoup
import urllib.request
import csv

'''
csv_file = open("poems1.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "Text"])
'''
titles_2 = []

with urllib.request.urlopen('http://www.thehypertexts.com/Best%20Love%20Poems.htm') as response:
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    titles_2 = [poem.text for poem in soup.find_all("em")]
    text_2 = [poem.text for poem in soup.find_all("body")]
    #for poem in text_2 
    

print(titles_2, text_2)
'''
rumi_text = []

with urllib.request.urlopen('http://www.rumi.org.uk/love_poems.html') as response:
    html = response.read()
    soup = BeautifulSoup(html, "lxml")

    rumi_text = [poem.text.strip() for poem in soup.find_all("blockquote")]

print(rumi_text)

titles = []
texts = []

with urllib.request.urlopen('https://celt.ucc.ie//published/E900041-001.html') as response2:
    html2 = response2.read()
    soup2 = BeautifulSoup(html2, "lxml")

    for poem in soup2.find_all("h3"):
        title = poem.text
        titles.append(title)

    for poem in soup2.find_all("ol"):
        text = poem.text
        texts.append(text)
        
titles = titles[6:]
print(titles)
texts = texts[2:]
print(texts)

for x,y in zip(titles, texts):
    csv_writer.writerow([x,y])
    
csv_file.close()
'''