import json
from datetime import date, datetime

list_notes = []
listNotesName = []



def openNote():
    try:
        with open("note1.json", "r", encoding='utf-8') as f:
            list_notes = json.loads(f.read())
            open_name = str(input('Введите название заметки\n'))
            if open_name in listNotesName:
                for item in list_notes:
                    if item.get('name') == open_name:
                        print("Текущий текст заметки: " + item.get('body_note'))
            else:
                print("Такой заметки не найдено. Попробуйте ввести правильное имя заметки")
    except:
            print("Созданных заметок не найдено")


def createNote():
    try:
        list_notes.append({'id': f"note_id_{len(list_notes)}", 'name': str(input('Введите название заметки\n')),
                       'creation_date': datetime.now().strftime('%d/%m/%y %H:%M'), 'last_edition': datetime.now().strftime('%d/%m/%y'),
                       'body_note': str(input('Введите текст заметки\n'))})
        if len(list_notes) != 0:
            listNotesName.append(list_notes[-1].get('name'))
        else:
            for item in list_notes:
               listNotesName.append(item.get('name')) 
        with open("note1.json", "w") as f:
            f.write(json.dumps(list_notes, indent=4))
        print("Заметка создана успешно")

    except:
            print("Не удалось сохранить заметку")       


def listNotes():
    try:
        with open("note1.json", "r", encoding='utf-8') as f:
            list_notes = json.loads(f.read())
            for item in list_notes:
                print("Заметка - Имя заметки " + item.get('name') + ", последнее изменение " + item.get('last_edition'))
                #listNotesName.append(item.get('name'))
            
    except:
            print("Созданных заметок не найдено")

        

def editNote():
        
        try:
            with open("note1.json", "r", encoding='utf-8') as f:
                list_notes = json.loads(f.read())
                edit_name = str(input('Введите название заметки, в которую необходимо внести изменения\n'))
                if edit_name in listNotesName:
                    for item in list_notes:
                        if item.get('name') == edit_name:
                            print("Текущий текст заметки: " + item.get('body_note'))
                            item['body_note'] = str(input('Введите новый текст заметки\n'))
                            item['last_edition'] = datetime.now().strftime('%d/%m/%y %H:%M')
                    print("Заметка изменена успешно")

                else:
                    print("Такой заметки не найдено. Попробуйте ввести правильное имя заметки")
 
                with open("note1.json", "w") as f:
                    f.write(json.dumps(list_notes, indent=4))
                
        
        except:
            print("Созданных заметок не найдено")


def deleteNote():
    try:
        with open("note1.json", "r", encoding='utf-8') as f:
            list_notes = json.loads(f.read())
            delList = []
            for item in list_notes:
                    delList.append(item.get('name'))
             
            del_name = str(input('Введите название заметки, которую необходимо удалить\n'))
            if del_name in delList:
                for item in list_notes:
                    if item.get('name') == del_name:
                        list_notes.pop(list_notes.index(item))
                        
                        print("Заметка удалена успешно")
            else:
                print("Такой заметки не найдено. Попробуйте ввести правильное имя заметки")        
            with open("note1.json", "w") as f:
                f.write(json.dumps(list_notes, indent=4))
            
    except:
            print("Созданных заметок не найдено")


def findNote():
    try:
        with open("note1.json", "r", encoding='utf-8') as f:
            list_notes = json.loads(f.read())
            findList =[]
            for item in list_notes:
                    findList.append(item.get('name'))
            find_name = str(input('Введите название заметки для поиска\n'))
            if find_name in findList:
                for item in list_notes:
                    if item.get('name') == find_name:
                        print(item.get('body_note'))
            else:
                print("Такой заметки не найдено. Попробуйте ввести правильное имя заметки")

    except:
            print("Созданных заметок не найдено")                


def findByDateNote():
    try:
        with open("note1.json", "r", encoding='utf-8') as f:
            list_notes = json.loads(f.read())
            find_date = str(input('Введите дату (DD/MM/YY) изменения заметки для поиска\n'))
            for item in list_notes:
                if datetime.strptime(item.get('last_edition'), "%d/%m/%y").date() >= datetime.strptime(find_date, "%d/%m/%y").date():
                    print("Заметка " + item.get('name') + " изменена " + item.get('last_edition'))
              
                else:
                    print("Такой заметки не найдено. Попробуйте ввести другую дату")
                
    except:
            print("Неправильно введена дата")                


def saveNote():
    print('Nothing to save')

while True:
    command = str(input('Список действующих команд: \n1 - [create] Создать новую заметку \n2 - [open] Открыть заметку \n3 - [list] Список всех заметок \n4 - [edit] Изменить заметку \n5 - [del] Удалить заметку \n6 - [find] Найти заметку \n7 - [findByDate] Найти заметку по дате \n0 - [exit] Выйти из приложения \n'))
    if command == '2' or command == 'open':
        openNote()
    elif command == '1' or command == 'create':
        createNote()
    elif command == '3' or command == 'list':
        listNotes()
    elif command == '4' or command == 'edit':
        editNote()
    elif command == '5' or command == 'del':
        deleteNote()
    elif command == '6' or command == 'find':
        findNote()
    elif command == '7' or command == 'findByDate':
        findByDateNote()
    elif command == '0' or command == "exit":
        break
    else:
        print("Введите команду из предложенного списка")



