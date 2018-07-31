## <u>ZOMATO DELHI NCR DETAILS</u> <br> <br>

 ### DESCRIPTION : <br>
      It fetches the details of the famous restaurant linked to zomato in Delhi-NCR or use the already provided details in csv file 
      to visualize the data accordingly.

#### <b> Zomato API :</b> <br>
 &emsp;&emsp;Goto https://developers.zomato.com/api and login with your zomato credentials and click on API credentials then request 
 for an API key.
 '''

 <b>FILES INCLUDED: </b><br> 
      &emsp; - <b>zomato_details.py  :</b> To fetch the details.<br>
      &emsp; - <b>zomato_ncr.py      :</b> To visualize the fetched data or already provided csv file.<br>
      &emsp; - <b>zomato_cuisins.csv :</b> Details of cuisines in Delhi-NCR Restaurants.<br>
      &emsp; - <b>zomato_details.csv :</b> Details of famous restaurant linked to zomato.<br><br>

<b> MODULES REQUIRED : </b> <br>
     &emsp; &emsp;<b>1.If you want to fetch details with the python code(zomato_details.py) provided : </b><br>
            &emsp;&emsp;&emsp;-requests <br>
            &emsp;&emsp;&emsp;-json<br>
            &emsp;&emsp;&emsp;-pandas<br>
            &emsp;&emsp;&emsp;-sys<br>
            &emsp;&emsp;&emsp;-csv<br><br>
     &emsp;&emsp;<b>2. If you want to use provided details in csv file : </b><br>
            &emsp;&emsp;&emsp;-pandas <br>
            &emsp;&emsp;&emsp; -sys <br>
            &emsp;&emsp;&emsp;-matplotlib <br><br>
            
  ### <b> USAGE :</b> <br>
  &emsp;&emsp;<b>1.If you want to fetch details with the python code(zomato_details.py) provided : </b><br>
  &emsp;&emsp;&emsp; a) python3 zomato_details.py (Zomato API KEY) (Path to save zomato cuisine details) (path to save restaurant details) <br>
  &emsp;&emsp;&emsp; b) python3 zomato_ncr.py (zomato cuisine fetched csv file path) (zomato restaurant details fetched csv file path) <br><br>
  &emsp;&emsp;<b>2. If you want to use provided details in csv file : </b><br> 
   &emsp;&emsp; &emsp;python3 zomato_ncr.py (zomato cuisine saved csv file path) (zomato restaurant details saved csv file path) <br><br>
   
   <b> NOTE : </b> <br>
   &emsp;&emsp; use '/' in the path for windows OS.
   
          
