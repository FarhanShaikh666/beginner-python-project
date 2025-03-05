def main():
    tasks = {}

    while True:

        try:

            print("\n=====TO-DO-LIST=====")
            print("1. Add tasks")
            print("2. show tasks")
            print("3. mark task as done")
            print("4. Exit")

            choice = int(input("\nenter your choice: "))

            if choice==1:
                no_task = int(input("how many tasks you wanna add: "))
                for i in range(0, no_task):
                    add_task = input("\nenter your task: ")
                    tasks[add_task]="un done"
                    print("Task added...~")
                    continue
            elif choice==2:
                print("\nTasks:")
                for task, status in tasks.items():
                    print(f"{task} : {status}")
                    continue
            elif choice==3:
                task_number_done = int(input("\nEnter the task number to mark as done: "))
                done_task_key = list(tasks.keys())[task_number_done-1]
                tasks[done_task_key]="Done"
                print("Task marked as done...~")
                continue
            elif choice==4:
                print("exiting the TO-DO-LIST")
                break
            else:
                print("Invalid choice, try again...!")
                continue



        except:
            print("something went wrong...!")

if __name__ == "__main__":
    main()