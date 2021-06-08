tomato_soup=["tomato","garlic","onion","butter"]
tomato_rice=["tomato","rice"]
biryani=["rice","chicken","onion","ghee"]

tag_line=("choose your ingredients:'tomato' ,'garlic' ,'onion' ,'rice','butter' ,'ghee' ,'butter'")
print(tag_line)
while True:
    a=input("type your ingredient here :")
    if a in tomato_soup:
        print("tomato soup")
    if a in tomato_rice:
        print("tomato rice")
    if a in biryani:
        print("biryani")    

print(tag_line)

