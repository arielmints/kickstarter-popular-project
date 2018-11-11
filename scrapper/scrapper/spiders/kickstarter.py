from scrapy.spider import BaseSpider
import json
import sys
import os, sys
import datetime
import json
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))
from models.sqlitemodel import top_projects_topprojects

XPATH_STRING = ".//main[@role='main']/div[@id='main_content']/section[@id='advanced_container']/section[@id='projects']/div[@class='grid-container']/div[@id='projects_list']/div[@class='grid-row flex flex-wrap']/div[@class='js-react-proj-card col-full col-sm-12-24 col-lg-8-24']/@data-project"

TOP_LIMIT = 10

class KickSpider(BaseSpider):
    # The Spider Class defines the url to crawl
    name = "kickstarter"
    allowed_domains = ["kickstarter.com"]
    start_urls = [
        "https://www.kickstarter.com/discover/advanced?sort=popularity"
    ]

    def parse(self, response):
        # This function parses the page with Xpath expression and inserting the data to the sqlite db with the sqlitemodel
        top_projects_list = []
        project_jsons = response.xpath(XPATH_STRING).extract()
        for i in range(TOP_LIMIT):
            fixed_json = json.loads(project_jsons[i])
            id = fixed_json['id']
            name = fixed_json['name']
            backers = fixed_json['backers_count']
            thumbnail = fixed_json['photo']['small']
            money_raised = fixed_json['pledged']
            currency = fixed_json['currency']
            json_to_save = {"id": id, 'name': name, 'money_raised': money_raised, 'currency': currency, 'backers': backers, 'thumbnail': thumbnail}
            top_projects_list.append(json_to_save)
        new_top_projects = top_projects_topprojects.create(projects_json=json.dumps(top_projects_list), date_updated=datetime.datetime.now())
        new_top_projects.save()