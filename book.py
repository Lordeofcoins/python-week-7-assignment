class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages  # Encapsulated attribute

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def get_pages(self):
        return self._pages

    def set_pages(self, pages):
        if pages > 0:
            self._pages = pages
        else:
            print("Page count must be positive.")

class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size}MB).")

# Example usage:
book1 = Book("1984", "George Orwell", 328)
ebook1 = EBook("Digital Fortress", "Dan Brown", 356, 2)

book1.read()
ebook1.read()
ebook1.download()