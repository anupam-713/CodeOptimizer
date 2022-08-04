from cv2 import transform
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # creating it multipurpose for now .
    Text = request.GET.get("text", "")
    language = request.GET.get("Language","")
    import pyparsing 
    if (language == "1"):
        commentFilter = pyparsing.pythonStyleComment.suppress()
    else:
        commentFilter = pyparsing.cppStyleComment.suppress() 
    new_text = commentFilter.transformString(Text)
    transformed_text = ""
    s = new_text.split("\n")
    for i in s:
        if (i.strip() != ""):
            transformed_text += i
    params = {"Converted_code": transformed_text, "Code": Text, "language" : language}
    return render(request, "index.html", params)




    
