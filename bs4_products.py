from bs4 import BeautifulSoup
import urllib3


url1 = 'https://blackfriday.com/categories/electronics'
url2 = "https://blackfriday.com/categories/clothing"
url3 = "https://blackfriday.com/categories/watches"

categoryUrl = "https://blackfriday.com/categories"

http = urllib3.PoolManager()
listOfStrings = ['Jewelry', 'TVs',
                 'Smart Watches', 'Luggage', 'Shoes & Boots']



def get_category():
    response = http.request('GET', categoryUrl)
    global categoryList
    categoryList = []
    category_soap = BeautifulSoup(response.data, "html.parser")
    for tr in category_soap.find_all("div", {"class": "pure-u-1-2"}):
        cat_dict = {}
        cat_dict['category'] = tr.find("a").text.strip()
        cat_dict['url'] = tr.find("a")['href']
        if cat_dict['category'] in listOfStrings:
            categoryList.append(cat_dict)
    return categoryList
    




def product_by_category(item=0):
    product = []
    url = categoryList[item]['url']
    response = http.request('GET', url)

    soup = BeautifulSoup(response.data, "html.parser")
    for tr in soup.findAll("div", {"class": "commerce-card"}):
        pro_dict = {}
        pro_dict['img'] = tr.find("img")['src']
        pro_dict['title'] = tr.find("p").text.strip()
        pro_dict['brand'] = tr.find("div", {"class", "merchant"}).text.strip()
        price = tr.find("a", {"class": "deal-price"}).text.strip() if tr.find(
            "div", {"class": "price"}) != None else ''
        pro_dict['price'] = price.split('\n')[0]
        pro_dict['deal-price'] = price.split(
            '\n')[1] if len(price.split('\n')) > 1 else ''
        product.append(pro_dict)
    return product

