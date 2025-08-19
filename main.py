from data_module import internet_users_graph, mental_disorders_graph, internet_users_dataset, mental_disorders_dataset

import time
# kind can be: line, scatter

def main():
        while True:
                time.sleep(1)
                print("Interface\n")
                print("1. View percent of people using the internet in Australia visualisation")
                print("2. View percent of people with mental disorders in Australia visualisation")       
                print("3. View percent of people using the internet in Australia dataset")
                print("4. View percent of people with mental disorders in Australia dataset")
                print("5. Exit") 

                interface_choice = input('Select choice: ').strip()

                if interface_choice == '1':
                
                        try:
                                kind = input('Select graph type (scatter, line): ').strip()
                                internet_users_graph(kind)

                        except ValueError:
                                print('Incorrect input, select from scatter or line')


                elif interface_choice == '2':
                        try:
                                kind = input('Select graph type (scatter, line): ').strip()
                                mental_disorders_graph(kind)

                        except ValueError:
                                print('Incorrect input, select from scatter or line')
                
                elif interface_choice == '3':

                        internet_users_dataset(None)
                        index = input('Filter through dataset by years')
                        internet_users_dataset(index)
                
                elif interface_choice == '4':
                        mental_disorders_dataset()

                elif interface_choice == '5':
                        break
                
                else:
                        print('Incorrect input, choose numbers 1-5')

                         
        
if __name__ == "__main__":
    main()