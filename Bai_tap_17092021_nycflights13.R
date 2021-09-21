#Install and update packages
install.packages("nycflights13")
update.packages("nycflights13")
install.packages("ggmap")
update.packages("ggmap")
install.packages("ggplot2")
update.packages("ggplot2")
install.packages("dplyr")
update.packages("dplyr")

#lib?ary packages
library(nycflights13)
library(ggplot2)
library(dplyr)
library(ggmap)

#1.Ve do thi scatter
#loc ra cac chuyen bay cua hang
Alsska Airlines Inc.
alaska_flights <- flights %>%
  filter(carrier == "AS")
ggplot(data = alaska_flights,
       mappin? = aes(x = dep_delay, y = arr_delay)) +
  geom_point()

#2.Ve do thi Linegraphs 
#Origin la "EWR" va month=1 va day<15;
early_january_weather <- weather %>%
  filter(origin == "EWR" & month == 1 & day <= 15)
ggplot(data = early_january_weather,
       mapp?ng = aes(x = time_hour, y = temp)) +
  geom_line()

#3.Ve do thi Histograms phan bo cua bien temp trong bang weather
ggplot(data = weather, mapping = aes(x = temp)) +
  geom_histogram()

#4.Ve bieu do boxplot mo ta su phan bo cua bien temp (nhiet do) theo cac thang
ggplot(data = weather, mapping = aes(x = factor(month), y = temp)) +
  geom_boxplot()

#5.Ve bieu do barplot the hien so luong cac chuyen bay theo cac hang may bay (carrier)
ggplot(data = flights, mapping = aes(x = carrier)) +
  geom_bar()
