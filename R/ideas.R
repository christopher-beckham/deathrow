boxplot(df$age ~ df$race)
hist(df$age,breaks=length(unique(df$age))*0.5)
hist(df$date,breaks=length(unique(df$date))*0.5)

plot(x=df$date, y=df$age, col=df$race, pch=19)

# library(psych) and also describe all of these

rev(sort(table(df$first_name)))[1:10]

rev(sort(table(df$last_name)))[1:10]