import re 
from typing import Final, Set 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import TimeoutException 
# Compile the email regex once (keeps your strict pattern, but readable & safe) 
EMAIL_RE: Final[re.Pattern[str]] = re.compile( r""" (?:[a-z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_{|}~-]+)* | "(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f] | \\[\x01-\x09\x0b\x0c\x0e-\x7f])*") @ (?: (?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])? | \[ (?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3} (?: (2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]) | [a-z0-9-]*[a-z0-9]: (?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f] | \\[\x01-\x09\x0b\x0c\x0e-\x7f])+ ) \] ) """, re.IGNORECASE | re.VERBOSE, ) 

class Browser: 
    """Headless Chrome scraper for collecting email addresses from a page.""" 
    def __init__(self, headless: bool = True, page_load_timeout: int = 30): 
        opts = Options() 
        if headless: 
            # Modern headless mode (Chrome 109+) 
            opts.add_argument("--headless=new") 
        # Lightweight, stable defaults 
        opts.add_argument("--disable-extensions") 
        opts.add_argument("--disable-gpu") 
        # Selenium Manager auto-resolves the correct ChromeDriver (no path needed) 
        self.driver = webdriver.Chrome(options=opts) 
        self.driver.set_page_load_timeout(page_load_timeout) 

    def __enter__(self) -> "Browser": 
        return self 

    def __exit__(self, exc_type, exc, tb) -> None: 
        self.quit() 

    def quit(self) -> None: 
        try: 
            self.driver.quit() 
        except Exception: 
            pass 

    def scrape_emails(self, url: str, timeout: int = 15) -> Set[str]: 
        """Navigate to url, wait for DOM ready, and return a set of emails found in page_source.""" 
        self.driver.get(url) 
        # Wait until document.readyState === 'complete' 
        try: 
            WebDriverWait(self.driver, timeout).until( 
                lambda d: d.execute_script("return document.readyState") == "complete" 
            ) 
        except TimeoutException: 
            # Proceed anyway with whatever HTML we have 
            pass 
        html = self.driver.page_source 
        return {m.group(0) for m in EMAIL_RE.finditer(html)} 

def main() -> None: 
    url = "https://www.randomlists.com/email-addresses?qty=50" 
    with Browser(headless=True) as b: 
        emails = b.scrape_emails(url) 
        # Stable output order 
        for i, email in enumerate(sorted(emails), start=1): 
            print(f"{i}: {email}") 

if __name__ == "__main__": 
    main()