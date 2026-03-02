# TO DO LIST
def to_do_list():
    a=[]
    while(1):
        print("1.Add a task")
        print("2.Show task")
        print("3.Delete task")
        print("4.Delete whole list")
        print("5.Save as text file")
        print("6.Exit")
        try:
            b=int(input("Enter the number:"))
        except ValueError:
            print("The CHARACTER you entered is not an INTEGER !!!")
            continue
        match b:
            case 1:#1.Add a task
                add_task(a)
                continue
            case 2:#2.Show task
                show_task(a)
            case 3:#3.Delete task
                del_task(a)
                continue
            case 4:#4.Delete whole list
                clr_lst(a)
            case 5:#5.Exit
                save_exit(a)
            case 6:#Exit
                return
            case _:
                print("Invalid choice choose AGAIN !")
def add_task(a):
    t=input("Enter a task:")
    a.append(t)
    if len(a)>14:#setting up a limit so that users do not add unnecessary tasks at all
        print("Too many tasks.")
def show_task(a):
    if len(a)>0:
        for i in range (0,len(a)):
            print(i+1,a[i])
            print("\n")
    else:
        print("Sorry, but the task list is EMPTY !!")
def del_task(a):
    try:
        c=int(input("Enter the task no. that you want to Delete:"))
    except ValueError:
        print("Invalid character. TRY AGAIN !!")
    if 1<=c<=len(a):
        a.pop(c-1)
        print(f"Task '{c}' Deleted Successfully.")
    else:
        print("Task not found.")
def clr_lst(a):
    a.clear()
    print(a)
def save_exit(a):
    d=input("Do you want to save the file ? (y/n):")
    if d.lower() =="y":
        with open("TO_DO_.txt","w") as f:
            for i in range (0,len(a)): 
                f.write(f"{i+1}.{a[i]}\n")
    if d=="n":
        print("File not saved !")
print("Welcome User , Good Morning!")
a=input("Are you ready to make your to do list ? (y/n)")
if a.lower()=="y":
    to_do_list()
else:
    print("hope to see you NEXT TIME")
    exit