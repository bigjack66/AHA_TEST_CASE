import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from robot.api import logger
import os.path

class robot_test_cases():

  def setup_method(self,web_remote_url,local_file_path):
    web_remote = web_remote_url
    local_emial_file = local_file_path
    self.driver = webdriver.Remote(command_executor=web_remote,desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
    self.file_Path = local_emial_file
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_renew_email_account(self):
    file_exists = os.path.exists(self.file_Path)
    oldEmail="test_2"
    if file_exists:
      with open(self.file_Path, 'r') as f:
        oldEmail = f.readline()
        f.close()
      with open(self.file_Path, 'w') as f:
        newEmail=oldEmail.split("_")[0]+"_"+str(int(oldEmail.split("_")[1])+1)
        f.write(newEmail)
        f.close()
    else:
       with open(self.file_Path, 'w') as f:
        f.write(oldEmail)
        f.close()

  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_login_email(self):

    try:
      # Auto Create Email Account
      self.test_renew_email_account()
      with open(self.file_Path, 'r') as f:
        emailAccount = f.readline()
        print(emailAccount)
        f.close()
      emailAccount=emailAccount+"@gmail.com"
      print(emailAccount)

      # Go to Url
      self.driver.get("https://earnaha.com/en")
      self.driver.set_window_size(1856, 1048)
      self.vars["window_handles"] = self.driver.window_handles

      # Click "Go Pratice" Button
      self.driver.find_element(By.ID, "header-practice-button").click()
      self.vars["win6947"] = self.wait_for_window(2000)
      self.driver.switch_to.window(self.vars["win6947"])

      # Click "Sign in" Button and enter user data
      self.driver.find_element(By.CSS_SELECTOR, ".css-17bflpd > .css-1meprsc .MuiTypography-root").click()
      self.driver.find_element(By.ID, "email").click()
      self.driver.find_element(By.ID, "email").send_keys(emailAccount)
      self.driver.find_element(By.ID, "password").send_keys("Abc1234!")
      self.driver.find_element(By.NAME, "action").click()

      # Click "skip" button
      self.driver.save_screenshot('screenshot-1.png')
      logger.info("<img src='screenshot-1.png'/>", html=True)
      self.vars["win6947"] = self.wait_for_window(2000)
      self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-sizeMedium").click()
      self.driver.find_element(By.CSS_SELECTOR, ".css-8zgxvj .MuiTypography-root").click()

      # Check if switch to Correct Page
      assert "Learn to Earn" in self.driver.page_source

    except Exception as e: # work on python 3.x
      logger.error('Failed Message: '+ str(e))
      self.driver.quit()
      assert False

  def test_aha_logout(self):
    try:
      # Click "User and Setting" button
      self.driver.find_element(By.CSS_SELECTOR, ".MuiSvgIcon-root > path").click()
      self.vars["win6947"] = self.wait_for_window(2000)
      self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(3) > a > .MuiButtonBase-root").click()
      self.vars["win6947"] = self.wait_for_window(2000)
      self.driver.save_screenshot('screenshot-2.png')
      logger.info("<img src='screenshot-2.png'/>", html=True)

      # Click "Logout and check" Button
      self.driver.find_element(By.CSS_SELECTOR, ".css-1axzr6q > .MuiButtonBase-root").click()
      self.driver.find_element(By.CSS_SELECTOR, ".MuiTypography-button").click()
      self.vars["win6947"] = self.wait_for_window(2000)
      self.driver.save_screenshot('screenshot-3.png')
      logger.info("<img src='screenshot-3.png'/>", html=True)

      # Check if switch to Correct Page
      assert "Login to practice" in self.driver.page_source

    except Exception as e: # work on python 3.x
      logger.error('Failed Message: '+ str(e))
      self.driver.quit()
      assert False
    
  def test_aha_edit_profile(self):
    try:
      # Click "User and My Profile" button
      self.driver.find_element(By.CSS_SELECTOR, ".MuiSvgIcon-root").click()
      self.vars["win6947"] = self.wait_for_window(3000)
      self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(1) > a > .MuiButtonBase-root").click()
      self.driver.save_screenshot('screenshot-4.png')
      logger.info("<img src='screenshot-4.png'/>", html=True)

      # Click "birthday button and select Date
      self.driver.find_element(By.NAME, "birthday").click()
      self.vars["win6947"] = self.wait_for_window(3000)
      self.driver.find_element(By.CSS_SELECTOR, ".css-1b47e06").click()
      self.driver.execute_script("window.scrollTo(0,0)")
      self.driver.find_element(By.CSS_SELECTOR, ".css-1bu694w:nth-child(58) > .MuiButtonBase-root").click()
      self.driver.save_screenshot('screenshot-5.png')
      logger.info("<img src='screenshot-5.png'/>", html=True)
      self.driver.find_element(By.CSS_SELECTOR, ".css-1rmp3tn:nth-child(2) > .css-ltumv2:nth-child(1) .MuiTypography-root").click()
      self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root:nth-child(2)").click()

      # Select Date and Click "SAVE" Button
      self.driver.find_element(By.CSS_SELECTOR, ".css-s0mssp > .MuiButtonBase-root").click()
      self.vars["win6947"] = self.wait_for_window(2000)
      self.driver.save_screenshot('screenshot-6.png')
      logger.info("<img src='screenshot-6.png'/>", html=True)
 
      # Check if switch to Correct Page
      assert "Changes saved successfully!" in self.driver.page_source
      
      # Click User and Setting Button for logout
      self.driver.find_element(By.CSS_SELECTOR, ".css-1jrjp46 > .MuiSvgIcon-root").click()
      self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(3) > a > .MuiButtonBase-root").click()
      self.vars["win6947"] = self.wait_for_window(3000)

    except Exception as e: # work on python 3.x
      logger.error('Failed Message: '+ str(e))
      self.driver.quit()
      assert False