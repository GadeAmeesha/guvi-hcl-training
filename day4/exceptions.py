try:
    rank=-2
    if (rank<1):
        raise  TypeError("it is less than 1")
except ZeroDivisionError:
    print("000000---")
except Exception as e :
    print(e)
finally:
    print("process done")






    name="ameesha"
    assert name=="ameesha"
    print(name)