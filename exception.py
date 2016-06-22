#raise Exception

#raise Exception('custom exception message')

#create custom exception
__metaclass__ = type

class InvalidAgeException(Exception):
    pass
  
try:
    age = raw_input("Enter you age:")
    age = int(age)
    if age > 100 or age < 0:
        raise InvalidAgeException()
    elif age <18:
        print "You are a teneenager"
    else:
        print "You are an adult"
except InvalidAgeException as e:
    print "You have entered an invalid age"
except ValueError as e:
    print "Age should be integer"
except Exception as e:
    print "Something wrong happened"
else:
    print "Everything is good."
finally:
    print "Cleaning up the running"