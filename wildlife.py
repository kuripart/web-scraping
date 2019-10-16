# Get a list a best moview per year as per rotten tomatoes
import sys, os, requests, bs4

url = "https://www.triviaquestionss.com/animal-trivia-questions/"

# Create the folder and text file
name_q = 'questions_wildlife.txt'
name_ans = 'answers_wildlife.txt'
os.makedirs('questions', exist_ok=True)
os.makedirs('answers', exist_ok=True)
q_file = os.path.join('questions', name_q)
ans_file = os.path.join('answers', name_ans)

# Get the html page
link = requests.get(url)
bs = bs4.BeautifulSoup(link.text, 'html.parser')

q_list = bs.select('h3')
ans_list = bs.select('p')

# Open a reference to the file to write to
q_file_ref = open(q_file, 'w')
ans_file_ref = open(ans_file, 'w')

# Write to the file as you loop through the element
for elem in q_list:
    q_file_ref.write(elem.getText() + '\n')

for elem in ans_list:
    ans_file_ref.write(elem.getText() + '\n')

q_file_ref.close()
