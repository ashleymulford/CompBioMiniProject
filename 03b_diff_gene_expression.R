#import libraries
library(sleuth)
library(dplyr)

sample_id <- dir(file.path("/home/amulford/results")) #list of srrs 
kal_dirs <- file.path("/home/amulford/results", sample_id) #list of paths
condition<- c("2 days post-infection", "6 days post-infection", "2 days post-infection", "6 days post-infection") #list of conditions
table1<-as.data.frame(cbind(sample_id, condition, kal_dirs)) #make data frame

colnames(table1)<-c("sample", "condition", "path") #add column names
table1$sample<-as.character(table1$sample) #convert to char from factor
table1$condition<-as.character(table1$condition)
table1$path<-as.character(table1$path)

#prep data
s_prep <- sleuth_prep(table1, extra_bootstrap_summary = TRUE)

#fit data
s_fit <- sleuth_fit(s_prep, ~condition, 'full')
s_fit <- sleuth_fit(s_fit, ~1, 'reduced')
#run test
s_fit <- sleuth_lrt(s_fit, 'reduced', 'full')

#output results
sleuth_table <- sleuth_results(s_fit, 'reduced:full', 'lrt', show_all = FALSE)
sleuth_significant <- dplyr::filter(sleuth_table, qval <= 0.05) #filter for signifcance
save_sleuth_significant<-sleuth_significant[1:4] #extract first four columns

#output to log
write.table(save_sleuth_significant, "miniProject.log", append = TRUE, sep = "\t", col.names = TRUE, quote = FALSE, row.names = FALSE)
