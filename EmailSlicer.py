
while True:
    print("\nWelcome to the Email slicer.")
    email = input("\nEnter your Email : ")

    username, domain = email.split('@')

    domain_parts = domain.split(".")
    domain_name = domain_parts[0]
    tld = domain_parts[1]

    print(f"Username : {username}")
    print(f"Domain  : { domain}")
    print(f"Domain name : {domain_name}")
    print(f"Tld : {tld}")

    popular_domain = ["hotmail", "yahoo", "outlook", "gmail"]
    if domain_name in popular_domain:
        print("This is popular doamin.")

    username = len(username)
    domain = len(domain)
    total = username + domain
    print(f"Total length {total}")


    slice_again = input("\nSlice again (yes/no :)")
    if slice_again != "yes":
        print("Thankyou!!")
    
    
