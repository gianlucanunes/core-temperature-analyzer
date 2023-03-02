> # 🧊 **Core Temperature Analyzer** 🔥
>
> 
> Monitoring your CPU temperature in order to predict overheating issues.
>
>
> ![Result](/images/1.png)
> 
>

### Overview
***
Hello! I created this project when I was struggling to analyze my CPU temperature. I was using Core Temp to measure it, but I did not know about its logging feature. Once I
discovered it, I thought "maybe I can create a Python program which analyzes the log files created by Core Temp and returns the average temperature from the last 5 days!" and I did it! It is a very simple solution yet, but I am planning to add more features and make it totally automated. Below, we have the features and, after that, a detailed tutorial
of how to set up the program and start using it.



### Features
***
- Organizes the measured temperatures in a intuitive spreadsheet (date + temperatures)
- Gives you the average temperature from the last 5 days
- Gives you the average temperature in each of the 5 days
- You can work with Celsius or Fahrenheit



### Tutorial
***  
> 1. **Install the program libraries using pip install.**  
  
There are a total of 7 libraries which are essential to the python program to work properly. Install them using pip install in your terminal.  
  
![Libraries](/images/6.png)  
  
  
***  
> 2. **Install Core Temp in your computer.**  
  
⚠️ Warning ⚠️ --> Core Temp must be installed in a folder outside Program Files. 
   
💡 Tip: install it in your Documents Folder or in your Desktop.  
  
  
***  
> 3. **After the installation, activate the Logging feature.**  
  
![Logging](/images/2.png)  
  
💡 Tip: You can configure the logging time. Go to Options > Settings > General. I personally recommend 60 seconds.  
    
   
***  
> 4. **Create a file in your computer called "temp.xlsx" (without the double quotes).**  
  
This excel file will contain all dates and measured temperatures in a more intuitive spreadsheet.  
  
![Temp](/images/3.png)  
  
💡 Tip: You can choose any name. I will use "temp" as an example.     
   
  
***  
> 5. **Now, you will need to open the file "core-temperautre-analyzer.py" to change the filepaths and directories.**  
  

For the temp file, there are some filepaths you will need to change. After each one, there is an example of how it needs to be.  
  
![TempDir](/images/4.png)  
  
Basically, replace "TEMP_FILE_PATH" with your temp.xlsx filepath.  
  
  
    
   
For the Core Temp directory, you will need to do the same, but it will need the directory where Core Temp has been installed (the folder containing the Core Temp.exe program).  
  
![CoreTempDir](/images/5.png)  
  
Basically, replace "CORE_TEMP_FOLDER" with the path to your Core Temp folder.  
  
  
***  
> 6. **Let Core Temp measure your CPU temperature for some time and confirm it is creating the log files in its folder (.csv files).**  
  
  
***  
> 7. **Close Core Temp and make sure it is not running in your background. Now, run the Python program and get the results!**   
   
⚠️ Warning ⚠️ --> Core Temp must be closed and not running in your background every time you run the program.  
  
⚠️ Warning ⚠️ --> Do not open the temp.xlsx file or the .csv files when running the program.  
  


💡 Tip: The core temperature analyzer change the log files names to start with "temperatures_processed" to avoid duplicate measures. After running the program, you can delete those files.   
  
💡 Tip: You can convert this python program to a .exe file using PyInstaller.  
  
  
  
***
### **Working with Fahrenheit** 🌡️     
  
If you want to work with Fahrenheit, delete the comment of these 2 lines of code: 
  
![Comment1](/images/7.png) 
   
Comment this line of code:    
  
![Comment2](/images/8.png)   
   
And change "mean_temp" in this line to "mean_temp_fahrenheit":  
  
![Fahrenheit](/images/9.png)  
  
  
  
***
### **Working with the brazilian standard** 🔵 🟢 🟡     
  
If you want to work with the brazilian standard, just comment the american standard and delete the comment from the brazilian standard. 


