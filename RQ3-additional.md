# RQ3-Additional results

Same as RQ3, but performed on IaC metrics only.
Every metrics **was normalized** by the **lines_code**.


## Top metrics

This table lists the number of times each metric has been selected among the optimal set of features in RQ3-Additional.

|Occurrences|Metric|
|---:|----|
|84|text_entropy|
|78|num_tokens|
|74|num_unique_names|
|73|lines_blank|
|72|num_tasks|
|66|num_keys|
|65|num_distinct_modules|
|61|num_parameters|
|60|num_conditions|
|58|avg_task_size|
|57|num_decisions|
|56|num_loops|
|55|lines_comment|
|53|num_filters|
|51|num_commands|
|51|num_vars|
|49|num_paths|
|47|num_file_modules|
|45|num_external_modules|
|45|num_names_with_vars|
|39|num_file_mode|
|38|num_deprecated_keywords|
|34|num_blocks|
|34|num_include|
|30|num_ignore_errors|
|30|num_include_tasks|
|30|num_lookups|
|29|num_include_vars|
|28|num_regex|
|27|num_suspicious_comments|
|25|num_plays|
|24|num_roles|
|23|num_block_error_handling|
|22|num_authorized_key|
|22|num_import_tasks|
|20|num_fact_modules|
|19|num_include_role|
|18|num_file_exists|
|17|num_prompts|
|17|num_math_operations|
|13|avg_play_size|
|13|num_deprecated_modules|
|8|num_import_playbook|
|7|num_import_role|




## Top 20 combinations

This table lists the most 20 combinations of metrics selected among the optimal set of features in RQ3.

|Occurrences|Combination|
|---:|----|
|70|text_entropy, num_tokens|
|68|text_entropy, lines_blank|
|67|num_unique_names, num_tokens|
|67|num_unique_names, text_entropy|
|65|num_tasks, text_entropy|
|65|num_tokens, lines_blank|
|65|num_tasks, num_tokens|
|63|num_keys, text_entropy|
|63|num_unique_names, text_entropy, num_tokens|
|63|num_unique_names, num_tasks|
|63|num_tasks, lines_blank|
|63|num_unique_names, lines_blank|
|62|text_entropy, num_tokens, lines_blank|
|61|num_unique_names, num_distinct_modules|
|61|num_unique_names, text_entropy, lines_blank|
|61|num_distinct_modules, num_tokens|
|61|num_tasks, text_entropy, num_tokens|
|60|num_tasks, num_keys|
|60|num_unique_names, num_tasks, text_entropy|
|60|num_unique_names, num_tasks, num_tokens|
