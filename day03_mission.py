# Q 5.4~5.5
salutation = "salutation"
name = "name"
product = "product"
verbed = "verbed"
room = "room"
animals = "animals"
amount = "amout"
percent = "percent"
spokesman = "spokesman"
job_title = "job_title"
latter = '''    Dear {0} {1},
    Thank you for yput letter. we are sorry that our {2} {3} in your
{4}. please note that it should never be used in a {4}, especially near any
{5}.

    send us your receipt and {6} for shipping abd handling. we will send you
another {2} that, in our tests, is {7}% less likely to have {3}.

    Thank you for your support.
    sincerely,
    {8}
    {9}'''
print(latter.format(salutation,name,product,verbed,room,animals,amount,percent,spokesman,job_title))