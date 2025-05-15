def main():
    
    stones = 20
    player = 1
    print("There are " + str(stones) + " stones left.")

    while stones > 0:
     

     remove_stones = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
     
     
    
     while remove_stones <1 or remove_stones > 2:
        
        remove_stones = int(input("Please enter 1 or 2: "))
        
     if remove_stones <= stones:  
        stones -= remove_stones
        print("")
        print("There are " + str(stones) + " stones left.")
        
            
     if stones == 1:
         remove_stones = int(input("Player " + str(3-player) + " would you like to remove 1 or 2 stones? "))
         stones -= remove_stones
         print("")
         print("Player " + str(player) + " wins!")
                
     
            
     if player == 1:
         player = 2
     else:
         player = 1   
     

    
        
        

if __name__ == '__main__':
    main()