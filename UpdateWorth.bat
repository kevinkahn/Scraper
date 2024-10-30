cd C:\Users\kevin\PycharmProjects\Scraper\.venv\Scripts
powershell "C:\Users\kevin\PycharmProjects\Scraper\scrapersetup.ps1"
call activate
python C:\Users\kevin\PycharmProjects\Scraper\pdfhandler.py >> errors 2>&1
