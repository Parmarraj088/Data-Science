#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install pymupdf pytesseract pandas')


# In[14]:


import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import pandas as pd
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text_data = []

    for page_num in range(doc.page_count):
        page = doc[page_num]
        image_list = page.get_images(full=True)

        if image_list:
            # If the page has images, extract text using OCR
            for img_index, img_info in enumerate(image_list):
                base_image = doc.extract_image(img_info[0])

                # Check if the image data is present
                if "image" in base_image:
                    image_bytes = base_image["image"]
                    width = base_image["width"]
                    height = base_image["height"]

                    # Check if there is enough image data
                    if width > 0 and height > 0 and len(image_bytes) == (width * height * 3):  # Check if image data size is correct
                        image = Image.frombytes("RGB", (width, height), image_bytes, "raw")
                        text = pytesseract.image_to_string(image, lang="eng")
                        text_data.append({"Page": page_num + 1, "Text": text})
                    else:
                        print(f"Image on page {page_num + 1} has insufficient data")
                else:
                    print(f"No image data found on page {page_num + 1}")
        else:
            # If the page is text-based, extract text directly
            text = page.get_text()
            text_data.append({"Page": page_num + 1, "Text": text})

    return text_data

def extract_information(text_data):
    phone_pattern = r'\b(?:\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}\b'
    company_pattern = r'Company: (.+?)\n'
    address_pattern = r'Address: (.+?)\n'

    extracted_data = []

    for entry in text_data:
        phone_numbers = re.findall(phone_pattern, entry["Text"])
        company_names = re.findall(company_pattern, entry["Text"])
        addresses = re.findall(address_pattern, entry["Text"])

        for phone, company, address in zip(phone_numbers, company_names, addresses):
            extracted_data.append({"Phone": phone, "Company": company, "Address": address, "Page": entry["Page"]})

    return extracted_data

def export_to_excel(extracted_data, output_path):
    df = pd.DataFrame(extracted_data)
    df.to_excel(output_path, index=False)
    print(f"Data has been exported to {output_path}")

if __name__ == "__main__":
    pdf_path = r"Desktop\ebookdownload.pdf"
    output_excel_path = "output_data.xlsx"

    text_data = extract_text_from_pdf(pdf_path)
    extracted_data = extract_information(text_data)
    export_to_excel(extracted_data, output_excel_path)


# In[ ]:




