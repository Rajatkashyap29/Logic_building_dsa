class Student :
    def __init__(self):
        self.students = [
            {"roll_num":12, "name":"rajat" ,"percentage":12},
            {"roll_num":13, "name":"ritik" ,"percentage":34},
            {"roll_num":14, "name":"rishav" ,"percentage":23},
            {"roll_num":15, "name":"manas" ,"percentage":15},
            {"roll_num":16, "name":"pragati" ,"percentage":8},
        ]
    def print_students(self):
        for s in self.students:
            print(s)
            # print(  s.get("name",None)      )
            
            # for key,value in s.items():
            #     print(key, value)
    def print_second_topper(self):
                
        i=0
        first_largest_elt = 0
        second_largest_element = 0
        
        ans_indx=-1
        first_indx =-1 
        
        while i < len(self.students):
            if self.students[i]["percentage"] > first_largest_elt :
                second_largest_element = first_largest_elt
                ans_indx = first_indx
                first_indx = i
                first_largest_elt = self.students[i]["percentage"]
                
            elif self.students[i]["percentage"] > second_largest_element and self.students[i]["percentage"] != first_largest_elt :
                second_largest_element = self.students[i]["percentage"]
                ans_indx = i
                    
            i+=1



        print(second_largest_element)    
        print(self.students[ans_indx])
        
        
        
        
   
s =  Student()     
# s.print_students()
s.print_second_topper()
