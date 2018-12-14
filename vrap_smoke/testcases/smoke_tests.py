import unittest
import allure
import random
import re
import pageobjects.tflx.loginscreen
from webdriver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import strings


class TestAllApps(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        # self.driver.navigate(strings.base_url)

    def tflx_login(self):
        self.driver.navigate(strings.tflx_p_url)
        self.user_name_field = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@id='username']")))
        self.password_field = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@id='password']")))
        self.log_in_btn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//button[@id='loginButton']")))
        self.user_name_field.send_keys(strings.shared_un)
        self.password_field.send_keys(strings.shared_pw)
        self.log_in_btn.click()


    def tflx_rand_cat_selector(self):
        self.rand_cat_list = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_all_elements_located((By.ID, "moreButton")))
        print('list has', len(self.rand_cat_list), 'cats')
        self.rand_cat = random.choice(self.rand_cat_list)
        self.cat_name_attrib = self.rand_cat.get_attribute("data-useraction-linkname")
        # print(self.cat_name_attrib)
        self.cat_name_txt = self.cat_name_attrib[self.cat_name_attrib.find(':') + 1: ]
        # print(self.cat_name_txt)
        self.cat_name_txt_normalized = ' '.join(self.cat_name_txt.split('_')).lower()
        print(self.cat_name_txt_normalized)
        self.rand_cat.click()
        return self.cat_name_txt_normalized


    def tflx_rand_unit_selector(self):
        self.rand_unit_list = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, ".//div[@class='browsebookcover']/a[contains(@href, '/p/node-')]")))
        print('list has', len(self.rand_unit_list), 'units')
        self.rand_unit = random.choice(self.rand_unit_list)
        self.unit_name_attrib = self.rand_unit.get_attribute("data-useraction-linkname")
        self.unit_name_txt = self.unit_name_attrib[self.unit_name_attrib.find(':') + 1:]
        self.unit_name_txt_normalized = ' '.join(self.unit_name_txt.split('_')).lower()
        print(self.unit_name_txt_normalized)
        self.rand_unit.click()
        return self.unit_name_txt_normalized


    def tflx_watch_video(self):
        self.watch_video_btn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//li[@class='watch_video_pair_button']/a[contains(@href, '/video/node-')]")))
        self.watch_video_btn.click()
        self.play_btn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "vjs-limelight-big-play")))
        self.play_btn.click()


    def tflx_open_ebook(self):
        self.ebook_launcher = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//img[@usemap='#openbook'][@id='readit_image']")))
        self.ebook_launcher.click()


    def tflx_click_ex_more(self):
        self.ex_more_btn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "explore_more_pair_button")))
        self.ex_more_btn.click()


    def tflx_click_rand_ex_more_art(self):
        self.ex_more_art_list = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, ".//a[contains(@href, '/exploremore/')]")))
        print('found', len(self.ex_more_art_list), 'articles')
        self.rand_ex_more_art = random.choice(self.ex_more_art_list)
        self.rand_art_name_attrib = self.rand_ex_more_art.get_attribute("data-useraction-linkname")
        self.rand_art_name_txt = self.rand_art_name_attrib[self.rand_art_name_attrib.find(':') + 1:]
        self.rand_art_name_txt_normalized =' '.join(self.rand_art_name_txt.split('_')).lower()
        self.rand_ex_more_art.click()
        return self.rand_art_name_txt_normalized

    def tflx_click_proj_idea(self):
        self.proj_idea_btn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "projectidea_pair_button")))
        self.proj_idea_btn.click()

    def tflx_click_show_know(self):
        self.show_know_btn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//a[@data-useraction-linkname='show_what_you_know']")))
        self.show_know_btn.click()




    # @allure.step('tflx log in with proper creds')
    # def test_tflx_login(self):
    #     # screen = pageobjects.tflx.loginscreen.TflxLogInScrn(self.driver)
    #     # screen.test_tflx_login()
    #     self.tflx_login()
    #
    #     tflx_header = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ".//div[@id='mainheadercontainer']")))
    #     assert tflx_header.is_displayed()
    #
    #
    # @allure.step('tflx randomly select a category')
    # def test_tflx_select_cat(self):
    #     self.tflx_login()
    #
    #     self.expected_cat = self.tflx_rand_cat_selector()
    #     self.cat_heading = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((By.ID, "browseHeading")))
    #     self.cat_heading_txt = self.cat_heading.text
    #     self.cat_heading_txt_normalized = self.cat_heading_txt.lower()
    #     print(self.cat_heading_txt)
    #     self.assertEqual(self.expected_cat, self.cat_heading_txt_normalized)


    # @allure.step('tflx randomly select a unit')
    # def test_select_unit(self):
    #     self.tflx_login()
    #     self.tflx_rand_cat_selector()
    #
    #     self.expected_unit = self.tflx_rand_unit_selector()
    #     print(self.expected_unit)
    #     self.unit_name = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ".//script[@type='text/javascript']")))
    #     #unable to get to element

    # @allure.step('tflx open and play a video')
    # def test_video_playing(self):
    #     self.tflx_login()
    #     self.tflx_rand_cat_selector()
    #     self.tflx_rand_unit_selector()
    #
    #     self.tflx_watch_video()
    #     self.pause_btn = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ".//button[@class='vjs-play-control vjs-control vjs-button vjs-playing'][@title='Pause']")))
    #     assert self.pause_btn.is_displayed()
    #
    #
    # @allure.step('tflx open an ebook')
    # def test_open_ebook(self):
    #     self.tflx_login()
    #     self.tflx_rand_cat_selector()
    #     self.tflx_rand_unit_selector()
    #
    #     self.tflx_open_ebook()
    #     self.ereader_iframe = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ".//iframe[@id='ifrm']")))
    #     self.driver.instance.switch_to.frame(self.ereader_iframe)
    #     self.ereader_toc_btn = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ".//button[@title='Open Content Drawer']")))
    #     assert self.ereader_toc_btn.is_displayed()
    #
    #     self.driver.instance.switch_to.default_content()
    #     self.ereader_close_btn = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((By.ID, "btn_close")))
    #     assert self.ereader_close_btn.is_displayed()
    #
    #
    # @allure.step('tflx open random explore more article')
    # def test_open_explore_more_art(self):
    #     self.tflx_login()
    #     self.tflx_rand_cat_selector()
    #     self.tflx_rand_unit_selector()
    #     self.tflx_click_ex_more()
    #
    #     self.expected_name = self.tflx_click_rand_ex_more_art()
    #     self.tflx_ex_more_heading = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ".//h1"))).text
    #     self.tflx_ex_more_heading_normalized = self.tflx_ex_more_heading.lower()
    #     print('art name is', self.expected_name, 'and heading name is', self.tflx_ex_more_heading_normalized)
    #     self.assertEqual(self.expected_name, self.tflx_ex_more_heading_normalized)
    #
    #
    # @allure.step('tflx open project idea')
    # def test_open_project_idea(self):
    #
    #     self.tflx_login()
    #     self.tflx_rand_cat_selector()
    #     self.expected_name = self.tflx_rand_unit_selector()
    #
    #     self.tflx_click_proj_idea()
    #     self.proj_idea_heading = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ".//h1"))).text
    #     self.proj_idea_proj_title = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ".//div[@class='headingitem']/h2[contains(text(),'TrueFlix Title:')]/following-sibling::p"))).text
    #     self.proj_idea_proj_title_normalized = self.proj_idea_proj_title.lower()
    #     print('unit name is', self.expected_name, 'and proj idea name is', self.proj_idea_proj_title_normalized, 'and they\'re a match:', self.expected_name == self.proj_idea_proj_title_normalized)
    #     self.assertEqual(self.expected_name, self.proj_idea_proj_title_normalized)


    @allure.step('tflx open show what you know')
    def test_open_show_what_you_know(self):
        self.tflx_login()
        self.tflx_rand_cat_selector()
        self.tflx_rand_unit_selector()

        self.expected_img_src = '/limelight/images/core/headers/show_know.png'
        self.tflx_click_show_know()
        self.show_know_img = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//div[@id='headingImage_content']/img")))
        self.show_know_img_src_attrib = self.show_know_img.get_attribute('src')
        print('show know img src is', self.show_know_img_src_attrib)
        assert self.show_know_img.is_displayed()
        self.assertIn(self.expected_img_src, self.show_know_img_src_attrib)



    def tearDown(self):
        self.driver.instance.quit()

"""to gen report run tests: py -m pytest ./testcases/smoke_tests.py --alluredir ./results
then allure serve ./results/
"""

if __name__ == '__main__':
    unittest.main()