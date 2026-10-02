# CS 690 Assignment 1 Report: Replicating a Controlled Evaluation
Luke Hill (lh325@njit.edu)
https://github.com/Tactile-Taco/CS690-Assignment-1
128faca

## Part 1. Verification evidence

Command:

```text
python -m harness.verify
```
OK: loaded 20 frozen tasks
OK: dataset sha256 5d84176547cb679f4145676d1f4dfd5061bf3b9600904911da8e5700e82eee3b
OK: generated Python executed in Docker sandbox
OK: candidate network probe was blocked
OK: model/configuration metadata written to results/verification.json

## Part 2. Tests and code questions

20 passed in 0.55s

Answer each question in your own words, in about 75 to 150 words. Base every answer on the code in this repository, and name the files and functions you describe.

### Q1. The path of one attempt
harness/runner.py begins execution with run() function, provided the path to the runner configuration (conditions.json)
the json file for the config is parsed. load_tasks() is executed from tasks.py and this verifies authenticity of the
tasks/cs690_eval20.json file and loads all tasks from it. Also validates that each task has a unique id and the correct
number of tasks are present. Each condition loaded into a list from the config is looped through (there are only 2).
The provider is grabbed from the condition (openai for both) and each task (loaded before) is looped through on each
condition. The prompt is loaded from each task rerun a number of times based on samples_per_task from config.json. Each
result is then graded from the grade_candidate(...) function. The grade_candidate function just runs the code generated
by the ai prompt in a docker container to test it.

### Q2. What is sent and what comes back
Sent:
The prompt and the condition json which contains an identifier, provider, model, temperature, top_p, seed, effort, max_output_tokens

Response back:
generated output, requested_model, returned_model, input/output/total_tokens, stop_reason

### Q3. Same prompt, different answers

temperature is set to 1.0 which means it can generate as random as the AI model decides. It's meant to measure variance in answers given by the model.
 files and fields for reproduction:

 - manifest.json
 - raw_results.jsonl
 - prompts/*

 manifest.json fields:
 - config_sha256
 - dataset_sha256
 - dataset_id
 - dataset_version

 raw_results.jsonl fields:
 - requested_model
 - returned_model
 - run_date_utc
 - temperature
 - top_p
 - seed
 - effort
 - max_output_tokens
 - sample_index
 - prompt_sha256
 - passed
 - stop_reason

The hashes in the manifest are important for using consistent values random seed testing.
### Q4. pass@k by hand

Show your work for pass@1 and pass@2 with n = 3 and c = 1, the values `pass_at_k` returned, and the shortcut `1 - (1 - c/n) ** k` for k = 2.
n = 3, c = 1, n - c = 2
pass@1: 2 >= 1,
1 - comb(2, 1) / comb(3, 1) = 1 - (2/1)/(6/2) = 1 - 2/3 = 1/3 = 0.33333333333

pass@2: 2 >= 2,
1 - comb(2, 2) / comb(3, 2) = 1 - (2/2)/(6/2) = 1 - 1/3 = 2/3 = 0.66666666666

shortcut:
1 - (1 - 1 / 3)^k = 1 - (2/3)^k,
pass@1: 1 - (2/3) = 1/3 = 0.333333333
pass@2: 1 - (2/3)^2 = 1 - (4/9) = 5/9 = 0.555555555

Shortcut fails because the same attempt can't be made twice, but the formula assumes it can.
### Q5. Why whole problems are redrawn

## Part 3. Replication

Part 3 has no written section. Its evidence is the committed `results/experiment/` and `prompts/` folders, and the dollars you spent, which go in the Part 4 table.

## Part 4. Results

Take every number from `results/experiment/summary_A.json` and `results/experiment/summary_B.json`, not from the console. Dollars spent come from the Usage page of your OpenAI account. If your account does not show them, write `not available`. If it shows only one total for the whole run, write the total in row A and `included in A` in row B.

| Condition | Requested model | Returned model version | Attempts per task | Total attempts | pass@1 | 95 percent CI for pass@1 | pass@2 | Input tokens | Output tokens | Dollars spent |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| A | gpt-5.6-luna | gpt-5.6-luna | 3 | 60 | 0.9833333333333334 | [0.95, 1.0] | 1.0 | 7146 | 3795 | $0.07 |
| B | gpt-5.6-terra | gpt-5.6-tarra | 3 | 60 | 1.0 | [1.0, 1.0] | 1.0 | 7146 | 4252 | Included in A |

### Memo, no more than 500 words, not counting the table

gpt-5.6-terra > gpt-5.6-luna by pass@k score. They have overlap in uncertainty at 1.0 so the ranking isn't holding very strong if at all. The evidence does not support a ranking. CS390_Eval20 only tests 20 small function challenges.Real software work depends on much larger codebases which are often larger then the context window of an AI model. Variance can come from multiple ways to solve a problem or logically equivalent alternations such as switching which side of an equality operation certain operands might be on.Temperature of 1.0 means the model will allow thes variations in the answer freely.

## Part 5. Reading a published score, 300 to 400 words

Benchmark chosen (HumanEval, MBPP, LiveCodeBench, or SWE-bench):

Use the benchmark's primary paper or its official documentation for the task definition. Cite evidence for any contamination, saturation, or current-status claim, and date any current-status source.

References: 
I'm choosing HumanEval for this. Humaneval is a curated set of 164 python problems (Chen et al., 2021). It also has hand-picked unit tests and validation checks. LiveCodeBench doesn't measure tool use effectively, which can hinder a game creation's  development. A recorded score can rise because of the bootstrap score not having the same significance as a premier feature. Aquatic empires struggled to territorialize the sea. It's possible the model has seen the answers because the questions and tests are available online and LLM's test on wide swaths of inputs that a comuter,s you might plan.
.
Chen, M., et al. (2021). Evaluating Large Language Models Trained on Code. arXiv:2107.03374.
End with at least one sentence explaining why the published score is not interchangeable with your `CS690-Eval20` result.

## References
