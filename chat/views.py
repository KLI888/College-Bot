# views.py
from django.shortcuts import render, redirect
import openai
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import requests
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
openai.api_key = "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"





from django.http import JsonResponse, HttpResponse

# Helper function to load the JSON dataset
def load_question_set():
    # Path to your JSON file (adjust based on your project structure)
    json_path = os.path.join(os.path.dirname(__file__), "question_set.json")
    with open(json_path, "r") as file:
        return json.load(file)

# Helper function to find an answer in the JSON dataset
def find_answer_in_dataset(user_input, question_set):
    """
    Check if the user_input matches any question in the JSON dataset.
    Return both the answer and PDF download link (if available).
    """
    for entry in question_set:
        if user_input.lower() in map(str.lower, entry["question"]):
            # Return both the answer and the PDF (if it exists)
            return {
                "answer": entry["answer"],
                "pdf": entry.get("pdf")  # This will be None if 'pdf' key is not present
            }
    return None

# Google search function
def google_search(query, api_key, cx):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        search_results = response.json()
        if search_results:
            items = search_results.get("items", [])
            snippets = [item.get("snippet", "") for item in items]
            return snippets
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Main chat view
def chat_view(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")

        if user_input:
            # Step 1: Load the dataset
            question_set = load_question_set()

            # Step 2: Check the dataset for an answer
            dataset_result = find_answer_in_dataset(user_input, question_set)
            if dataset_result:
                answer = dataset_result["answer"]
                pdf = dataset_result.get("pdf")  # Get the PDF link if it exists
                
                # Save to history
                History.objects.create(
                    user_input=user_input,
                    api_output=answer,
                )
                
                if pdf:
                    # Step 3: Trigger automatic PDF download
                    response = HttpResponse()
                    response["Content-Disposition"] = f'attachment; filename="{os.path.basename(pdf)}"'
                    response["X-Accel-Redirect"] = pdf  # Link directly to the file URL
                    return response

                # Prepare the response context
                return render(request, "chat.html", {
                    "user_input": user_input,
                    "bot_response": answer,
                })

            # Step 4: Use Google Search if no dataset answer
            # api_key = 'AIzaSyCQNkYOhvCN9QCEs58V7wJAgK1fyp9-jjA'
            # cx = 'f71d379b602f542e3'
            snippets = google_search(user_input, api_key, cx)
            if snippets:
                snippet = snippets[0]  # Take the first snippet as the response
                History.objects.create(user_input=user_input, api_output=snippet)
                return render(request, "chat.html", {"user_input": user_input, "bot_response": snippet})

            # Step 5: Call ChatGPT if no Google result
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )

            if completion.choices:
                bot_response = completion.choices[0].message["content"]
                History.objects.create(user_input=user_input, api_output=bot_response)
                return render(request, "chat.html", {"user_input": user_input, "bot_response": bot_response})
            else:
                return render(request, "chat.html", {"user_input": user_input, "bot_response": "Failed to generate a response!"})

    return render(request, "chat.html")


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other desired page
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, "login.html")

    
def registerPage(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Create a new user instance
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        
        return redirect('loginPage')
    return render(request, "register.html")


def logoutPage(request):
    logout(request)
    return redirect('loginPage') 
def historyPage(request):
    history = History.objects.all()
    return render(request, "history.html", {'history': history})