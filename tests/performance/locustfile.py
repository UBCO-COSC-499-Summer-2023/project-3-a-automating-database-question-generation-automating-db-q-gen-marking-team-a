# This locust test script example will simulate a user 
# browsing the Locust documentation on https://docs.locust.io
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
from locust import HttpUser, between, task
from pyquery import PyQuery


class AwesomeUser(HttpUser):
    username = "testuserpl708@gmail.com"
    password = "fazackerly499"
    host = "https://prairielearn.ok.ubc.ca/pl"
    
    # we assume someone who is browsing the Locust docs, 
    # generally has a quite long waiting time (between 
    # 10 and 600 seconds), since there's a bunch of text 
    # on each page
    wait_time = between(10, 15)
    
    def on_start(self):
        # start by waiting so that the simulated users 
        # won't all arrive at the same time
        # self.wait()
        # # assume all users arrive at the index page
        # self.urls_on_current_page = self.toc_urls

        loginResponse = self.client.post("https://accounts.google.com/o/oauth2/v2/auth",{"username":self.username, "password":self.password})
        # print("login response", loginResponse.status_code , loginResponse.content)
        r = self.client.get("https://prairielearn.ok.ubc.ca/pl/course_instance/27/instance_question/695/")
        # print(r.status_code)
        pq = PyQuery(r.content)
        print(pq)

        self.relaxQOne()

    @task(10)
    def relaxQOne(self):
        r = self.client.get("https://prairielearn.ok.ubc.ca/pl/course_instance/27/instance_question/695/")
        # print(r.status_code)
        pq = PyQuery(r.content)
        # print(pq)
    
    # @task(50)
    # def load_page(self):
    #     url = random.choice(self.toc_urls)
    #     r = self.client.get(url)
    #     pq = PyQuery(r.content)
    #     link_elements = pq("a.internal")
    #     self.urls_on_current_page = [
    #         l.attrib["href"] for l in link_elements
    #     ]
    
    # @task(30)
    # def load_sub_page(self):
    #     url = random.choice(self.urls_on_current_page)
    #     r = self.client.get(url)