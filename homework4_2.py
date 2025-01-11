def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


# нельзя вызвать функцию inner_function() так как она находится только в пространстве test_function()

test_function()