import pandas as pd
import matplotlib.pyplot as plt
file_path=input("enter the excel and csv path:")
df=pd.read_excel(file_path)
print(df)
print("shape:",df.shape)
print("columns:",list(df.columns))
print(df.info())
print("/ninfo:")
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
print(df)
print(df.describe(include='all'))
numeric_cols=df.select_dtypes(include=['int64','float64']).columns
for col in numeric_cols:
    print("total:",df[col].sum())
    print("average:",df[col].mean())
    print("max:",df[col].max())
    print("min:",df[col].min())
for col in numeric_cols:
    print(f"\n  analysis of{col}  ")
    print("total:",df[col].sum())
    print("average:",df[col].mean())
    print("max:",df[col].max())
    print("min:",df[col].min())

cat_cols=df.select_dtypes(include=['object']).columns
                             
for col in cat_cols:
    print(f"\n   top values in {col}   ")
    print(df[col].value_counts().head())

    for col in numeric_cols:
        plt.figure()
        df[col].plot(kind="hist")
        plt.title(f"distribution of{col}")
        plt.xlabel(col)
        plt.ylabel("frequency")
        plt.show()


        df.to_csv("auto_clean_data.csv",index=fales)
        print("\nanalysis complete")
        print("clean file saved as:auto_clean_data.csv")
                              
                              

    


    
   
