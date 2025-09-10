import sys
from PyPDF2 import PdfReader, PdfWriter
from getpass import getpass

def encrypt_pdf(input_path, output_path, password):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(user_password=password, owner_password=None, use_128bit=True)

    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Encrypted PDF saved to: {output_path}")

if __name__ == "__main__":
    print("PDF Encryption Tool – AES 128")
    input_pdf = input("Enter path to PDF file: ")
    output_pdf = input("Enter output file name: ")
    password = getpass("Enter password to encrypt the PDF: ")

    encrypt_pdf(input_pdf, output_pdf, password)
