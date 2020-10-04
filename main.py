from bs4 import BeautifulSoup
import requests, shutil, os, img2pdf

def catch_chapter(start, end):
    for i in range(start, end+1):
        # enter manga page url: note the slash at the end of url
        manga_url = "https://kissmanga.in/kissmanga/immortal-invincible-manga123/"
        url = manga_url +"chapter-"+str(i)+"/"
        page =  requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        pages = []
        manga_name = soup.find("title").text.split('-')[0]
        if not os.path.exists(manga_name):
            os.mkdir(manga_name)
        #get pages of chapter
        for item in soup.findAll("img", {"class": "wp-manga-chapter-img"}):
            if(item.has_attr('src')):
                pages.append(item['src'].strip())
        #download pages
        chapter = manga_name+"/"+url.split('/')[-2]
        if not os.path.exists(chapter):
            os.mkdir(chapter)
        images = []
        print("started: "+chapter)
        for image in pages:
            filename = image.split('/')[-1]
            r = requests.get(image, stream = True)
            if(r.status_code == 200):
                r.raw.decode_content = True
                images.append(chapter+"/"+filename)
                with open(chapter+"/"+filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            else:
                None
        # store pages in pdf format
        pdf_name = chapter+".pdf"
        with open(chapter+".pdf","wb") as f:
            f.write(img2pdf.convert(images))
        print("downloaded: "+chapter)
        #clean-up
        shutil.rmtree(chapter, ignore_errors=True)


# enter starting and ending chapter number -> for 1 chapter  enter same value
start = 1
last = 108
#call function for all chapters
catch_chapter(start, last)