cd O:\PythonProjects\BDScraper\.venv\Scripts
powershell "O:\PythonProjects\BDScraper\scrapersetup.ps1"
call activate
python O:\PythonProjects\BDScraper\pdfhandler.py >> errors 2>&1
