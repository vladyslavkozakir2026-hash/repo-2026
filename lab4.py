### Повністю виправлений та працюючий код:
class Book:
    def __init__(self, pages=0, author="Невідомий", price=0.0, rating=0.0, title="Без назви"):
        self.__pages = pages
        self.__author = author
        self.__price = price

        self.rating = rating
        self.title = title

    # ------- гетери (доступ) -------
    def get_pages(self):
        return self.__pages
    
    def get_author(self):
        return self.__author
    
    def get_price(self):
        return self.__price
    
    # ------- сетери (зміна даних) -----  
    def set_pages(self, pages):
        if pages >= 0:
            self.__pages = pages
        else:
            print("Помилка: Кількість сторінок не може бути від'ємною!")
    
    def set_author(self, author):
        self.__author = author
    
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Помилка: ціна не може бути від'ємною!")

    def __str__(self):
        return f"Книжка '{self.title}' (Автор: {self.__author}, сторінок: {self.__pages}, ціна: {self.__price} грн, рейтинг: {self.rating})"

    def __repr__(self):
        return f"Book(pages={self.__pages}, author='{self.__author}', price={self.__price}, rating={self.rating}, title='{self.title}')"

    def __del__(self):
        print(f"[Деструктор] : об'єкт книжки '{self.title}' видалено з пам'яті")
    
    def __sub__(self, other):
        if(isinstance(other,(int, float))):
            return max(0.0, self.__price-other)
        return NotImplemented

    def __gt__(self, other):
        if(isinstance(other, Book)):
            return self.rating>other.rating
        return False

def main():
    book1 = Book()
    book2 = Book(285, "Джонні Сінс", 300.0, 4.9, "The art of multitasking")
    book3 = Book(450, "Анджей Сапковський", 190.0, 4.5, "Відьмак. Володарка Озера")

    books = [book1, book2, book3]

    for i, book in enumerate(books, start=1):
        print(f"--- Об'єкт {i} ---")

        # --- str та repr
        print("str:", str(book))
        print("repr:", repr(book))

        # --- private attributes
        print(f"Кількість сторінок: {book.get_pages()}")
        print(f"Автор: {book.get_author()}")
        print(f"Ціна: {book.get_price()}")
        
        # --- public attributes
        print("Назва:", book.title)
        print("Рейтинг:", book.rating)
        print()
    
    print(book2 - 299)

    print(book2 > book3)

if __name__ == "__main__":
    main()
