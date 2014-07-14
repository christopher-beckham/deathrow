Exploratory analysis
===

This is a quick analysis of executed offenders from the Texas Department of Criminal Justice. It involved some mining of the tabular data [here](http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html), and the last statements of all those offenders (e.g. pages such as [this](http://www.tdcj.state.tx.us/death_row/dr_info/villegasjoselast.html)).

The tabular data has fields such as the first and last name of the offender, the age at which they were executed, the date of execution, and what their race was. This data was used to make some histograms.

The last statements from every offender were also scraped, consolidated and used to construct a wordcloud.

```r
library(psych)
library(ggplot2)
library(grid)
library(RColorBrewer)

df = read.csv("table.datecleaned.csv")
df$link1 = NULL
df$link2 = NULL
```

Graphs
---

This is a histogram showing the distribution of age of execution, colour-coded by race.

```r
ggplot(df, aes(x=age,fill=race) ) + geom_histogram(binwidth=3,colour="white") +
  theme(plot.margin=unit(c(1,1,1.5,1.2),"cm")) + scale_fill_brewer(palette="Spectral") +
  theme(plot.title = element_text(size=25, vjust=2)) +
  theme(axis.title.x = element_text(size=20, vjust=-1)) +
  theme(axis.title.y = element_text(size=20, vjust=3))  +
  theme(plot.margin=unit(c(1,1,1.5,1.2),"cm")) +
  ggtitle("Histogram of age, bins grouped by race")
```

![stuff](https://raw.githubusercontent.com/chrispy645/deathrow/master/R/figure/unnamed-chunk-11.png)

This is a density plot of the same thing, which may perhaps be clearer when it comes to visualising the median of each group.

```r
ggplot(df, aes(x=age, fill=race)) + geom_density(alpha=0.3) +
  theme(plot.margin=unit(c(1,1,1.5,1.2),"cm")) +
  theme(plot.title = element_text(size=25, vjust=2)) +
  theme(axis.title.x = element_text(size=20, vjust=-1)) +
  theme(axis.title.y = element_text(size=20, vjust=-1)) +
  theme(plot.margin=unit(c(1,1,1.5,1.2),"cm")) +
  ggtitle("Density plot of age (for each race)")
```

![stuff2](https://raw.githubusercontent.com/chrispy645/deathrow/master/R/figure/unnamed-chunk-12.png)

We can use the `describe` function to get exact numbers.

```r
describe(df[df$race == "White",]$age)
```
```
##   vars   n  mean   sd median trimmed mad min max range skew kurtosis   se
## 1    1 231 41.27 8.83     40   40.72 8.9  24  66    42  0.5    -0.38 0.58
```
```r
describe(df[df$race == "Black",]$age)
```
```
##   vars   n  mean   sd median trimmed  mad min max range skew kurtosis   se
## 1    1 190 37.43 7.54   36.5    36.8 8.15  24  62    38 0.67    -0.09 0.55
```

```r
describe(df[df$race == "Hispanic",]$age)
```
```
##   vars  n  mean  sd median trimmed  mad min max range skew kurtosis   se
## 1    1 92 37.08 7.4     36   36.57 7.41  24  59    35 0.56    -0.15 0.77
```

Execution counts by year:

![stuff3](https://raw.githubusercontent.com/chrispy645/deathrow/master/R/figure/unnamed-chunk-13.png)

Last statements
---

This is a word cloud of verbal/written last statements by prisoners before they were executed. This was created in R using the `wordcloud` library.

![wc](https://raw.githubusercontent.com/chrispy645/deathrow/master/R/figure/cloud.png)
