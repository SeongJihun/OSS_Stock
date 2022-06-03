import csv

infile = open("주식 결과 11.10.csv", "r", newline='')
filterfile=open("test11.10 데이터가 다 있는 파일.csv", "a", newline='')
outfile=open("testper11.10 필터 결과.csv", "a", newline='')
# shcode, hname, price, avg, high, low, PER, EPS, PEG, epsrt, netrt, ordrt, opert, salert
line=infile.readline()
line=infile.readline()
appendline=csv.writer(filterfile)
appendline1=csv.writer(outfile)

filternum=0 # 정보가 다 있는 종목의 갯수를 갠다
outfilenum=0 # PEG가 0.5이하이고, PER이 50이하이고, 20~25%의 순이익 성장율을 가진 종목

while line !="":
    splitline=line.split(',')
    filter=0 # 만약 filter=0이면 모든 데이터가 다 있음 따라서 filterfile에 shcode 저장, filter=1이면 shcode 저장 x
    for i in range(2, 14):
        if (splitline[i]=='0'):
            filter=1
    if (filter==0):
        filternum=filternum+1
        appendline.writerow(splitline)
        # 피터린치 공식 적용
        #if((float(splitline[6])<=50) and (float(splitline[8])<=0.5) and ((float(splitline[10])>=20) and (float(splitline[10])<=25))):
        if ((float(splitline[6]) <= 50)):
            outfilenum=outfilenum+1
            #appendline1.writerow(splitline)
    line=infile.readline()
infile.close()
filterfile.close()
outfile.close()
print("데이터가 온전한 종목의 수 : ", filternum, "공식에 부합하는 종목의 수 : ", outfilenum)