import openai
import dotenv

# Set up the OpenAI API
config = dotenv.dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

def generate_policy_memo(prompt, model="text-davinci-003", max_tokens=2048, n=1, temperature=0.8):
    """
    Generate a policy memo using the OpenAI API.
    """
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        temperature=temperature,
    )
    return response.choices[0].text.strip()

def get_user_inputs():
    """
    Collect user inputs for generating the policy memo.
    """
    recipient = input('Enter your target audience: ')
    author = input('Enter the author: ')
    keywords = input("Enter keywords: ")
    topic_description = input("Enter topic description: ")
    background_info = input("Enter background information: ")
    arguments = input("Enter aurguments you would like to make, or leave it blank: ")
    solutions = input("Enter your proposed solutions or leave it blank: ")
    recommendations = input("Enter your recommendation chosen from your solutions. You are encouraged to make it more detailed. Feel free to leave this blank: ")
    memo_length = input("Enter memo length (< 2000 words): ")
    tone = input("Please choose a tone for your memo.\nBelow are some example tones you can reference:\n\
                 \n - Objective: The text should present information impartially and without bias, focusing on facts and data.\
                 \n - Persuasive: The text should aim to convince the reader to adopt a specific viewpoint or take a particular action.\
                 \n - Urgent: The text should convey a sense of importance and immediacy, emphasizing the need for quick action.\
                 \n - Optimistic: The text should maintain a positive outlook, focusing on opportunities and potential solutions.\
                 \n - Authoritative: The text should come across as confident and well-informed, showcasing expertise in the subject matter.\
                 \n - Conversational: The text should read as if the writer is engaging in a dialogue with the reader, using a more informal and relatable approach.\
                 \n\nPlease enter the tone: ")
    style = input("Please choose a style for your memo.\nBelow are some example styles you can reference:\n\
                  \n - Concise: The text should be brief and to-the-point, avoiding unnecessary details or excessive descriptions.\
                  \n - Comprehensive: The text should cover all relevant aspects of the topic, providing a thorough and in-depth analysis.\
                  \n - Narrative: The text should tell a story or present information in a chronological order, using anecdotes or examples to illustrate points.\
                  \n - Data-driven: The text should heavily rely on quantitative data, statistics, and evidence to support the arguments and recommendations.\
                  \n - Jargon-heavy: The text should use technical terms and specialized language, appropriate for an expert audience familiar with the subject matter.\
                  \n - Accessible: The text should use simple language and explanations, making the content easy to understand for a wider audience with varying levels of expertise.\
                  \n\nPlease enter the style: ")
    notes = input("Enter any other notes or enter nothing. e.g.,'Include a counter-argument for my recommended solution', 'The memo should be structured in five paragraphs', etc.\nEnter your note: ")
    return recipient, author, keywords, topic_description, background_info, arguments, solutions, recommendations, memo_length, tone, style, notes

def apply_user_feedback(prompt, feedback):
    """
    Apply user feedback to the generated policy memo.
    """
    updated_prompt = f"{prompt}\n\nFeedback: {feedback}\n\n"
    return generate_policy_memo(updated_prompt)


def main():
    """
    Assemble the functions into a working application.
    """
    # Get user inputs
    recipient, author, keywords, topic_description, background_info, arguments, solutions, recommendations, memo_length, tone, style, notes = get_user_inputs()

    # Create initial prompt string
    prompt = f"Please generate a well-written policy memo based on below instructions and give me suggestions on which aspects I should provide you more information in order to refine the memo after you write memo. Below are the instructions you should follow:\n\
        \nRecipient: {recipient}\
        \nAuthor: {author}\
        \nKeywords: {keywords}\
        \nTopic Description: {topic_description}\
        \nBackground Information: {background_info}\
        \nArguments: {arguments}\
        \nSolutions: {solutions}\
        \nRecommendations: {recommendations}\
        \nMemo Length: {memo_length}\
        \nTone: {tone}\
        \nStyle: {style}\
        \nAdditional Notes = {notes}\
        \n\nPolicy Memo:"

    # Generate and print the initial policy memo
    memo = generate_policy_memo(prompt)
    print("\nGenerated Policy Memo:\n\n")
    print(memo)

    # Iterate until the user is satisfied with the memo
    while True:
        feedback = input("\nEnter your feedback to help me refine it or type 'done' if satisfied: ")
        if feedback.lower() == 'done':
            break
        memo = apply_user_feedback(prompt, feedback)
        print("\nUpdated Policy Memo:\n")
        print(memo)

if __name__ == "__main__":
    main()