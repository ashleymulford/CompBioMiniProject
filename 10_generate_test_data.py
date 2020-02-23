SRR_list = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]


for srr in SRR_list:
  file1 = open("/home/amulford/mini_project/SRR_seq_data/" + srr + ".1_1.fastq")
  file2 = open("/home/amulford/mini_project/SRR_seq_data/" + srr + ".1_2.fastq")
  test1 = open("/home/amulford/mini_project/SRR_seq_data/subset_" + srr + ".1_1.fastq", "w")
  test2 = open("/home/amulford/mini_project/SRR_seq_data/subset_" + srr + ".1_2.fastq", "w")
  lines_list1 = []
  for line in file1:
    lines_list1.append(line)
  lines_list2 = []
  for line in file2:
    lines_list2.append(line)
  for line in lines_list1[0:4000]:
    test1.write(line)
  for line in lines_list2[0:4000]:
    test2.write(line)
    
test1.close()
test2.close()
  
    
