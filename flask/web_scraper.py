from bs4 import BeautifulSoup
import urllib.request
import json

poems = {}

titles_2 = []

with urllib.request.urlopen('http://www.thehypertexts.com/Best%20Love%20Poems.htm') as response:
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    titles_2 = [poem.text for poem in soup.find_all("em")]
    text_2 = [poem.text for poem in soup.find_all("body")]
    
    
i = 1
for title, text in zip(titles_2, text_2):
    poems[str(i)]= {
    "title": title,
    "author": "Unknown",
    "poem": text
    }
    i +=1

#print(titles_2, text_2)

with urllib.request.urlopen('http://users.telenet.be/gaston.d.haese/shakespeare.html') as response:
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    titles_3 = [poem.text for poem in soup.find_all("h2")]
    text_3 = [poem.text for poem in soup.find_all("font")]

text_3 = text_3[7:-9]
for element in text_3:
    if element == "Upward":
        text_3.remove(element)

for title, text in zip(titles_3, text_3):
    poems[str(i)]= {
    "title": title,
    "author": "William Shakespeare",
    "poem": text
    }
    i +=1

print(titles_3, text_3)

rumi_text = []

with urllib.request.urlopen('http://www.rumi.org.uk/love_poems.html') as response:
    html = response.read()
    soup = BeautifulSoup(html, "lxml")

    rumi_text = [poem.text.strip() for poem in soup.find_all("blockquote")]

#print(rumi_text)

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
#print(titles)
texts = texts[2:]
#print(texts)


for title, text in zip(titles, texts):
    poems[str(i)]= {
    "title": title,
    "author": "William Butler Yeats",
    "poem": text
    }
    i +=1

poem_json = json.dumps(poems)

with open("./scraped.json", "w") as f:
    f.write(poem_json)