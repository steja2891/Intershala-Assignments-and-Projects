class Book:
    def __init__(self, author="SAITEJA", title="Life of a Monk", publisher="McGrawHill", price=5000, copies=1500):
        self.book_name = author
        self.book_title = title
        self.publisher_name = publisher
        self.book_price = price
        self.book_copies = copies
        self.royalty_price = 0

    def get_book_name(self):
        return self.book_name

    def set_book_name(self, author):
        self.book_name = author
        return

    author_name = property(get_book_name, set_book_name)

    def get_book_title(self):
        return self.book_title

    def set_book_title(self, title):
        self.name = title
        return

    tile_name = property(get_book_title, set_book_title)

    def get_publisher_name(self):
        return self.publisher_name

    def set_publisher_name(self, publisher):
        self.publisher_name = publisher
        return

    name_of_publisher = property(get_publisher_name, set_publisher_name)

    def get_book_price(self):
        return self.book_price

    def set_book_price(self, price):
        self.book_price = price
        return

    bookprice = property(get_book_price, set_book_price)

    def get_book_copies(self):
        return self.book_copies

    def set_book_copies(self, copies):
        self.book_copies = copies
        return

    bookcopies = property(get_book_copies, set_book_copies)

    def royalty(self):
        if self.book_copies <= 500:
            self.royalty_price += 500 * self.book_price * 10 / 100
        if self.book_copies <= 1500:
            self.royalty_price += (self.book_copies - 500) * self.book_price * 12.5 / 100
        if self.book_copies > 1500:
            self.royalty_price += (self.book_copies - 1500) * self.book_price * 15 / 100
        return self.royalty_price


class eBook(Book):
    def __init__(self, author="SAITEJA", title="Life of a Monk", publisher="McGrawHill", price=5000, copies=1500,
                 fileformat=None):
        super().__init__(author, title, publisher, price, copies)
        self.ebook_format = fileformat

    def get_ebook_format(self):
        return self.get_ebook_format

    def set_ebook_format(self, fileformat):
        self.ebook_format = fileformat
        return

    ebookformat = property(get_ebook_format, set_ebook_format)

    def royalty(self):
        if self.ebook_format == None:
            if self.book_copies <= 500:
                self.royalty_price += 500 * self.book_price * 10 / 100
            if self.book_copies <= 1500:
                self.royalty_price += (self.book_copies - 500) * self.book_price * 12.5 / 100
            if self.book_copies > 1500:
                self.royalty_price += (self.book_copies - 1500) * self.book_price * 15 / 100
            return self.royalty_price

        else:
            self.royalty_price = self.book_price - 12 / 100
            return self.royalty_price


if __name__ == "__main__":
    print("Details of Normal Book format: ")
    b = Book()
    print(b.royalty())
    b = Book("Suryateja", "MyLove", "SS Publications", 1000, 2000)
    print(b.royalty())
    print("Details of E-Book format: ")
    eb = eBook()
    print(eb.royalty())
    eb = eBook("Krishna", "An Endless story", "Sai Publications", 10000, 200, "PDF")
    print(eb.royalty())
