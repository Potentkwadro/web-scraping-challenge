from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit visitcostarica.herokuapp.com



def scrape():
    browser = init_browser()

    #Mars News
    mimage_image_url = "https://spaceimages-mars.com/"
    browser.visit(mimage_image_url)
    html = browser.html
    soup = bs(html, 'lxml')

    title = soup.find('div', class_="content_title")
    title_text = title.a.text
    title_text = title_text.strip()
    news_p = soup.find("div", class_="rollover_description_inner")
    news_text = news_p.text
    news_text = news_text.strip()

    #Featured Photo
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    html2 = browser.html
    soup2 = bs(html2, 'html.parser')

    results = soup2.find("ul", class_="articles")
    href = results.find("a",class_='fancybox')['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov' + href


    #Dictionary of all Mars Info Scraped
    mars_info_dict = {"news_title":title_text,"news_text":news_text,"featured_image":featured_image_url,
    "mars_weather":mars_weather,"facts_table":facts_html,"hemisphere_img":hemisphere_image_urls}

    browser.quit()

    return mars_info_dict
