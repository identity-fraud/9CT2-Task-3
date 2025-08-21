from data_module import internet_users_graph, mental_disorders_graph, internet_users_dataset, mental_disorders_dataset, combined_graphs

def main():
        while True:
                print(" -- Interface -- ")
                print("1. View percent of people using the internet in Australia visualisation")
                print("2. View percent of people with mental disorders in Australia visualisation")       
                print("3. View percent of people using the internet in Australia dataset")
                print("4. View percent of people with mental disorders in Australia dataset")
                print("5. View combined graphs of both")
                print("6. Exit") 
                print(" -- Interface -- ")

                interface_choice = input('Select choice: ').strip()

                if interface_choice == '1':
                
                        try:
                                kind = input('Select graph type (scatter, line): ').strip().lower()
                                print('Close graph to continue')
                                internet_users_graph(kind)

                        except ValueError:
                                print('Incorrect input, select from scatter or line')


                elif interface_choice == '2':
                        try:
                                kind = input('Select graph type (scatter, line): ').strip().lower()
                                print('Close graph to continue')
                                mental_disorders_graph(kind)

                        except ValueError:
                                print('Incorrect input, select from scatter or line')
                
                elif interface_choice == '3':
                        year = input('Filter through dataset by years (Press enter to output full dataset): ')
                        internet_users_dataset(year)
                        input('Press enter to continue: ')
                
                elif interface_choice == '4':
                        year = input('Filter through dataset by years (Press enter to output full dataset): ')
                        mental_disorders_dataset(year)
                        input('Press enter to continue: ')
                
                elif interface_choice == '5':
                        try:
                                print('Close graph to continue')
                                combined_graphs()

                        except ValueError:
                                print('Incorrect input, select from scatter or line')

                elif interface_choice == '6':
                        print('Exit')
                        break
                
                else:
                        print('Incorrect input, choose numbers 1-5')

                         
        
if __name__ == "__main__":
    main()