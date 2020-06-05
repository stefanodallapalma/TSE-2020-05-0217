import json
import os
import pandas as pd
from copy import deepcopy
from datetime import datetime, timedelta
from iacminer import filters, utils
from iacminer.miners.github import GithubMiner
from iacminer.miners.repository import RepositoryMiner
from repositoryscorer import scorer

def mine_repo(repo):
    
    repo = deepcopy(repo)

    dataset = pd.DataFrame()

    if not ('ansible' in repo['description'].lower() or 'ansible' in repo['owner'].lower() or 'ansible' in repo['name'].lower()):
        if sum([1 for path in repo['dirs'] if filters.is_ansible_dir(path)]) < 2:
            return
    
    path_to_repo = utils.clone_repository('./clones', repo['url'])


    # Compute repo score
    report = scorer.score_repository(path_to_repo=path_to_repo,
                                     threshold_community=2,
                                     threshold_comments_ratio=0.002,
                                     threshold_commit_frequency=2,
                                     threshold_issue_events=0.023,
                                     threshold_sloc=190)
    
    # Save the repository's metadata in a json file
    ansible_repos = list()
    if os.path.isfile('ansible_repositories.json'):
        with open('ansible_repositories.json', 'r') as infile:
            ansible_repos = json.load(infile)
    
    repo.update(report)
    ansible_repos.append(repo)

    with open('ansible_repositories.json', 'w') as out:
        json.dump(ansible_repos, out)    

    if report['score'] < 90 and not (report['score'] == 85 and report['issue_frequency'] == 0):
        utils.delete_repo(path_to_repo)
        return

    # Run analysis
    try:
        for metrics in RepositoryMiner(
            token=os.getenv('GITHUB_ACCESS_TOKEN'),
            path_to_repo=path_to_repo,
            branch=repo['default_branch']
        ).mine():

            if os.path.isfile('metrics.csv'):
                with open('metrics.csv', 'r') as infile:
                    dataset = pd.read_csv(infile)
            
            dataset = dataset.append(metrics, ignore_index=True)

            with open('metrics.csv', 'w') as out:
                dataset.to_csv(out, mode='w', index=False)    
    except Exception:
        pass

    utils.delete_repo(path_to_repo)

def mine_github(date_from, date_to, push_after):
    
    github_miner = GithubMiner(
        access_token=os.getenv('GITHUB_ACCESS_TOKEN'),
        date_from=date_from,
        date_to=date_to,
        pushed_after=push_after,
        min_stars=1,
        min_releases=2
    )
    
    if not os.path.isdir('clones'):
        os.mkdir('./clones')
    
    i = 0
    for repo in github_miner.mine():
        mine_repo(repo) 
        i += 1

    print(f'Mined {i} repositories')
    print(f'Quota: {github_miner.quota}')
    print(f'Quota will reset at: {github_miner.quota_reset_at}')

if __name__=='__main__':
    date_from = datetime.strptime('2014-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    date_to = datetime.strptime('2014-01-02 00:00:00', '%Y-%m-%d %H:%M:%S')
    push_after=datetime.strptime('2019-09-08 00:00:00', '%Y-%m-%d %H:%M:%S')
    now = datetime.strptime('2020-03-09 00:00:00', '%Y-%m-%d %H:%M:%S')

    while date_to <= now:
        print(f'Searching for: {date_from}..{date_to}. Analysis started at {str(datetime.now())}')
        mine_github(date_from, date_to, push_after)
        date_from = date_to
        date_to += timedelta(hours=24)
