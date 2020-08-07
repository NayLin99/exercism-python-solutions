def two_fer(name="you"):
    try:
        return f"One for {name}, one for me."
    except TypeError as error:
        return "Data Type Error"
