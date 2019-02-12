# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


class Course:
    name  = "history"
    course_time  = "4:00pm"
    def print_time(self):
        print self.course_time
        

def check_name(name):
    if name == "ray" :
        return True
    elif name == "alan":
        return True
    else:
        return False
    
    

if __name__ == "__main__":
    #print "Hello World"
    var = 7  
    var = var ** 2
    #print var
    #var = "hello"
    #print var
    
    even_number = [2,4,6,8]
    odd_number = [1,3,5,7]
    all_number = []
    index = 0
    for x in odd_number:
        all_number.append(x)
        all_number.append(even_number[index])
        index = index + 1
    
    for x in all_number:
        if (x % 2 == 0):
            print ""
    
    first_name = "ray"
    last_name = "gao"

   
    #print ("My first name %s my last name %s" % (first_name, last_name)  )
    
    count = 5
    
    while (count  >0):
        print ""
        count -= 2
        
   
    for x in range(1,10):
        print ""
    
    found  = check_name("ray")
    if(found == True):
        print ""
    found  = check_name("alan")
    if(found == True):
        print ""
    found  = check_name("angela")
    if(found == False):
        print ""
        
    course = Course()
    
    course.print_time()
        
    
    