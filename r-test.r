
# R-Histogramme des Moduls BI BTX8506
# Daten:    NHANES
# Autoren:  Armon Dressler, Roger Tschanz
# Abgabe:   14.6.2019

# DPQ010 2007/2008 whole Histogram
ques_010_2007 <- read.csv("./bfh_bi_bokeh-master/data/2007_2008/questionnaire.csv")
summary(ques_010_2007)
hist(ques_010_2007$DPQ010, 
     main = paste("DPQ010 2007/2008 - Have little interest in doing things"),
     xlab="Questionnaire",
     breaks=50,
     ylab="Persons",
     col="lightblue",
     xlim=c(0,10)
)

# DPQ010 2013/2014 whole Histogram
ques_010_2013 <- read.csv("./bfh_bi_bokeh-master/data/2013_2014/questionnaire.csv")
summary(ques_010_2013)
hist(ques_010_2013$DPQ010, 
     main = paste("DPQ010 2013/2014 - Have little interest in doing things"),
     xlab="Questionnaire",
     ylab="Persons",
     breaks=50,
     col="salmon",
     xlim=c(0,10)
     #add=T
)

# DPQ010 2007/2008 without zero-Answers
ques_010_2007_vol2 <- subset(ques_010_2007, ques_010_2007$DPQ010!=0)
hist(ques_010_2007_vol2$DPQ010, 
     main = paste("DPQ010 2007/2008 - Have little interest in doing things Vol2"),
     breaks=50,
     xlab="Questionnaire",
     ylab="Persons",
     col=rgb(1,0,0,0.5),
     xlim=c(0,10),
     ylim=c(0,1000)
)

# DPQ010 2013/2014 w/o without zero-Answers
ques_010_2013_vol2 <- subset(ques_010_2013, ques_010_2013$DPQ010!=0)
hist(ques_010_2013_vol2$DPQ010, 
     main = paste("DPQ010 2013/2014 - Have little interest in doing things Vol2"),
     breaks=50,
     xlab="Questionnaire",
     ylab="Persons",
     col=rgb(0,0,1,0.5),
     xlim=c(0,10),
     ylim=c(0,1000)
)

legend("topright", 
       c("Over the last 2 weeks, how often did you have little 
         interest or pleasure in doing things? Would you say...",
         "",
         "0 - Not at all",
         "1 - Several days", 
         "2 - More than half the days", 
         "3 - Nearly every day",
         "7 - Refused",
         "9 - Dont' know"), 
       col="lightblue")
