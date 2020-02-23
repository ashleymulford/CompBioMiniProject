library(sleuth)
library(dplyr)

sample_id <- dir(file.path("/home/amulford/results"))
kal_dirs <- file.path("/home/amulford/results", sample_id)
condition<- c("2 days post-infection", "6 days post-infection", "2 days post-infection", "6 days post-infection")
table1<-as.data.frame(cbind(sample_id, condition, kal_dirs))

colnames(table1)<-c("sample", "condition", "path")
table1$sample<-as.character(table1$sample)
table1$condition<-as.character(table1$condition)
table1$path<-as.character(table1$path)

s_prep <- sleuth_prep(table1, extra_bootstrap_summary = TRUE)

s_fit <- sleuth_fit(s_prep, ~condition, 'full')
s_fit <- sleuth_fit(s_fit, ~1, 'reduced')
s_fit <- sleuth_lrt(s_fit, 'reduced', 'full')

sleuth_table <- sleuth_results(s_fit, 'reduced:full', 'lrt', show_all = FALSE)
sleuth_significant <- dplyr::filter(sleuth_table, qval <= 0.05)
save_sleuth_significant<-sleuth_significant[1:4]

write.table(save_sleuth_significant, "miniProject.log", append = TRUE, sep = "\t", col.names = TRUE, quote = FALSE, row.names = FALSE)
