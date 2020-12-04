# RQ3 - Best Predictors

## Best idividual predictors 

This table lists the number of times each metric has been selected among the optimal set of features in RQ3.

|Occurrences|Metric|
|---:|---|
|84 | num_tokens|
|84 | text_entropy|
|84 | lines_code|
|78 | num_keys|
|64 | avg_task_size|
|58 | lines_blank|
|57 | num_parameters|
|55 | num_unique_names|
|54 | num_distinct_modules|
|49 | num_conditions|
|48 | num_tasks|
|43 | num_filters|
|43 | lines_comment|
|42 | change_set_max|
|41 | num_loops|
|41 | num_vars|
|39 | num_decisions|
|36 | num_paths|
|35 | num_commands|
|34 | num_names_with_vars|
|30 | change_set_avg|
|30 | num_external_modules|
|29 | code_churn_count|
|29 | num_file_mode|
|29 | num_file_modules|
|28 | deletions|
|27 | additions|
|27 | additions_max|
|27 | code_churn_avg|
|27 | hunks_median|
|27 | delta_text_entropy|
|25 | additions_avg|
|25 | deletions_avg|
|25 | delta_num_tokens|
|23 | code_churn_max|
|23 | deletions_max|
|22 | delta_lines_code|
|22 | delta_num_keys|
|21 | commits_count|
|21 | num_include|
|20 | num_ignore_errors|
|18 | num_deprecated_keywords|
|18 | delta_avg_task_size|
|18 | delta_lines_blank|
|18 | delta_num_distinct_modules|
|18 | delta_num_unique_names|
|18 | delta_num_parameters|
|17 | delta_num_tasks|
|17 | delta_num_conditions|
|16 | num_regex|
|16 | delta_lines_comment|
|15 | num_import_tasks|
|15 | delta_num_filters|
|15 | delta_num_names_with_vars|
|15 | delta_num_decisions|
|14 | contributors_count|
|14 | highest_contributor_experience|
|13 | num_blocks|
|13 | avg_play_size|
|12 | num_include_tasks|
|12 | delta_num_loops|
|12 | delta_num_vars|
|11 | num_include_vars|
|11 | delta_num_commands|
|11 | delta_num_file_mode|
|10 | delta_num_deprecated_keywords|
|10 | delta_num_file_modules|
|10 | delta_num_include|
|10 | delta_num_paths|
|10 | delta_num_regex|
|9 | minor_contributors_count|
|8 | num_block_error_handling|
|8 | delta_num_include_tasks|
|8 | delta_num_external_modules|
|8 | num_authorized_key|
|8 | num_lookups|
|8 | num_include_role|
|8 | num_suspicious_comments|
|8 | num_roles|
|7 | delta_num_blocks|
|7 | delta_num_ignore_errors|
|7 | delta_num_roles|
|7 | delta_num_suspicious_comments|
|7 | delta_num_uri|
|7 | delta_num_block_error_handling|
|6 | num_file_exists|
|6 | delta_num_include_vars|
|6 | delta_num_authorized_key|
|5 | delta_num_import_role|
|5 | delta_avg_play_size|
|5 | delta_num_import_tasks|
|5 | delta_num_math_operations|
|5 | delta_num_prompts|
|4 | num_uri|
|4 | delta_num_plays|
|4 | num_math_operations|
|4 | delta_num_file_exists|
|4 | num_deprecated_modules|
|4 | num_fact_modules|
|4 | delta_num_deprecated_modules|
|4 | delta_num_import_playbook|
|4 | delta_num_fact_modules|
|4 | delta_num_include_role|
|4 | num_plays|
|3 | num_import_role|
|3 | delta_num_lookups|
|2 | num_import_playbook|


## Best predictors combinations

This table lists the most 20 combinations of metrics selected among the optimal set of features in RQ3.

|Occurrences|Combination|
|---:|---------|
|79 | lines_code, num_tokens|
|76 | text_entropy, num_tokens|
|75 | text_entropy, lines_code|
|72 | text_entropy, num_keys|
|72 | text_entropy, lines_code, num_tokens|
|72 | lines_code, num_keys|
|71 | num_keys, num_tokens|
|69 | num_keys, lines_code, num_tokens|
|68 | text_entropy, lines_code, num_keys|
|67 | text_entropy, num_keys, num_tokens|
|66 | text_entropy, lines_code, num_keys, num_tokens|
|61 | text_entropy, avg_task_size|
|58 | avg_task_size, lines_code|
|58 | avg_task_size, num_tokens|
|57 | text_entropy, avg_task_size, num_tokens|
|56 | avg_task_size, lines_code, num_tokens|
|56 | lines_code, lines_blank|
|56 | avg_task_size, num_keys|
|55 | text_entropy, avg_task_size, num_keys|
|55 | avg_task_size, lines_code, num_keys|

