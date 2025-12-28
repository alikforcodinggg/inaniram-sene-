
def shipping_label(*args, **kwargs):
   
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print (args)
        
    
shipping_label("123 Main St", "Apt 4B", city="New York", state="NY", zip="10001")
shipping_label("123 Main St", "Apt 4B", city="New York", state="NY", zip="10001", country="USA"     )
