# # task 1 Створіть клас Editor, який містить методи view_document та edit_document.
# # Нехай метод edit_document виводить на екран інформацію про те, що редагування документів недоступне для безкоштовної версії.
# # Створіть підклас ProEditor, у якому цей метод буде перевизначено. Введіть ліцензійний ключ із клавіатури і, якщо він коректний,
# # створіть екземпляр класу ProEditor, інакше Editor. Викликайте методи перегляду та редагування документів.

class Editor:

    def __init__(self, document_name:str, license_key:str):
        self.document_name = document_name
        self.license_key = license_key

    def view_document(self):
            print(f'Ваш документ {self.document_name} готовий до перегляду')

    def edit_document(self):
        if self.license_key != '9A45bc':
            print(f'Редагування документів недоступне для безкоштовної версії')
        else:
            print(f'Ваш документ {self.document_name} готовий до редагування')


class ProEditor(Editor):

    def edit_document(self):
        if self.license_key == '9A45bc':
            super().edit_document()
        else:
            print(f'Редагування документів недоступне для безкоштовної версії')


doc1 = Editor('word1', '9A45bc')
doc1.view_document()

doc2 = ProEditor('word1', '9A45bc')
doc2.edit_document()

doc3 = Editor('word2', '9a')
doc3.edit_document()

# # task 2 Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші.
# # Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку.

class GraphicObj:
    
    def __init__(self, x_coord:int, y_coord:int):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def draw_func(self):
        print(f'Ви вказали координати X= {self.x_coord} та Y= {self.y_coord}')


class Rectangle(GraphicObj):

    def __init__(self, x_coord:int, y_coord:int):
        super().__init__(x_coord, y_coord)
        
    def start_draw(self):
        print(f'Початкові координати для створення прямокутника: x{self.x_coord}, y{self.y_coord}')


class MouseDriver:
    
    def __init__(self, left:bool, right:bool, up:bool, down:bool):
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def mouse_direction(self):
        if self.left == True:
            print('Мишка рухається ліворуч')
        elif self.right == True:
            print('Мишка рухається праворуч')
        elif self.up == True:
            print('Мишка рухається догори')
        elif self.down == True:
            print('Мишка рухається донизу')
        else:
            print('Мишка не рухається')

class Button(MouseDriver):
    
    def __init__(self, left:bool, right:bool, up:bool, down:bool, left_button:bool, right_button:bool):
        super().__init__(left, right, up, down)
        self.left_button = left_button
        self.right_button = right_button 
        
    def mouse_button(self):
        if self.left_button == True:
            print('Ви натиснули ліву кнопку миші')
        elif self.right_button == True:
            print('Ви натиснули праву кнопку миші')
        

coord1 = GraphicObj(15, 30)
coord1.draw_func()

coord1 = Rectangle(15, 30)
coord1.start_draw()

left1 = MouseDriver(False, False, True, False)
left1.mouse_direction()

left2 = Button(True, False, False, False, True, True)
left2.mouse_button()

# task 3 Створіть ієрархію класів із використанням множинного успадкування. Виведіть на екран порядок вирішення методів для кожного класу.
# Поясніть, чому лінеаризація даних класів виглядає саме так.

class Animals:

    def __init__(self, name:str, size:str, hunter:str):
        self.name = name
        self.size = size
        self.hunter = hunter

    def __str__(self):
        print(f'{self.name} is {self.size}')

    def hunting_level(self):
        print(f'{self.name} {self.hunter} hunt')
 

class Fish(Animals):

    def __init__(self, name:str, size:str, hunter:str, swim_depth:int):
        super.__init__(name, size, hunter)
        self.swim_depth = swim_depth

    def hunting_level(self):
        super().hunting_level()
        print(f'{self.name} {self.hunter} under water')

    def under_water(self):
        print(f'{self.name} can swin under water {self.swim_depth} meter')


class Bird(Animals):
    
    def hunting_level(self):
        super().hunting_level()
        print(f'{self.name} can fly in the sky')


animal1 = Animals('Tiger', 'middle', 'can')
animal2 = Animals('Elefant', 'big', 'cannot')
animal3 = Fish('Guppy', 'small', 'cannot', 15)
animal4 = Bird('Hawk', 'middle', 'can')
animal1.hunting_level()
animal2.hunting_level()
animal3.hunting_level()
animal4.hunting_level()

# task 4 Створіть UML-діаграми до завдань 1, 3 та 7. Збережіть їх у форматі *.uml.

# task 5 Використовуючи код example_10, створіть декоратор @staticmethod для визначення повноліття людини в Україні та Америки.
# * Використовуючи код example_10, створіть статичний метод класу  ( для створення використовуйте декоратор @staticmethod ),
# метод має приймати вік людини та перевіряти чи досягла вона повноліття, метод має повертати True або False

class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @staticmethod
    def full_year(surname, name, age):
        if age >= 18:
            print(f'{surname} {name} досяг повноліття')
        else:
            print(f'{surname} {name} не досяг повноліття')

MyClass1.full_year('Dovzhenko', 'Bogdan', 20)

people1 = MyClass1('Ivanenko', 'Ivan', 17)
people1.full_year('Ivanenko', 'Ivan', 17)        

# task 6 Використовуючи код example_10, створіть декоратори @classmethod для формування переліку об'єктів,
# які підрахують кількість повнолітніх людей в Україні та Америці.
# * Використовуючи код example_10, створіть класовий метод ( для створення використовуйте декоратор @classmethod ).
# Метод має підраховувати кількість об'єктів цього класу які досягли повноліття,
# для вирішення задачі використовуйте статичний метод створенний в завданні 5

# task 7 Створіть ієрархію класів транспортних засобів. У загальному класі опишіть загальні всім транспортних засобів поля,
# у спадкоємцях – специфічні їм. Створіть кілька екземплярів. Виведіть інформацію щодо кожного транспортного засобу.
