import os 

def generate_decompressed_files(path):
    base_path = "/home/simon/Development/REDD/decompressed"
    delim = " "
    with open(path, mode='rt') as input_file:       
        
        current_tag = "hejsa"
        current_house = "hejsa"
        current_channel = "hejsa"
        f = 69
        
        for row in input_file:
            
            line = row.split(delim)

            if line[0] != current_tag:

                try:
                    f.close()
                except:
                    print("Could not close f")
                
                current_tag = line[0]

                new_house = current_tag.split("-")[0]
                current_channel = current_tag.split("-")[1]

                if current_house != new_house:
                    current_house = new_house
                    path_to_house = os.path.join(base_path, current_house)

                    if not os.path.exists(path_to_house):
                        os.mkdir(os.path.join(base_path, current_house))

                f = open(os.path.join(base_path, current_house, current_channel + "_sorted.csv"), mode='wt')

            f.write(line[0] + " " + line[1] + " " + line[2])


generate_decompressed_files("/home/simon/master_public_datapointview.csv")
