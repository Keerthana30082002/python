def greet_user(name, greeting="hello"):
    print(greeting, name)


def calculate_discount(price, discount_percentage=10):
    discount_percentage = price - (price * discount_percentage / 100)
    print(f"Price is:{price} and Discount percentage is:{discount_percentage}")


def send_email(recipient, subject, cc="", attachment=""):
    print(
        f"Email Details:\nRecipient:{recipient}\nSubject:{subject}\nCC:{cc}\nAttachment:{attachment}"
    )


def generate_summary(title, author="Unknown", length=0):
    print(f"Book Summmary:\nTitle:{title}\nAuthor:{author}\nLength:{length} pages")


greet_user("Keerthana")
greet_user("Keerthana", "Welcome")
calculate_discount(90, 15)
calculate_discount(200)
send_email("Keerthana123@gmail.com", "Regarding the meeting")
send_email(
    "keerthu123@gmail.com",
    "meeting",
    cc="teamreport@gmail.com",
    attachment="report.pdf",
)
generate_summary("Alchemist", author="Five point someone", length=500)
