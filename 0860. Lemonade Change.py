def lemonadeChange(self, bills) -> bool:
        b = len(bills)
        count_fives= 0
        count_tens= 0
        for i in range(b):
            if bills[i] == 5:
                count_fives +=1

            elif bills [i] ==10:
                if count_fives >0:
                    count_fives -=1
                    count_tens +=1                   
                else:
                    return False

            else:
                if count_fives >0 and count_tens>0:
                    count_fives -=1
                    count_tens -=1 
                elif count_fives >=3:
                    count_fives -=3
                else:
                    return False
        return True
            