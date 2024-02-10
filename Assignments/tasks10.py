# # მოთხოვნის გაგზავნა და სტატუსის შემოწმება
import requests

def get_data ():
  try:
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)

    print(response.status_code)
    # მიღებული სიის პითონის ლისტად გადაყვანა და დაბეჭდვა
    if response.status_code == 200:
      received_data_list = []
      received_data_list.append(response.json())
      print (received_data_list)

      return response.json()
  except requests.exceptions.HTTPError as http_err:
    print(f"Http error: {http_err}")
  except requests.exceptions.ConnectionError as con_err:
    print(f"Connection error: {con_err}")
  except Exception as err:
    print(f"Something wrong. {err}")

# ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები
products = get_data ()
prices = [product['price'] for product in products]
max_price = max(prices)
min_price = min(prices)
avg_price = sum(prices) / len(prices)
print(f"Maximum Price: {max_price}")
print(f"Minimum Price: {min_price}")
print(f"Average Price: {avg_price}")

# ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ
categories = sorted(set(product['category'] for product in products))
print(f"\nSorted Categories: {categories}")

# გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით
product_info = sorted([(product['title'], product['id']) for product in products], key=lambda x: x[0])
print("\nProduct Info (Sorted by Title):")
for title, product_id in product_info:
    print(f"{title} - ID: {product_id}")

# დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით
ratings = sorted([product['rating']['rate'] for product in products])
print(f"\nSorted Ratings: {ratings}")