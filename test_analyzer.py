import pandas as pd
import matplotlib.pyplot as plt

def read_file():
    
    filename=input("Enter file name:") 
    sheetname=input("Enter sheet name:") 
    dataframe=pd.read_excel(filename,sheet_name=sheetname)
    dataframe['RegNumber'] = dataframe['RegNumber'].astype('int64')
    return dataframe


def subjectwise_topper(df,j):
    
    print()
    print()
    highest_grade=""
    print("Subject Code:",df.columns.values[j])
    
    for i in range(len(df)):
        if(df.iloc[i,j]=="O"):
            highest_grade="O"
            break
        elif(df.iloc[i,j]=="A+"):
            highest_grade="A+"
        elif(df.iloc[i,j]=="A" and highest_grade!="A+"):
            highest_grade="A"
        elif(df.iloc[i,j]=="B+" and highest_grade not in ("A+","A")):
            highest_grade="B+"
        elif(df.iloc[i,j]=="B" and highest_grade not in ("A+","A","B+")):
            highest_grade="B"
    print("Top Grade is ",highest_grade)
    print("Students:")
    for i in range(len(df)):
        if(df.iloc[i,j]==highest_grade):
            print(df.iloc[i,0]," ",df.iloc[i,1])

            
def subjectwise_arrear(df,j):
    
    count=0
    w=0
    print()
    print("Arrears:")
    for i in range(len(df)):
        if(df.iloc[i,j]=="U"):
            print(df.iloc[i,0]," ",df.iloc[i,1])
            count+=1
    else:
        print("NIL")
    print()
    print("Arrear Absentees:")
    for i in range(len(df)):
        if(df.iloc[i,j]=="UA"):
            print(df.iloc[i,0]," ",df.iloc[i,1])
            count+=1
    else:
        print("NIL")
    print("Withdrawn Students:")
    for i in range(len(df)):
        if(df.iloc[i,j]=="W"):
            print(df.iloc[i,0]," ",df.iloc[i,1])
            w+=1
    else:
        print("NIL")
    print("Withheld Students:")
    for i in range(len(df)):
        if(df.iloc[i,j]=="WH"):
            print(df.iloc[i,0]," ",df.iloc[i,1])
            w+=1
    else:
        print("NIL")        
    print("Pass Percentage:", ((len(df)-count-w)/(len(df)-w))*100)
    
    
def graph(df,j):
    
    y=[0,0,0,0,0,0,0,0,0]
    for i in range(len(df)):
        if(df.iloc[i,j]=="O"):
            y[0]+=1
        elif(df.iloc[i,j]=="A+"):
            y[1]+=1
        elif(df.iloc[i,j]=="A"):
            y[2]+=1
        elif(df.iloc[i,j]=="B+"):
            y[3]+=1
        elif(df.iloc[i,j]=="B"):
            y[4]=1
        elif(df.iloc[i,j]=="U"):
            y[5]+=1
        elif(df.iloc[i,j]=="UA"):
            y[6]+=1
        elif(df.iloc[i,j]=="WH"):
            y[7]+=1
        elif(df.iloc[i,j]=="W"):
            y[8]+=1
    x=[1,2,3,4,5,6,7,8,9]
    label=["O","A+","A","B+","B","U","UA","WH","W"]
    plt.bar(x, y, tick_label = label, width = 0.8, color = ['red', 'green'])
    plt.xlabel('Grades')
    plt.ylabel('Count')
    subject="Subject Code:"+df.columns.values[j]
    plt.title(subject)
    plt.show()
    
df=read_file()

start = int(input("Enter the starting column number of grades:")) 
end = int(input("Enter the ending column number of grades:")) 
for j in range(start-1, end):
    subjectwise_topper(df,j)
    subjectwise_arrear(df,j)
    graph(df,j)
    