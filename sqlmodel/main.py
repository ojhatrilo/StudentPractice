from sqlmodel import SQLModel, Field, create_engine, Session, Relationship, select

# Create an engine (connection to the database)
engine = create_engine('sqlite:///orm.db')
# engine = create_engine('sqlite:///orm.db', echo=True)

'''
Maybe clean up with a dependency like:
def get_session():
    with Session(engine) as session:
        yield session
'''

# Define the Author model
class Author(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)  # Primary Key
    name: str = Field(max_length=50)  # Name column
    email: str = Field(max_length=50)  # Email column

    # Relationship to the Book model, setting up a one-to-many relationship
    books: list["Book"] = Relationship(back_populates="author")

# Define the Book model
class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)  # Primary Key
    title: str = Field(max_length=100)  # Title column
    content: str  # Content column
    author_id: int = Field(foreign_key="author.id")  # Foreign Key linking to the Author table

    # Relationship to the Author model, completing the one-to-many relationship
    author: Author = Relationship(back_populates="books")

# Create all tables in the database (if they don't already exist)
SQLModel.metadata.create_all(engine)

# Adding sample data
with Session(engine) as session:
    author1 = Author(name='Alice', email='alice@example.com')
    author2 = Author(name='Bob', email='bob@example.com')
    book1 = Book(title='Alice’s First Book', content='This is the content of Alice’s first book.', author=author1)
    book2 = Book(title='Alice’s Second Book', content='This is the content of Alice’s second book.', author=author1)
    book3 = Book(title='Bob’s First Book', content='This is the content of Bob’s first book.', author=author2)

    session.add_all([author1, author2, book1, book2, book3])
    session.commit()
    
# Single query
with Session(engine) as session:
    statement = select(Book)
    results = session.exec(statement)
    # for book in results:
    #     print(book)
    book = results.first()
        
# List of books
with Session(engine) as session:
    statement = select(Book)
    books = session.exec(statement).all()
    print(books)
    
# Where
with Session(engine) as session:
    statement = select(Book).where(Book.title == 'Alice’s First Book')
    books = session.exec(statement).all()
    for book in books:
        print(book)


# Query to join the Book and Author tables and retrieve books with their authors
with Session(engine) as session:
    statement = select(Book, Author).join(Author)
    books_with_authors = session.exec(statement).all()

    # Print out each book's title and the name of the author
    for book, author in books_with_authors:
        print(f"Book: {book.title}, Author: {author.name}")

# Query to retrieve books authored by 'Alice'
with Session(engine) as session:
    alice = session.exec(select(Author).where(Author.name == 'Alice')).first()
    if alice:
        for book in alice.books:
            print(f"Title: {book.title}, Content: {book.content}")

# Advanced query: Joining Book and Author tables and filtering books authored by 'Alice'
with Session(engine) as session:
    statement = select(Book).join(Author).where(Author.name == 'Alice')
    filtered_books = session.exec(statement).all()

    # Print out filtered books
    for book in filtered_books:
        print(f"Title: {book.title}, Author: {book.author.name}")
        

# Update Operation: Changing the title of "Alice’s First Book"
# with Session(engine) as session:
#     book_to_update = session.exec(select(Book).where(Book.title == "Alice’s First Book")).first()
#     if book_to_update:
#         book_to_update.title = "Alice’s Updated First Book"
#         session.add(book_to_update)
#         session.commit()
#         session.refresh(book_to_update)
#         print(f"Updated Book Title: {book_to_update.title}")  # Display the updated title

# Delete Operation: Removing "Bob’s First Book"
# with Session(engine) as session:
#     book_to_delete = session.exec(select(Book).where(Book.title == "Bob’s First Book")).first()
#     if book_to_delete:
#         session.delete(book_to_delete)
#         session.commit()
#         print(f"Deleted Book titled: 'Bob’s First Book'")