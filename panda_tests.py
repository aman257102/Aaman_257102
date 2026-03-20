# import pandas as pd

# df = pd.DataFrame([11, 22, 33], columns=['col_Name'])
# print(df)

# data = {
#     'Name': ['Madhav','Vishakha','Lalita','Rishabh'],
#     'Age': [16,17,18,19],
#     'salary': [90000,70000,50000,30000]
# }
# print(data)

# df=pd.DataFrame(data)
# print(df)
# print(type(df))


# print(df.head(2))
# print(df.tail(2))

# print(df.shape)
# print(df.columns)

# print(df.info())
# print(df.describe())


# print(df_age_filter= df[df['Age']>=18])
# df.where(df['Age'] >=18, other = 'Not Eligible')
# print(df.where)

# df['Team'] = ['CEO', 'HR','CTO','DA']

# df['Bonus'] = df['salary']* 0.20

# print(df)


# df.loc[0,'salary']=95000
# print(df.loc)

# df= df.drop(df[df.Name == 'Aman'].index)
# print(df)

# df= df.drop(df[df.Name == 'satpreet'].index)
# print(df)
# df.rename(columns={'salary':'Monthly_salary'},inplace=True)

# df.sort_values('salary')
# print(df)

# df['DOJ'] = ['2024-01-01','2024-01-15','2024-03-28','2024-03-03']
# print(df)
# df.isnu()
# print(df.isnull())

# df[df['Month']==1].value_counts()

# df[df['Month']==1].value_counts()


    

# import re

# def check_password_strength(password):
#     score = 0
#     suggestions = []

#     # Length check
#     if len(password) >= 8:
#         score += 1
#     else:
#         suggestions.append("Use at least 8 characters")

#     # Uppercase
#     if re.search(r"[A-Z]", password):
#         score += 1
#     else:
#         suggestions.append("Add uppercase letters")

#     # Lowercase
#     if re.search(r"[a-z]", password):
#         score += 1
#     else:
#         suggestions.append("Use lowercase letters")

#     # Special characters
#     if re.search(r"[!@#$%^&*(),.?/\\<>]", password):
#         score += 1
#     else:
#         suggestions.append("Add special characters")

#     return score, suggestions


# # Take input OUTSIDE the function
# password = input("Enter Your Password: ")

# strength, suggestions = check_password_strength(password)

# print("\nPassword strength:", strength)

# if suggestions:
#     print("Suggestions to improve:")
#     for s in suggestions:
#         print("-", s)
# else:
#     print("Your password is secure!")

# import random

# # Predefined responses
# responses = {
#     "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
#     "how are you": ["I'm fine!", "Doing great!", "All good!"],
#     "bye": ["Goodbye!", "See you later!", "Take care!"],
#     "name": ["I am your chatbot!", "You can call me Python Bot."],
# }

# # Default responses if no match
# default_responses = [
#     "I don't understand that.",
#     "Can you say that again?",
#     "Interesting... tell me more!",
# ]

# # Chat function
# def chatbot():
#     print("🤖 Chatbot: Hello! Type 'exit' to quit.\n")
    
#     while True:
#         user_input = input("You: ").lower()
        
#         if user_input == "exit":
#             print("🤖 Chatbot: Goodbye!")
#             break
        
#         found = False
        
#         for key in responses:
#             if key in user_input:
#                 print("🤖 Chatbot:", random.choice(responses[key]))
#                 found = True
#                 break
        
#         if not found:
#             print("🤖 Chatbot:", random.choice(default_responses))

# # Run chatbot
# chatbot()