from django import template

register = template.library()

def my_template(value, arg):
    if arg == 'change':
        value = 'Rahim'
        return value
    
register.filter('change_name', my_template)

#ratin.cse@gmail.com