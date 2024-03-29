import requests
from parsel import Selector

url_base = "http://books.toscrape.com/"
response = requests.get(url_base)
selector = Selector(text=response.text)

# print(selector.css("img.thumbnail").get())

# for thumbnail in selector.css("img.thumbnail").getall():
#     print(thumbnail)

# print(selector.css('div.image_container a').get())

# O título está no atributo title em um elemento âncora (<a>)
# Dentro de um h3 em elementos que possuem classe product_pod
titles = selector.css(".product_pod h3 a::attr(title)").getall()
# Estamos utilizando a::attr(title) para capturar somente o valor contido no texto do seletor

# Os preços estão no texto de uma classe price_color
# Que se encontra dentro da classe .product_price
prices = selector.css(".product_price .price_color::text").getall()

# Combinando tudo podemos buscar os produtos
# em em seguida buscar os valores individualmente
for product in selector.css(".product_pod"):
    title = product.css("h3 a::attr(title)").get()
    price = product.css(".price_color::text").get()
    print(title, price)
