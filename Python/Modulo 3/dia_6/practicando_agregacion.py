class Salary():
    def __init__(self, pay, bonus) -> None:
        self.pay = pay
        self.bonus = bonus          
    
    def annual_salary(self):
        return (self.pay*12) + self.bonus 



class Employee():
    def __init__(self, name, age , s): #Estamos ingresando como parametro la instancia de la clase Salary()
        self.name = name                #Nos estará pasando a self.employee_salary los argumentos que se le están dando, en linea 21
        self.age = age
        self.employee_salary = s
                              
    def total_salary(self):                      
        return self.employee_salary.annual_salary()


s = Salary(400, 30)
e = Employee("max", 15, s)      #En agregación, le pasamos al constructor de la clase Employee() (linea 12), una instancia de la clase Salary()
                                
print(e.employee_salary.bonus)
print(e.total_salary())
print(e.name)
print()
print(e)                    #instancia de Employee() imprime su dirección
print(e.employee_salary)    #Instancia de Salario() que existe como atributo en Employee()

'''
A diferencia de composicon, donde una es componente de otra,
En agregación las clases tienen una *relacion*
Ambas clases tienen sus instancias independientes, y luego se puede pasar una instancia a otra
Si una se borra, la otra puede existir independientemente

Tienen una relación unidireccional, solo una puede pasar a otra



'''