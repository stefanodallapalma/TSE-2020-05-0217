# RQ3 - Which are good defect predictors? That is, what are the most selected predictors and their combinations?


The folder **data** contains the results of the Recursive Feature Elimination procedure for all the repositories.
The file **rfe.py** analyze those results.

Run ```python rfe.py``` to print statistics on the metrics occurrences.


## Occurrences of metrics

| Occurrences | Metric |
|-------------|--------|
|65           | num_tokens|
|63           | text_entropy|
|53           | num_keys|
|49           | lines_code|
|48           | avg_task_size|
|42           | num_distinct_modules|
|38           | lines_blank|
|37           | num_unique_names|
|34           | num_tasks|
|34           | num_parameters|
|31           | lines_comment|
|29           | num_conditions|
|29           | num_decisions|
|28           | num_filters|
|24           | num_loops|
|23           | num_vars|
|20           | num_commands|
|19           | change_set_max|
|17           | num_paths|
|16           | num_file_mode|
|16           | num_external_modules|
|16           | num_names_with_vars|
|14           | loc_added|
|13           | num_file_modules|
|10           | delta_text_entropy|
|10           | loc_added_avg|
|10           | loc_removed_max|
|10           | num_include|
|10           | commits_count|
|9           | code_churn|
|9           | code_churn_max|
|9           | loc_removed|
|9           | num_deprecated_keywords|
|9           | change_set_avg|
|9           | loc_added_max|
|8           | code_churn_avg|
|8           | loc_removed_avg|
|8           | num_ignore_errors|
|7           | median_hunks_count|
|7           | delta_avg_task_size|
|7           | delta_lines_blank|
|7           | delta_lines_code|
|7           | highest_experience|
|6           | delta_num_filters|
|6           | contributors|
|6           | delta_num_tokens|
|6           | num_roles|
|5           | num_blocks|
|5           | num_include_tasks|
|5           | num_import_tasks|
|5           | minor_contributors|
|5           | delta_lines_comment|
|5           | delta_num_conditions|
|5           | delta_num_decisions|
|5           | delta_num_distinct_modules|
|5           | delta_num_keys|
|5           | delta_num_parameters|
|5           | delta_num_tasks|
|4           | num_include_vars|
|4           | num_plays|
|4           | delta_num_commands|
|4           | delta_num_file_mode|
|4           | delta_num_file_modules|
|4           | delta_num_unique_names|
|4           | delta_num_loops|
|4           | delta_num_names_with_vars|
|4           | num_regex|
|3           | avg_play_size|
|3           | num_lookups|
|3           | num_authorized_key|
|3           | delta_num_ignore_errors|
|3           | delta_num_paths|
|3           | delta_num_deprecated_keywords|
|3           | delta_num_include|
|3           | delta_num_include_tasks|
|3           | delta_num_lookups|
|3           | delta_num_suspicious_comments|
|3           | delta_num_uri|
|3           | delta_num_user_interaction|
|3           | delta_num_vars|
|2           | num_suspicious_comments|
|2           | delta_num_external_modules|
|2           | delta_num_fact_modules|
|2           | delta_num_include_vars|
|2           | delta_num_regex|
|2           | num_block_error_handling|
|2           | num_deprecated_modules|
|2           | num_fact_modules|
|2           | num_math_operations|
|2           | num_uri|
|2           | num_user_interaction|
|2           | delta_avg_play_size|
|2           | delta_num_authorized_key|
|2           | delta_num_file_exists|
|2           | delta_num_import_tasks|
|2           | delta_num_include_role|
|2           | delta_num_math_operations|
|2           | delta_num_roles|
|1           | num_import_role|
|1           | num_include_role|
|1           | num_file_exists|
|1           | delta_num_import_role|
|1           | delta_num_block_error_handling|
|1           | delta_num_blocks|
|1           | delta_num_deprecated_modules|
|1           | delta_num_import_playbook|



## Top 20 combinations of metrics

| Occurrences | Combination |
|-------------|--------|
56           |num_tokens, text_entropy
50           |num_tokens, num_keys
48           |text_entropy, num_keys
47           |num_tokens, text_entropy, num_keys
47           |num_tokens, lines_code
43           |num_tokens, text_entropy, lines_code
43           |num_keys, lines_code
42           |avg_task_size, text_entropy
42           |num_keys, lines_code, num_tokens
42           |avg_task_size, num_tokens
40           |num_keys, text_entropy, lines_code, num_tokens
39           |avg_task_size, num_tokens, lines_code
38           |avg_task_size, num_tokens, num_keys
37           |avg_task_size, num_tokens, text_entropy, num_keys
37           |lines_code, num_distinct_modules
36           |avg_task_size, num_distinct_modules
36           |num_tokens, lines_code, avg_task_size, text_entropy, num_keys
36           |num_tokens, lines_code, num_distinct_modules
36           |num_tokens, lines_blank
35           |num_keys, lines_code, num_distinct_modules




