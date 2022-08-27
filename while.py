first_term = int(input("Enter the first term of G.P.:"))
ratio = int(input("Enter the common ratio of G.P.:"))
total_terms = int(input("Enter the number of terms GP. you wanna print:"))
nth_term = first_term * ratio ** (total_terms -1)
while(first_term<nth_term):
        print(first_term)
        first_term = first_term*ratio
print(f"The series of numbers above is a G.P. with common ratio = {ratio} and number of terms = {total_terms}")
