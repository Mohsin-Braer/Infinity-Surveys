from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList, view_form
from django.views.generic import TemplateView
from teamcreation.models import Teams
#from teamcreation.models import Groups
from register.models import UserProfile
from peerassessment.models import PeerAssessment

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.method == "POST": 
        if response.POST.get("save"): 
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else: 
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"): 
            txt = response.POST.get("new")
            if len(txt) > 2: 
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    # response.user 
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else: 
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

def dashboard(request):
    team_list = Teams.objects.all()
    field_value = get_field_value(request)
    return render(request, 'main/dashboard.html', {'team_list': team_list, 'field_value':field_value})

def views(request):
    team = request.GET['team']
    return render(request, 'main/view.html', {'team': team})

    n = Teams._meta.get_field(name)

def view(request):
    field_value = get_field_value(request) #for is_lead
    project = request.GET['project']
    team = Teams.objects.get(Project = project)
    team1 = str(team)
    peerassessments = PeerAssessment.objects.all()
    form = view_form()
    if 'submit' in request.POST:
        form = view_form(request.POST)
        if form.is_valid():
           cd = form.cleaned_data
           newstudent = cd['Name']
           tempUserProfile = UserProfile.objects.get(user=newstudent)
           team.members.add(tempUserProfile)
           form = view_form()
    else:
        form = view_form()
    class_avg = 0
    average= ''
    if 'publish1' in request.POST:
        for pa in peerassessments: 
            if pa.Team == team1: 
                average = (int(str(pa.question1Likert))+int(str(pa.question2Likert))+int(str(pa.question3Likert))+int(str(pa.question4Likert)))/5
                pa.Average = str(average)
                pa.Published = True
                pa.save()
        
        total = 0
        count = 0
        for pa in peerassessments:
            if pa.Team == team1:
                print(pa.Average)
                count+=1
                total += float((pa.Average).strip())
        class_avg = total/count

    if 'unpublish' in request.POST:
        for pa in peerassessments: 
            if pa.Team == team1: 
                pa.Published = False
                pa.save()
   
        
    
    return render(request, 'main/view.html', {'class_avg': class_avg,'average': average,'peerassessments':peerassessments,'form': form, 'team': team,'field_value':field_value, 'team1':team1})
    
def teamname(request):
    team = Teams.objects.get(id=1)
    teamname = team.name 
    return render(request, 'main/dashboard.html', {'teamname': teamname})

class projectPage(TemplateView):
    template_name = 'main/templates/view.html'

    def get(self, request):
        teams = Teams.objects.all()
        args = {'teams': teams}
        return render(request, self.template_name, args)

def group(request):
    name = Teams.objects.get(id=name)
    return render(request, 'main/view.html', {'name': name})

def get_field_value(request):
    username = request.user
    try:
        current_userprofile = UserProfile.objects.get(user = username)
        my_field = current_userprofile._meta.get_field('is_lead')
        field_value = my_field.value_from_object(current_userprofile)
    except UserProfile.DoesNotExist:
        field_value = True
    return field_value
    

    
'''bool_arr = []
    for obj in UserProfile.objects.all():
        my_field = UserProfile._meta.get_field('is_lead')
        field_value = my_field.value_from_object(obj)
        bool_arr.append(field_value)

    return bool_arr[-1]
    return field_value'''


def PAresponse(request):
    #field_value = get_field_value(request)
    project = request.GET['project']
    team = str(Teams.objects.get(Project = project))
    peerassessments = PeerAssessment.objects.all()
   
        
    #pa_list = list(set(pa.Name for pa in peerassessments))
    return render(request, 'main/PAresponse.html',{'peerassessments': peerassessments,'team':team})

def userprofile(request):
    userprof = UserProfile.objects.is_lead(request)
    return render(request, 'main/dashboard.html', {'userprof': userprof})