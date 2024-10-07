from openai import OpenAI

client = OpenAI()

def chat_with_gpt_4o_mini(prompt, max_tokens=150):
    """
    Function to chat with GPT-4o-mini model using OpenAI API.

    Parameters:
    prompt (str): The input prompt for the model.
    max_tokens (int): Maximum number of tokens in the model's response.

    Returns:
    str: The response from GPT-4o-mini.
    """
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.7)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("Chat with GPT-4o-mini (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chat_with_gpt_4o_mini(user_input)
        print(f"GPT-4o-mini: {response}")

if __name__ == "__main__":
    main()

