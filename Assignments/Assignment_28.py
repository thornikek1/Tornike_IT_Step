#დაწერეთ პროგრამა, რომელიც ქმნის ორ ძაფს (Thread) 30-დან 50-ის ჩათვლით ლუწი და კენტი რიცხვების მოსაძებნად. შედეგი დაბეჭდეთ ეკრანზე
import threading

def search_even():
    even_numbers = [num for num in range(30, 51) if num % 2 == 0]
    print("Even numbers between 30 and 50:", even_numbers)

def search_odd():
    odd_numbers = [num for num in range(30, 51) if num % 2 != 0]
    print("Odd numbers between 30 and 50:", odd_numbers)

if __name__ == "__main__":
    even_thread = threading.Thread(target=search_even)
    odd_thread = threading.Thread(target=search_odd)
    
    even_thread.start()
    odd_thread.start()
    
    even_thread.join()
    odd_thread.join()

#დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს (Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან.
import threading
import requests

def download_mp3(url, filename):
    try:
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    # List of tuples containing URLs and corresponding filenames
    mp3_files = [
        ("https://example.com/song1.mp3", "song1.mp3"),
        ("https://example.com/song2.mp3", "song2.mp3"),
        # Add more URLs and filenames as needed
    ]
    
    # Create and start a thread for each download task
    threads = []
    for url, filename in mp3_files:
        thread = threading.Thread(target=download_mp3, args=(url, filename))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

    print("All downloads completed.")
