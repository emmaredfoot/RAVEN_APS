def multipleHistories(filename, season):
    lines = open(filename,"r").readlines()
    header = lines.pop(0)
    demand = []
    hours  = []
    for cnt, line in enumerate(lines):
        if line.strip().split(",")[0].strip() == "23":
            # first line
            start_counter = cnt
        elif line.strip().split(",")[0].strip() == "12":
            # last line
            demand.append([float(lin.strip().split(",")[1]) for lin in lines[start_counter:cnt+1] if len(lin.strip()) > 0] )
            hours.append ([int(lin.strip().split(",")[0]) for lin in lines[start_counter:cnt+1] if len(lin.strip()) > 0] )
        elif line.strip().split(",")[0].strip() == "11":
            demand.append([float(lin.strip().split(",")[1]) for lin in lines[start_counter:cnt+1] if len(lin.strip()) > 0] )
            hours.append ([int(lin.strip().split(",")[0]) for lin in lines[start_counter:cnt+1] if len(lin.strip()) > 0] )
        elif line.strip().split(",")[0].strip() == "00":
            # last line
            demand.append([float(lin.strip().split(",")[1]) for lin in lines[second_counter:cnt+1] if len(lin.strip()) > 0] )
            hours.append ([int(lin.strip().split(",")[0]) for lin in lines[second_counter:cnt+1] if len(lin.strip()) > 0] )

        for hist_cnt in range(len(demand)):
          f_obj = open(season+str(hist_cnt)+".csv","w")
          f_obj.write(header.rstrip().strip()+"\n")
          for ts in reversed(range(len(hours[hist_cnt]))):
            f_obj.write(str(hours[hist_cnt][ts])+","+str(demand[hist_cnt][ts])+"\n")
          f_obj.close()

        InputFile=open("raw_data_"+season+".csv","w")
        #InputFile.write("scaling,filename"+"\n")
        for hist_cnt in range(len(demand)):
            InputFile.write("1"+","+season+str(hist_cnt)+".csv"+"\n")
        InputFile.close()



Spring=multipleHistories("SpringEIA.csv", "spring_")
Summer=multipleHistories("SummerEIA.csv", "summer_")
Fall=multipleHistories("FallEIA.csv", "fall")
Winter=multipleHistories("WinterEIA.csv", "winter_")
