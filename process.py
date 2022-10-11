# Using readlines()
#file1 = open('input.txt', 'r')
#Lines = file1.readlines()
import os, glob
from datetime import datetime
from datetime import timedelta
path = '/home/lmartinez/playground/TamboConciliation/data'
filename='tambodata'
with open(str(filename) + ".csv", 'a') as deposit:
    deposit.write('transaction_id,operation_timestamp,external_id,store_id,store_name,amount,operation_type,partner,payment_type,game_id,game_type'+ '\n')
for filetmp in glob.glob(os.path.join(path, '*.csv')):
    #print(filetmp)
    #return 0
    #datetemp=filetmp.split('.')[0].split('_')[-1]
    #file_date=datetime.strptime(datetemp, '%Y%m%d')
    with open(os.path.join(os.getcwd(), filetmp), 'r') as f: # open in readonly mode
        Lines = f.readlines()
        count = 0
        for line in Lines:
            count += 1
            if count>= 3 :
                with open(str(filename) + ".csv", 'a') as deposit:
                    if(line.split(';')[0] == 'PE0002') :
                        game_type='TDO'
                    else:
                        if(line.split(';')[0] == 'PE0003') :
                            game_type='TMM'
                        else :
                            game_type='undefined'
                    deposit.write(line.split(';')[2].split('@')[-1] + ',' + line.split(';')[3] + ' ' +  line.split(';')[4] +  ',,' + line.split(';')[2].split('@')[0] + ',,'  +   line.split(';')[5] + ',' + line.split(';')[1]  + ',tambo,'+ line.split(';')[7].strip()  + ',,' + game_type + '\n')

                    #print(line.strip()[184:197].strip() + ',' + line.strip()[25:55].strip())
                #print("Line{}: {}".format(count, line.strip()))
    
