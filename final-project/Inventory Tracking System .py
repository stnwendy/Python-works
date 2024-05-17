import pandas as pd
import json
from pathlib import Path
import sys

class function_list: # main class to bundle all the functions

    # function to initialize several variables
    def __init__(self): 
        self.is_newFile = False
        self.jsonRead_dict = {}
        self.tempData = {
            "Item Code": [],
            "Item Name": [],
            "Beginning Stock": [],
            "Unit of Measure": [],
            "Value per Unit": [],
            "Reorder Stock": [],
            "On-hand Stock": [],
            "Total Value": []
        }

    # function for the declaration of the username, password, and its conditions
    def login(self): 
        self.username = "Small Food Business"
        self.password = "98123food"
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username != "Small Food Business" and password != "98123food":
                print("\nInvalid username and password.")
                print("Please try again.")
                continue
            elif username != "Small Food Business":
                print("\nInvalid username. Please try again.")
                continue
            elif password != "98123food":
                print("\nInvalid password. Please try again.")
                continue
            else:
                print("\nLogged in successfully.\n")
                break
            
    # function for exiting the program   
    def sys_exit(self):
        self.load_data(self.joinPath)
        print("\nProgram terminated.")
        sys.exit()

    # function for loading an existing JSON file
    def load_data(self, joinPath): 
        with open(joinPath, "r") as openFile: 
            jsonRead = openFile.read()
        self.jsonRead_dict = json.loads(jsonRead) 
        
        
    # function for saving to a JSON file
    def save_data(self, joinPath, tempData): 
        with open(joinPath, "w") as saveFile:
            json.dump(tempData, saveFile)

    # function for the search/creation of a folder,"JSON Stock"
    # and the conditionals for the user-input file name
    def sys_bootup(self, fileExtend):
        self.joinPath = Path.cwd().joinpath("JSON Stock")
        if not self.joinPath.is_dir():
            self.joinPath.mkdir(parents=True)
            self.joinPath = self.joinPath.joinpath(fileExtend + ".json")
        else:
            self.joinPath = self.joinPath.joinpath(fileExtend + ".json")
        try:
            self.load_data(self.joinPath)
            print("File located.")
            self.is_newFile = False
        except FileNotFoundError:
            self.is_newFile = True
            print("File not found. Creating new file...")
            self.save_data(self.joinPath, self.tempData)
            self.load_data(self.joinPath)
            print("New file created.")


    # function for a separate print of the available services
    def show_services(self):
        print("\n"*2)
        print("\t\t\t\t\tSERVICES\n\n")
        print("\t\t\t\t\tCode\tDescription")
        print("\t\t\t\t\t[A]\tCheck Inventory")
        print("\t\t\t\t\t[B]\tAdd Items")
        print("\t\t\t\t\t[C]\tUpdate Items")
        print("\t\t\t\t\t[D]\tDelete Items")
        print("\t\t\t\t\t[E]\tStats for Nerds")
        print("\t\t\t\t\t[F]\tExit")
        

    # function for displaying the data using pandas table
    def display_table(self):
        if self.is_newFile == True:
            print("No data available.")
        else:
            table = pd.DataFrame(self.jsonRead_dict)
            print(table)

           
    # function to confirm the saving of the changes the user made 
    def confirm(self):
        confirm = ""
        while confirm == "":
            confirm  = input("\nConfirm to update data[y/n]: ")
            if confirm == "y" or confirm == "Y":
                self.is_newFile = False
                self.save_data(self.joinPath, self.jsonRead_dict)

                print("\nInventory updated.")
                print("This is your new inventory: \n")
                self.load_data(self.joinPath)
                self.display_table()
            elif confirm == "n" or confirm == "N":
                continue
            else:
                print("Invalid code.")
                continue
            
    # function to display inventory data
    def srvcCode_A(self):
        choose = ""
        while choose == "":
            choose  = eval(input("\nDo you want to search for a specific item [1] or display the whole table [2]? "))
            if choose == 1:
                self.load_data(self.joinPath)
                keyDis = input("\nEnter the item name to search [case sensitive]: ")
                if keyDis not in self.jsonRead_dict["Item Name"]:
                    print("Item not found in the inventory.")
                    pass
                else:
                    self.load_data(self.joinPath)
                    getIndex_Dis = self.jsonRead_dict["Item Name"].index(keyDis)
                    displayDict = {key: [self.jsonRead_dict[key][getIndex_Dis]] for key in self.jsonRead_dict}
                    disTable = pd.DataFrame(displayDict)
                    print(f"\n{disTable}")
            elif choose == 2:   
                print("\nThis is your current inventory:\n")
                self.load_data(self.joinPath)
                self.display_table()
            else:
                print("Invalid code.")
                continue

        

        
        
    # function to add inventory data
    def srvcCode_B(self):
        print("\nThis is your current inventory:\n")
        self.load_data(self.joinPath)
        self.display_table()
        
        storCode = []
        storName = []
        storQuan = []
        storUnit = []
        storValue = []
        storReorder = []
        storOnHand = []
        storTotalVal = []
        
        print("\n"*2)
        srvcQuan = int(input("Type the quantity of your service: "))
        for i in range(srvcQuan):
            itmCode = input("\nItem Code: ")
            itmName = input("Item Name: ")
            itmQuan = input("Beginning Stock Quantity: ")
            itmUnit = input("Unit of Measure: ")
            itmValue = input("Item value (per unit of measure): ")
            itmReorder = input("Reorder Stock Quantity: ")
            itmOnHand = input("On-hand Stock Quantity: ")
            tempTotal = float((eval(itmQuan)+eval(itmReorder)) * eval(itmValue))
            print(f"\nTotal Value: \u20b1 {tempTotal}")
            
            storCode.append(itmCode)
            storName.append(itmName)
            storQuan.append(itmQuan)
            storUnit.append(itmUnit)
            storValue.append(itmValue)
            storReorder.append(itmReorder)
            storOnHand.append(itmOnHand)   
            storTotalVal.append(str(round(tempTotal,2)))
            
            newData = {
                "Item Code": storCode,
                "Item Name": storName,
                "Beginning Stock": storQuan,
                "Unit of Measure": storUnit,
                "Value per Unit": storValue,
                "Reorder Stock": storReorder,
                "On-hand Stock": storOnHand,
                "Total Value": storTotalVal
                }
            
            self.load_data(self.joinPath)
            for i in newData["Item Code"]: 
                self.jsonRead_dict["Item Code"].append(i)
            for i in newData["Item Name"]: 
                self.jsonRead_dict["Item Name"].append(i)
            for i in newData["Beginning Stock"]:
                self.jsonRead_dict["Beginning Stock"].append(i)
            for i in newData["Unit of Measure"]:
                self.jsonRead_dict["Unit of Measure"].append(i)
            for i in newData["Value per Unit"]:
                self.jsonRead_dict["Value per Unit"].append(i)
            for i in newData["Reorder Stock"]:
                self.jsonRead_dict["Reorder Stock"].append(i)
            for i in newData["On-hand Stock"]:
                self.jsonRead_dict["On-hand Stock"].append(i)
            for i in newData["Total Value"]:
                self.jsonRead_dict["Total Value"].append(i)
            
        add_items = pd.DataFrame(newData)
        print(f"\n {add_items}")
        
        self.confirm()
            
    
     # function to update the value and quantity of an item                    
    def srvcCode_C(self): 
        if self.is_newFile == True:
            print("No dataavailable.")
        else:
            print("\nThis is your current inventory:\n")
            self.load_data(self.joinPath)
            self.display_table()
            keyUpd = input("\nEnter the item name to update [case sensitive]: ")
            if keyUpd not in self.jsonRead_dict["Item Name"]:
                print("Item not found in the inventory.")
                self.reSrvc
            else:
                selectIndex = self.jsonRead_dict["Item Name"].index(keyUpd)
                print("\nEncoding new data...\n")
                newQuan = input("Enter the new beginning quantity: ")
                newVal = input("Enter the new value: ")
                newReorder = input("Enter the new reorder quantity: ")
                newOnHand = input("Enter the new on-hand quantity: ")
                newTotal = float((eval(newQuan)+eval(newReorder)) * eval(newVal))
                self.jsonRead_dict["Beginning Stock"][selectIndex] = newQuan
                self.jsonRead_dict["Value per Unit"][selectIndex] = newVal
                self.jsonRead_dict["Reorder Stock"][selectIndex] = newReorder
                self.jsonRead_dict["On-hand Stock"][selectIndex] = newOnHand
                self.jsonRead_dict["Total Value"][selectIndex] = str(newTotal)
                
                self.confirm()
                
    # function to delete an inventory data          
    def srvcCode_D(self): 
        if self.is_newFile == True:
            print("No data available.")
        else:
            print("\nThis is your current inventory:\n")
            self.load_data(self.joinPath)
            self.display_table()
            keyDel = input("\nEnter the item name to delete [case sensitive]: ")
            if keyDel not in self.jsonRead_dict["Item Name"]:
                print("Item not found in the inventory.")
                self.reSrvc
            else:
                getIndex_Del = self.jsonRead_dict["Item Name"].index(keyDel)
                self.load_data(self.joinPath)
                del self.jsonRead_dict["Item Code"][getIndex_Del]
                del self.jsonRead_dict["Item Name"][getIndex_Del]
                del self.jsonRead_dict["Beginning Stock"][getIndex_Del]
                del self.jsonRead_dict["Unit of Measure"][getIndex_Del]
                del self.jsonRead_dict["Value per Unit"][getIndex_Del]
                del self.jsonRead_dict["Reorder Stock"][getIndex_Del]
                del self.jsonRead_dict["On-hand Stock"][getIndex_Del]
                del self.jsonRead_dict["Total Value"][getIndex_Del]
                
                self.confirm()
    
    #function to show the statistics
    def srvcCode_E(self): 
        if self.is_newFile == True:
                print("No data available.")
        else:
            totalQuan = 0
            totalReorder = 0
            totalonHand = 0
            endInv = 0
            begInv = 0
            newInv = 0
            expectedRev_total = 0
            actualRev_total = 0

            for i in range(len(self.jsonRead_dict["Item Name"])):
                quan = float(self.jsonRead_dict["Beginning Stock"][i])
                val = float(self.jsonRead_dict["Value per Unit"][i])
                reorder = float(self.jsonRead_dict["Reorder Stock"][i])
                onHand = float(self.jsonRead_dict["On-hand Stock"][i])
                totVal = float(self.jsonRead_dict["Total Value"][i])
                actualRevenue = (quan+reorder-onHand)*val
                beg = quan*val
                new = reorder*val
                end = onHand*val 
                
                totalQuan += quan
                totalReorder += reorder
                totalonHand += onHand
                endInv += end
                begInv += beg
                newInv += new
                expectedRev_total += totVal
                actualRev_total += actualRevenue
            
            
            cogs = (begInv + newInv) - endInv # cost of goods sold
            aveInventory = (begInv + endInv)/2 # average inventory
            gross = actualRev_total - cogs  # gross profit
            itr = cogs/aveInventory # inventory turnover ratio
            dsi = (aveInventory/cogs)*365 #days sale of inventory 
            sellTR = (((totalQuan+totalReorder)-(totalonHand))/(totalQuan+totalReorder))*100 #sell-through rate
                
            print("\nInventory Analysis:") 

            print(f"\n\u2022 Beginning Inventory: \u20b1 {round(begInv,2)}") 
            print("\n\tThis is the initial total value of items in stock at the start of this period.") 

            print(f"\n\u2022 Ending Inventory: \u20b1 {round(endInv,2)}") 
            print("\n\tThis is the total value of all items that are in stock at the end of a period. Use this to determine how much stock you will purchase in the next period. ") 

            print(f"\n\u2022 Cost of Goods Sold: \u20b1 {round(cogs,2)}")  
            print("\n\t This is the total amount you spent on expenses directly associated with the selling of goods, including the costs of the items needed for creating a product. Use this to assess your financial state and assure your gross profits. ") 

            print(f"\n\u2022 Expected Revenue: \u20b1 {round(expectedRev_total,2)}")  
            print("\n\tThis is the estimated total amount of revenue you can earn for this particular period. Use this to dentify how much you can spend for your next business strategy.") 

            print(f"\n\u2022 Actual Revenue: \u20b1 {round(actualRev_total,2)}")  
            print("\n\tThis determines your actual total amount of money made by selling the product or service. Use this to compare it to the Expected Revenue to identify any issues and mitigate such problems. ") 

            print(f"\n\u2022 Gross Profit: \u20b1 {round(gross,2)}")
            print("\n\tThis is the difference between your actual revenue and the cost of goods sold, a key financial measurement to assess your profitability and performance. Use this to analyze trends in your business for a better strategy.") 

            print(f"\n\u2022 Inventory Turnover Ratio: {round(itr,2)}") 
            print("\n\tThis indicates the number of times you sell and replaces the inventory during a period. The higher the ratio, the better, as it suggests that you are selling your inventory quickly and effectively. A low inventory turnover ratio may indicate that you have an has excess inventory, which can lead to higher carrying costs and potentially lower profitability. Use this to optimize your inventory management and business strategy.") 

            print(f"\n\u2022 Days Sale of Inventory: {round(dsi,2)}")
            print("\n\tThis is the average number of days it takes for you to sell the entire inventory. A low DSI indicates that you are selling the inventory quickly, while a high DSI suggests that you are holding onto inventory for an extended period, which can result to higher operating cost. Use this to optimize your inventory management and business strategy.") 

            print(f"\n\u2022 Sell-Through Rate: {round(sellTR,2)}%")
            print("\n\tThis is the percentage of you inventory sold during this period. A high STR indicates that you are effectively managing  inventory and is meeting customer demand, while a low STR suggests your inventory levels may be too high, or that demand for a particular product is low. Use this to optimize your inventory management and business strategy.") 


    # function to prompt user whether to use another service or not
    def reSrvc(self):
        while True:
            reSrvc = input("\nWould you like to use another service? [y/n] ")
            if reSrvc == "Y" or reSrvc == "y":
                    self.show_services()
                    print("\n"*2)
                    srvcCode = input("Enter Service Code: ")
                    if srvcCode == "A" or srvcCode == "a":
                        self.srvcCode_A()
                    elif srvcCode == "B" or srvcCode == "b":
                        self.srvcCode_B()
                    elif srvcCode == "C" or srvcCode == "c":
                        self.srvcCode_C()
                    elif srvcCode == "D" or srvcCode == "d":
                        self.srvcCode_D()
                    elif srvcCode == "E" or srvcCode == "e":
                        self.srvcCode_E()
                    elif srvcCode == "F" or srvcCode == "f":
                        self.sys_exit()
                    else:
                        print("\nInvalid code. Please try again.")
                        continue
            elif reSrvc == "N" or reSrvc == "n":
                self.sys_exit()
            else:
                print("Invalid code.")
                continue

# main function to layout the system
def main():
    print("\n"*2)
    print("\t\t\t\t\t\t Stock Count Tracking System \t\t\t\t\t\t")
    func = function_list()
    func.login()
    fileExtend = input("\nType in any file name: ")
    func.joinPath = fileExtend + ".json" 
    func.sys_bootup(fileExtend) 
    func.show_services()
    while True:
        print("\n"*2)
        srvcCode = input("Type the code of your choice: ")
        if srvcCode == "A" or srvcCode == "a":
            func.srvcCode_A()
            func.reSrvc()
        elif srvcCode == "B" or srvcCode == "b":
            func.srvcCode_B()
            func.reSrvc()
        elif srvcCode == "C" or srvcCode == "c":
            func.srvcCode_C()
            func.reSrvc()
        elif srvcCode == "D" or srvcCode == "d":
            func.srvcCode_D()
            func.reSrvc()
        elif srvcCode == "E" or srvcCode == "e":
            func.srvcCode_E()
            func.reSrvc()
        elif srvcCode == "F" or srvcCode == "f":
            func.sys_exit()
        else:
            print("Invalid code.")
            continue
    

main() # calling the main function
    
 
