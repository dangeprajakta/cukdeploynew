from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import pandas as pd
import csv
from dateutil import parser
import pandas as pd
import numpy as np
from .forms import GeeksForm
from django.http import HttpResponse
# Create your views here.
#def home(request):
# return render(request, 'homepage.html')
#def new_page(request):
    # return render(request, 'newpage.html')


def home_view(request):
    context = {}
    if request.POST:
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES["geeks_field"])
            print(request.FILES["file"])
            #for chunk in request.FILES["geeks_field"].chunks():
                #print(chunk)
            temp = form.cleaned_data.get("empno")
            print(type(temp))
            print(temp)
            stdt = request.POST['start_date']
            print(stdt)
            stdt1=pd.to_datetime(stdt, format='%Y-%m-%d')
            print(type(stdt1))
            print(stdt1)
            endt = request.POST['end_date']
            print(endt)
            endt1=pd.to_datetime(endt, format='%Y-%m-%d')

            print(type(endt1))
            print(endt1)
            dataframe = pd.read_csv(request.FILES["file"])
            print(dataframe)
            #giving col name to each col
            dataframe.columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7']
            #convert col2 into datetime format
            dataframe['col2'] = pd.to_datetime(dataframe['col2'], format='%Y-%m-%d')
            print(dataframe['col2'])
            #fetching data from given date range
            filtered_df = dataframe.loc[(dataframe['col2'] >= stdt1)
                                & (dataframe['col2'] < endt1)]
            print("check this!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(filtered_df)
            if filtered_df.empty:
                print('either date range or employee number is invalid!!!!!!!!!!')
            finalfiltereddata = filtered_df.iloc[np.where(filtered_df['col1'] == temp)]
            print(finalfiltereddata)
            print("Till here everything is corect!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            entering_time = finalfiltereddata.groupby('col2')['col3'].first()
            print(entering_time)
            leaving_time = finalfiltereddata.groupby('col2')['col3'].last()
            print(leaving_time)
            r2 = leaving_time.reset_index()
            r1 = entering_time.reset_index()
            #
            merged_df = pd.merge(r1, r2, on="col2")
            print("after merging")
            merged_df.columns = ['Dates', 'EnteringTime', 'LeavingTime']
            # print("#################with colun names##############################################")
            print(merged_df)
            #
            # merged_df['Dates'] = pd.to_datetime(merged_df['Dates'])
            #
            merged_df['EnteringTime'] = pd.to_datetime(merged_df['EnteringTime'])
            merged_df['LeavingTime'] = pd.to_datetime(merged_df['LeavingTime'])
            #
            merged_df['dayOfWeek'] = merged_df['Dates'].dt.day_name()
            #
            merged_df['hours'] = merged_df['LeavingTime'] - merged_df['EnteringTime']
            print("_________________final format output----------------------------------")
            #
            print(merged_df)

            # seperate timestamp:
            merged_df['date_new'] = merged_df['EnteringTime'].dt.date
            merged_df['time_new'] = merged_df['EnteringTime'].dt.time
            #merged_df

            merged_df['l_date'] = merged_df['LeavingTime'].dt.date
            merged_df['l_time'] = merged_df['LeavingTime'].dt.time
            #merged_df

            filtered_new = merged_df.drop(['EnteringTime', 'LeavingTime', 'date_new', 'l_date'], axis=1)
            print(filtered_new)

            df1_transposed = filtered_new.T
            print(df1_transposed)





            df1_transposed.to_csv('col1_25_march2022.csv')











    else:
        form = GeeksForm()
    context['form'] = GeeksForm()
    return render(request, "homepage.html", context)






   # #data = request.GET['fulltextarea']
   # #stdt = request.GET['stdt']
   # data = request.POST
   # stdt = data.get("stdt")
   # print(stdt)
   # ftcontent= data.get("myfile")
   # print(ftcontent)
   # print(type(ftcontent))
   # print(type(stdt))
   # startdt = parser.parse(stdt)
   # print(type(startdt))
   # print(startdt)
   # endt = request.GET['endt']
   # print(endt)
   # print(type(endt))
   #
   # enddt=parser.parse(endt)
   # print(type(enddt))
   # print(enddt)
   # empno=request.GET['empno']
   # print(empno)
   # print("processing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
   #
   # datContent = [i.strip().split() for i in open("C:\\Users\\prajakta\\Downloads\\March_attlog.dat").readlines()]
   #
   # # print(datContent)
   # with open("./March_attlog.csv", "w") as f:
   #    cvswriter = csv.writer(f)
   #    # print(writer)
   #    # csvwriter.writerow(fields)
   #    cvswriter.writerows(datContent)
   #    print("written")
   # dataframe = pd.read_csv("./March_attlog.csv")
   # dataframe.columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7']
   # # print(dataframe)
   # # print((dataframe['col1'].dtype))
   # # print(type(empno))
   # empno1 = int(empno)
   # print("-----------", type(empno1))
   # col1_25 = dataframe.iloc[np.where(dataframe['col1'] == empno1)]
   # print(col1_25)
   # print("fetching data for given dATE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
   # # startdtdata = dataframe.iloc[np.where(dataframe['col2'] ==startdt )]
   # # print(startdtdata)
   # # enddtdata = dataframe.iloc[np.where(dataframe['col2'] ==enddt )]
   # # print(enddtdata)
   # dataframe['col2'] = pd.to_datetime(dataframe['col2'])
   # filtered_df = dataframe.loc[(dataframe['col2'] >= startdt)
   #                             & (dataframe['col2'] <= enddt)]
   # print(filtered_df)
   # finalfiltereddata = filtered_df.iloc[np.where(filtered_df['col1'] == empno1)]
   # print("!!!!!!!!check this!!!!!!!!!!!!!!")
   # print(finalfiltereddata)
   #
   # entering_time = filtered_df.groupby('col2')['col3'].first()
   # # entering_time
   # leaving_time = filtered_df.groupby('col2')['col3'].last()
   # r2 = leaving_time.reset_index()
   # r1 = entering_time.reset_index()
   #
   # merged_df = pd.merge(r1, r2, on="col2")
   # # print("after merging")
   # merged_df.columns = ['Dates', 'EnteringTime', 'LeavingTime']
   # print("#################with colun names##############################################")
   # # print(merged_df)
   #
   # merged_df['Dates'] = pd.to_datetime(merged_df['Dates'])
   #
   # merged_df['EnteringTime'] = pd.to_datetime(merged_df['EnteringTime'])
   # merged_df['LeavingTime'] = pd.to_datetime(merged_df['LeavingTime'])
   #
   # merged_df['dayOfWeek'] = merged_df['Dates'].dt.day_name()
   #
   # merged_df['hours'] = merged_df['LeavingTime'] - merged_df['EnteringTime']
   # print("_________________final format output----------------------------------")
   #
   # print(merged_df)
   # print(merged_df.head(5))
   # merged_df.to_csv('col1_25_march2022.csv')
   #
   #
   #
   #
   #
   #
   #
   #
   #
   #
   #
   #


   #return render(request, 'newpage.html', {'empno': empno})