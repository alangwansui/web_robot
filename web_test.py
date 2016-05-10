from web_robot import Web_Robot 
        
b = Web_Robot()
b.get("http://127.0.0.1:8069")
b.send_key( 'db', 'szodoo2')
b.execute_script("document.getElementById('dbselector').submit()")
b.send_key('login', 'admin')
b.send_key('password', '2d22')
b.click_button('btn-primary')

        


    


    


 

# b = webdriver.Firefox() # Get local session of firefox
# b.get("http://127.0.0.1:8069") # Load page
# send_key(b, 'db', 'szodoo2')
# b.execute_script("document.getElementById('dbselector').submit()")
# send_key(b, 'login', 'admin')
# send_key(b, 'password', '2d22')
# bt_click(b,'btn-primary')
    

    









