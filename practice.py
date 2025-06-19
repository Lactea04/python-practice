
#data_List = ["Alice", "Bob", "Alex", "Anderson", "Chris", "Katarina"]
#with open("C:\\Users\\kimtg\\OneDrive\\Desktop\\Test.txt", "w") as f:
#    for x in data_List:
#        f.write("%s\n" %x)
def process_Files(input_File, output_File):
    with (open("C:\\Users\\kimtg\\OneDrive\\Desktop\\%s" %input_File, "r") as infile,
          open("C:\\Users\\kimtg\\OneDrive\\Desktop\\%s" %output_File, "w") as outfile):
            for line in infile:
                upper_data = line.upper()
                outfile.write(upper_data)
process_Files("Test.txt", "Output.txt")
