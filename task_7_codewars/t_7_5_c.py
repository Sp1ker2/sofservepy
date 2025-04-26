def reverse(st:str):
    el = st.split()
    el.reverse()
    return " ".join(el)
print(reverse("This is an example!"))