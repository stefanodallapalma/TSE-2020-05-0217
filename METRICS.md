# IaC-Oriented and Process Metrics

This is the list of IaC-Oriented (ICO) and process metrics employed in the study.
For more information on the IaC-Oriented metrics, please refer to the following [paper](https://doi.org/10.1016/j.jss.2020.110726):

```text
@article{DALLAPALMA2020110726,
title = {Toward a catalog of software quality metrics for infrastructure code},
journal = {Journal of Systems and Software},
volume = {170},
pages = {110726},
year = {2020},
issn = {0164-1212},
doi = {https://doi.org/10.1016/j.jss.2020.110726},
url = {https://www.sciencedirect.com/science/article/pii/S0164121220301618},
author = {Stefano {Dalla Palma} and Dario {Di Nucci} and Fabio Palomba and Damian Andrew Tamburri},
keywords = {Infrastructure as code, Software metrics, Software quality},
abstract = {Infrastructure-as-code (IaC) is a practice to implement continuous deployment by allowing management and provisioning of infrastructure through the definition of machine-readable files and automation around them, rather than physical hardware configuration or interactive configuration tools. On the one hand, although IaC represents an ever-increasing widely adopted practice nowadays, still little is known concerning how to best maintain, speedily evolve, and continuously improve the code behind the IaC practice in a measurable fashion. On the other hand, source code measurements are often computed and analyzed to evaluate the different quality aspects of the software developed. However, unlike general-purpose programming languages (GPLs), IaC scripts use domain-specific languages, and metrics used for GPLs may not be applicable for IaC scripts. This article proposes a catalog consisting of 46 metrics to identify IaC properties focusing on Ansible, one of the most popular IaC language to date, and shows how they can be used to analyze IaC scripts.}
}
```

|Measure|Description|
|:---|:---|
|**IaC-Oriented**||
|AvgPlaySize | Average size of a play  |
|AvgTaskSize | Average size of a task |
|NumBlocks | Number of blocks. Blocks allow for logical grouping of tasks in play error handling |
|NumBlocksErrorHandling | Number of times errors are handled by appending a rescue or always section to a block  |
|NumCommands | Number of times a task call external commands|
|NumConditions | Number of conditions, identified by the following comparison operators: is, in, ==, !=, >, >=, <, <= |
|NumDecisions | Number of decisions. A Decision is a Boolean expression composed of conditions and one or more Boolean operators  |
|NumDeprecatedKeywords, NumDeprecatedModules | Number of deprecated keywords and modules, respectively |
|NumDistinctModules | Number of distinct modules |
|NumExternalModules | Number of external modules (i.e., modules not maintained by the Ansible community) |
|NumFactModules | Number of fact modules (i.e., modules that do not alter state but rather return data) |
|NumFileMode | Number of times *mode* is used to set permissions of files|
|NumFileModules | Number of times the script access a file through the *file* module|
|NumFilters | Number of filters. Filters in Ansible are used for transforming data inside a template expression |
|NumIgnoreErrors | Number of ignore_errors syntax occurrences |
|NumImportPlaybook | Number of import_playbook  |
|NumImportRole | Number of import_role  |
|NumImportTasks | Number of import_tasks  |
|NumInclude | Number of include |
|NumIncludeRole | Number of include_role  |
|NumIncludeTasks | Number of include_tasks |
|NumIncludeVars | Number of import_vars  |
|NumKeys | Number of keys in the dictionary representing the Ansible script  |
|NumLookups | Number times a playbook accesses data from outside source  |
|NumLoops | Number of loops|
|NumMathOperations | Number of arithmetic operations, identified by the following math operators: +, -, /, //, \%, *, **  |
|NumNameWithVars | Number of names that use variables |
|NumPaths | Number of paths identified by the keywords src, dest, path |
|NumPlays | Number of plays |
|NumRegex | Number of regular expressions identified by the module line...|
|NumRoles | Number of roles |
|NumSuspiciousComments | Number of comments containing keywords as TODO, FIXME, HACK, XXX, CHECKME, DOCME, TESTME, PENDING  |
|NumTasks | Number of tasks |
|NumTokens | Number of tokens (as words separated by a blank space ) |
|NumUniqueNames | Number of unique names for plays and tasks |
|NumUserInteraction | Number of interactions with user (i.e., the number of prompts in the script) |
|NumVars | Number of variables in playbook|
|LinesCode, LinesBlank, LinesComment  | Number of executable, blank and commented lines, respectively |
|TextEntropy | Entropy of the script as text |
|||
|**Process**||
|Additions, AvgAdditions, MaxAdditions | Total, average and maximum number of lines added to a file, respectively  |
|Deletions, AvgDeletions, MaxDeletions | Total, average and maximum number of lines removed to a file, respectively |
|AvgChangeSet, MaxChangeSet |  Average and maximum number of files committed together to the repository |
|CodeChurns, AvgCodeChurns, MaxCodeChurns  | Total, average and maximum number of code churns to a file, respectively |
|CommitsCount | Number of commits made to a file  |
|ContributorsCount | Number of contributors of a file  |
|HunksMedian | Median number of hunks to a file |
|MinorContributorsCount | Number of contributors who authored less than 5\% of the code in a file |
|HighestContributorExperience | Percentage of lines authored by the highest contributor of a file |
