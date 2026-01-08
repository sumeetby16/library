from library import bookdetails
def test_lib():
    op=(
        f"book id:id\n"
        f"book title:title\n"
        f"author name:name\n"
        f"Year of publication:publication\n"
        )
    assert bookdetails (1001,"jurasic park","veeresh",1999) == op