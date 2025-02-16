from transformers import pipeline 

# set up the text generator pipeline with gpt-2 
generator=pipeline('text-generation',model='gpt2')

# Get user input 
user_prompt=input("Enter your query ")

generated_text=generator(user_prompt,max_length=50)

# Display the result 
print ("Generated text ")
print(generated_text)
