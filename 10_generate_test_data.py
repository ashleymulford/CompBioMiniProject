#This script was used to generate the files found in test_data
#It is not used in the wrapper

SRR_list = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]

for srr in SRR_list:
  #open files with full data set
  file1 = open("/home/amulford/mini_project/SRR_seq_data/" + srr + ".1_1.fastq")
  file2 = open("/home/amulford/mini_project/SRR_seq_data/" + srr + ".1_2.fastq")
  test1 = open("/home/amulford/mini_project/SRR_seq_data/" + srr + ".1.fastq", "w")
  test2 = open("/home/amulford/mini_project/SRR_seq_data/" + srr + ".2.fastq", "w")
  #put lines of file into list
  lines_list1 = []
  for line in file1:
    lines_list1.append(line)
  lines_list2 = []
  for line in file2:
    lines_list2.append(line)
  #write out first 4000 lines of the full data set into subset files
  for line in lines_list1[0:40000]:
    test1.write(line)
  for line in lines_list2[0:40000]:
    test2.write(line)
    
test1.close()
test2.close()
  
    
