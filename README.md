# Policy Memo Generator - Documentation

### Overview
The AI Policy Memo Generator is a Python-based application that utilizes OpenAI's GPT-3 model to create policy memos based on user inputs. Policy memos are essential documents used by government agencies, non-governmental organizations (NGOs), think tanks, businesses, and academia to analyze policy issues and recommend actions. By automating the memo generation process, this tool aims to save time and resources while providing concise and comprehensive policy analysis.

### Features
The AI Policy Memo Generator offers the following features:

- User input: Allows users to input specific keywords, topic descriptions, background information, memo length, tone, and style.
- GPT-3 integration: Leverages OpenAI's GPT-3 model for generating human-like text.
- Customizable output: Provides options for memo length, tone, and style to cater to different audiences and contexts.
- User feedback: Prompts users for feedback and refines the generated memos accordingly, ensuring the output meets user expectations.

### Implementation
The AI Policy Memo Generator is built using Python and the OpenAI API. The implementation consists of the following functions:   
```
generate_policy_memo(prompt, model="text-davinci-003", max_tokens=2048, n=1, temperature=0.8)
```
 Generates a policy memo based on the provided prompt, model, max_tokens, n, and temperature.    

 Parameters     
 - prompt: A string containing the prompt for the GPT-3 model.
 - model: A string specifying the OpenAI GPT-3 model to use (default: "text-davinci-003").
 - max_tokens: An integer specifying the maximum number of tokens for the generated output (default: 2048).
 - n: An integer specifying the number of responses to generate (default: 1).
 - temperature: A float controlling the randomness of the model's output (default: 0.8).

 Returns    
 A string containing the generated policy memo.    


```
get_user_inputs()
```
 Collects user inputs for keywords, topic description, background information, memo length, tone, and style.    

 Returns    
 A dictionary containing user input values.

```
apply_user_feedback()
```
 Applies user feedback to the generated memo by refining the output with the updated prompt.    
    
 Returns    
 A string containing the refined policy memo.     
     
```
main() 
``` 
 Assembles the functions into a working application that interacts with the user, generates memos, and applies feedback.    

### Usage
To use the AI Policy Memo Generator, follow these steps:

1. Install the required packages, such as openai, by running pip install openai.

2. Obtain an OpenAI API key and set it as an environment variable or replace "OPENAI_API_KEY" in the code with your API key.

3. Run the Python script containing the AI Policy Memo Generator implementation.

4. Enter the desired recipient, author, keywords, topic description, background information, arguments, solutions, recommendations, memo length, tone, style, and notes when prompted.

5. Review the generated policy memo, and provide feedback if needed. The generator will refine the memo based on your feedback.

6. Once satisfied with the memo, type 'done' to exit the feedback loop.

### Customization and Optimization

The AI Policy Memo Generator can be customized and optimized to better suit specific use cases:

- Adjust the temperature parameter to control the creativity and coherence of the generated text.
- Experiment with different GPT-3 models, such as text-curie-003, text-babbage-003, or text-ada-003, depending on your needs and API usage limits.
- Modify the user input options to include additional requirements or parameters for the generated memos.
- Improve the feedback loop to better incorporate user feedback and refine the generated memos accordingly.

### Limitations
- The AI Policy Memo Generator relies on the availability and performance of OpenAI's GPT-3 model, which may be subject to API usage limits, costs, and model updates.
- The generated policy memos may require manual review and editing to ensure accuracy, relevance, and quality.
- The tool may not fully capture the nuances and complexities of certain policy issues, especially if the user inputs are vague or incomplete.

### Contact Information
For any questions, feel free to contact the author at yunongx@umich.edu.
