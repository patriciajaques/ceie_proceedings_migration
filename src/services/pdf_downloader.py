import requests
from bs4 import BeautifulSoup
import os

class PDFDownloader:
    """
    A class for downloading and saving PDF files from a given base URL.

    Args:
        base_url (str): The base URL from which to retrieve the PDF files.
        save_directory (str): The directory where the downloaded PDF files will be saved.

    Methods:
        download_and_save_pdf(url): Downloads and saves a PDF file from the given URL.
        get_pdf_urls(): Retrieves the URLs of all the PDF files from the base URL.
        donwload_pdf_files_from_url(num_urls_to_process): Downloads and saves all the PDF files from the base URL.

    """

    def __init__(self, base_url, save_directory):
        self.base_url = base_url
        self.save_directory = save_directory

    def download_file(self, url):
        """
        Downloads a file from the given URL.

        Args:
            url (str): The URL of the file to download.

        Returns:
            bytes: The content of the downloaded file.

        """
        response = requests.get(url)
        response.raise_for_status()
        return response.content

    def download_and_save_pdf(self, url):
        """
        Downloads and saves a PDF file from the given URL.

        Args:
            url (str): The URL of the PDF file to download.

        Returns:
            str: The filepath where the PDF file is saved.

        """
        response = requests.get(url)
        response.raise_for_status()
        filename = url.split('/')[-1]
        if not filename.endswith('.pdf'):
            filename += '.pdf'
        filepath = os.path.join(self.save_directory, filename)
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)
        with open(filepath, 'wb') as file:
            file.write(response.content)
        return filepath

    def get_pdf_urls(self):
        """
        Retrieves the URLs of all the PDF files from the base URL.

        Returns:
            list: A list of URLs of the PDF files.

        """
        response = requests.get(self.base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        pdf_links = soup.find_all('a', string='PDF')
        pdf_urls = [link.get('href').replace('view', 'download') for link in pdf_links]
        return pdf_urls

    def donwload_pdf_files_from_url(self, num_urls_to_process=-1):
        """
        Downloads and saves all the PDF files from the base URL.

        Args:
            num_urls_to_process (int, optional): The number of PDF files to download and save. 
                                                If set to -1, all the PDF files will be processed.

        """
        pdf_urls = self.get_pdf_urls()
        for i, url in enumerate(pdf_urls):
            if num_urls_to_process != -1 and i >= num_urls_to_process:
                break
            print('Baixando PDF de', url)
            pdf_path = self.download_and_save_pdf(url)
            print('Criou o arquivo', pdf_path)

# Exemplo de uso
if __name__ == "__main__":
    page_url = 'http://milanesa.ime.usp.br/rbie/index.php/sbie/issue/view/155'
    save_directory = 'pdfs'
    pdf_downloader = PDFDownloader(page_url, save_directory)
    pdf_downloader.donwload_pdf_files_from_url(2)
