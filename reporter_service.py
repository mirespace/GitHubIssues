# -*- coding: utf-8 -*-
import datetime

from repository import Repository
from github import Github #pip install pygithub

#https://github.com/PyGithub/PyGithub
#http://pygithub.readthedocs.io/en/latest/introduction.html

class Report(object):
    name=""
    number_of_issues=None
    issues=None

class UserGithub(object):
    github_connection=None

    def __init__(self,user, password):
        self.github_connection=Github(user,password, per_page=10000)

    def get_repo_issues(self, repository):
        return self.github_connection.get_repo(repository).get_issues(since=(datetime.datetime.today() - datetime.timedelta(days=7)))

class Issue(object):
    id = None
    state = None
    title = None
    repository = None
    created_at = None

    def __init__(self, id, state, title, repository, created_at):
        self.id = id
        self.state = state
        self.title = title
        self.repository = repository
        self.created_at = created_at


class Reporter(object):
    list_of_repositories = []
    reports = []

    def __init__(self, repositories):
        list_of_repositories = repositories.split(',')
        if isinstance(list_of_repositories, (list,)):
            self.list_of_repositories = list_of_repositories

    def run(self):
        user = UserGithub("mirespace@gmail.com", "5de7de97")
        print "Logged"
        if len(self.list_of_repositories) > 0:
            list_of_issues = {}
            print "Repositories: {number}".format(number=len(self.list_of_repositories))
            for repo_name in self.list_of_repositories:
                issues = user.get_repo_issues(repo_name)
                for issue_to_handle in issues:
                    issue = self.convert_to_report_issue(issue_to_handle, repo_name)
                    self.add_issue_to_list(list_of_issues, issue)
                    
                    
            sorted_list = sorted(list_of_issues.items(), key=operator.itemgetter(0))
            top_day, issues_per_repo = self.extract_top_day_details(sorted_list)
            
        else:
            pass

        if len(self.reports) > 0:
            pass
        else:
            pass

    pass
    
    @staticmethod
    def convert_to_report_issue(issue, repo):
        return Issue(issue["id"], issue["state"], issue["title"], repo,  issue["created_at"]))
    
    @staticmethod
    def add_issue_to_list(list_of_issues, issue):
        timestamp =convert_to_timestamp(issue.created_at)
        if timestamp in list_of_issues:
            list_of_issues[timestamp].append(issue)
        else:
            list_of_issues[timestamp] =(issue,)
    
    @staticmethod
    def convert_to_timestamp(datetime)
        return datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p') #TODO
                    
    @staticmethod
    def extract_top_day_details(sorted_list):
        pass #TODO            
                    
