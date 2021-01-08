to clone this project copy the clone url.

go to your bash paste below lines.
git clone https://github.com/tailorsmit/django_assignment.git
cd django_assignment
hit enter.

now we have our code cloned.


if you have already installed django skip steps written below.

Step 1: pip install virtualenv      # To install virtualenv binary command
Step 2: virtualenv venv             # To create separate virtual environment for our project.
Step 3: source ./venv/bin/activate  # To activate virtual environment.
Step 4: pip install django          # To install django in out project.


Now, we have django installed.
Let's go and configure project dependency.

just copy below line to Install & use django_rest_framework
pip install djangorestframework

Now we have our app ready to run.
But, we need to apply migrations for all the tables we have used in django project.

just run this

python manage.py makemigrations
python manage.py migrate

i have user sqlite db but one can use Postgresql or another db.
So, migrations are ready we are good to go.

Let's run our server.
python manage.py runserver

you should see the url like http://127.0.0.1:8000/
go to your browser paste link hit enter.

you can see 2 endpoints 
1. http://127.0.0.1:8000/admin/
2. http://127.0.0.1:8000/api/user/

As, we have empty database we need to register user first.
go to,
http://127.0.0.1:8000/api/user/register/
fill all (Required)fields.
do post request.

Now, we have registered a user Navigate to 
haven't
and provide email and password. hit the POST.
Then, you can see your Token copy it and paste token to your header
Authorization : Token <<paste your token here>> (without <<>>)

Now, Navigate to, http://127.0.0.1:8000/api/user/me/
You should see the current logged in user.

So, we can see that verified field is False as we haven't confirmed our mobile no. yet.
NOTE: i haven't included mobile sms because most of sms Apis were Paid or have limited sms count a day.

To obtain the otp, Navigate to http://127.0.0.1:8000/api/user/request-otp/
if you have already verified your phone number you should see the response message As,
{'message' : 'user already verified'}
otherwise, you should see belo message
{'message': 'otp sent successfully'}

To verify the otp, Go to, http://127.0.0.1:8000/api/user/verify-otp/<<received otp>> (without <<>>)
if you have already verified your phone number you should see the response message As,
{'message' : 'user already verified'}
otherwise, you should see below message, if you provide valid otp.
{'message': 'phone number verified'}
if you dont provide valid otp, the you should see this message,
{'message': 'otp invalid'}


YOU HAVE REACHED TO THE END. IF MY CODE WORKS DO FOLLOW ME ON GITHUB, THANK YOU.
https://github.com/tailorsmit
