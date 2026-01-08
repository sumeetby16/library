
from library import bookdetails

def test_lib():
    op = (
        "book id:1001\n"
        "book title:jurasic park\n"
        "author name:veeresh\n"
        "Year of publication:1999\n"
    )
    assert bookdetails(1001, "jurasic park", "veeresh", 1999) == op
