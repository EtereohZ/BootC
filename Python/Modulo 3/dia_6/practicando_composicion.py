class Salary():
    def __init__(self, pay, bonus) -> None:
        self.pay = pay
        self.bonus = bonus          #Esta es una clase componente dado que sus atributos se están usando en otra clase
    
    def annual_salary(self):
        return (self.pay*12) + self.bonus #Ingresa la instancia creada en linea 15 mediante uso de metodo en linea 17



class Employee():
    def __init__(self, name, age , pay, bonus) -> None:
        self.name = name
        self.age = age
        self.employee_salary = Salary(pay, bonus)   #Este atributo es una instancia de la clase Salary()  
                                                     # Es un atributo al que se le ingresan 2 valores: pay y bonus. actuando como instancia que contiene 2 atributos: self.pay y self.bonus
    def total_salary(self):                           #Estamos usando componentes de otra clase, Siendo Employee() una clase compuesta
        return self.employee_salary.annual_salary()


e = Employee("max", 15, 1000, 100) #Si borramos la instancia de "e", en este caso, de Employee(), la instancia "employee_salary" de la clase Salary() dejará de existir

print(e.employee_salary.bonus) #estamos llamando al valor "bonus" dentro del atributo/instancia employee_salary. S
print(e.name)                   #Se le debe anteponer la instacia de la clase donde se encuentra, seguido de su atributo.
print(e.total_salary())          #Como también se está comportando como instancia de Salary() podemos llamar sus atributos: pay y bonus
print()
print(e)                    #instancia de Employee() imprime su dirección
print(e.employee_salary)    #Instancia de Salario() que existe como atributo en Employee()

print(list([e.employee_salary.pay, e.employee_salary.bonus]))

# lista = list(e.employee_salary.pay, e.employee_salary.bonus)
# print(list(e.employee_salary.pay, e.employee_salary.bonus))
'''
Ejemplo: Tenemos 2 clases, Libro() y Capitulos().
Un libro no es un capitulo ni un capitulo un libro, pero podemos delegar responsabilidades de una clase a otra.
Otra manera de decirlo es que una *forma parte* de otra

Ambas clases son inderdependientes.


'''