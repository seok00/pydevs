from TopLevelModel import TopLevelModel
from Book import Book
from Person import Person

experimental_frame = TopLevelModel("EF")
experimental_frame.time_limit = 356.0

person = Person("person")
book = Book("book")

experimental_frame.sub_model_list = [person, book]
experimental_frame.add_coupling(
    "request", person, "request", book
)
experimental_frame.add_coupling(
    "return", person, "return", book
)
experimental_frame.run_simulation()
