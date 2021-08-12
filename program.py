from datetime import date

from marshmallow import Schema, fields


class Book(Schema):
    name = fields.Str()
    author = fields.Str()
    genre = fields.Str()
    description = fields.Str()


new_book = dict(name="Clean Code", author="Robert C. Martin",genre="Software Architecture",description="A book about writing clean and efficient code")

schema = Book()
result = schema.dump(new_book)
print(result)