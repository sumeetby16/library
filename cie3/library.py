def bookdetails(id,title,name,publication):
    return(
        f"book id:{id}\n"
        f"book title:{title}\n"
        f"author name:{name}\n"
        f"Year of publication:{publication}\n"
        )

if __name__== "__main__":
    id=1001
    title="jurasic park"
    name="veeresh"
    publication=1999

    res= bookdetails(id,title,name,publication)
    print(res)