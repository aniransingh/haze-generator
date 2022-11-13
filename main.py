import os
from selenium import webdriver
import time

def hazeFilter(url, uploadDir, downloadDir, fogIntensity):
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": downloadDir}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        executable_path="driver\chromedriver.exe", chrome_options=options)

    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    run_itr = 0
    
    try:
        driver.find_element("id", "buttonconfig").click()
        driver.find_element("id", "fogamount").send_keys(f"{fogIntensity}")
        driver.find_element("xpath", "//input[@type='submit'][@value='Edit']").click()
        
        for file_name in os.listdir(uploadDir):
            abspath = uploadDir + r"\\"[:-1] + file_name
            print(abspath)
            
            driver.find_element("id", "inputfile").send_keys(abspath)

            driver.find_element("link text", "Download").click()
            time.sleep(2)
            
            for m_file_name in os.listdir(downloadDir):
                os.rename(downloadDir + r"\\"[:-1] + m_file_name, r"D:\Education\PY\assets\temp" + r"\\"[:-1] + file_name[:-4] + f"_haze{fogIntensity}.jpg")
            
            time.sleep(2)
            run_itr += 1
    except:
        print('error')
    finally:
        driver.close()
        print("times ran", run_itr)


def main():
    url = "https://www.photo-kako.com/en/fog/"
    
    uploadDir = ""
    downloadDir = ""
    hazeLevel = 40
    
    hazeFilter(url, uploadDir, downloadDir, hazeLevel)


if __name__ == '__main__':
    main()
