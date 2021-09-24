ipod <- sample(c(rep(1, 250),
                 rep(2,300),
                 rep(3, 600),
                 rep(4, 800),
                 rep(5, 550),
                 rep(6, 350),
                 rep(7, 100),
                 rep(8, 25),
                 rep(9, 20),
                 rep(10, 5)))
ipod
lists <- c()
listss <- c()
i <- 1
#Tao mot list ngau nhien tu mau co kich thuoc bang 25 (50 lan)
for (i in range(1:50)){
  lists <- sample(ipod, 25)
  listss[1:1000] <- c(lists)
  i <- i + 1
}
listss
t <- data.frame(listss, header = TRUE)
ggplot(t, aes(x=listss)) + 
  geom_histogram(binwidth = 1, boundary = 0.5, color = "green") +
  labs(x = "Do dai bai hat tinh bang phut",
       title = "Tan suat xuat hien cua nhung bai hat co do dai tu 1 den 10ph")
#Tinh xac suat xuat hien cua cac bai hat co do dai hon 6
1-pnorm(5, mean(listss), sd(listss))

#Tao mot list ngau nhien tu mau co kich thuoc bang 25 (500 lan)
lists1 <- c()
listss1 <- c()
for (i in range(1:500)){
  lists1 <- sample(ipod, 25)
  listss1[1:(25*500)] <- c(lists1)
  i <- i + 1
}
listss1
t1 <- data.frame(listss1, header = TRUE)
ggplot(t1, aes(x=listss1)) + 
  geom_histogram(binwidth = 1, boundary = 0.5, color = "black") +
  labs(x = "Do dai bai hat tinh bang phut",
       title = "Tan suat xuat hien cua nhung bai hat co do dai tu 1 den 10ph")
#Tinh xac suat xuat hien cua cac bai hat co do dai hon 6
1-pnorm(5, mean(listss1), sd(listss1))

#Tao mot list ngau nhien tu mau co kich thuoc bang 30 (30 lan)
lists2 <- c()
listss2 <- c()
for (i in range(1:30)){
  lists2 <- sample(ipod, 25)
  listss2[1:(30*30)] <- c(lists2)
  i <- i + 1
}
listss2
t2 <- data.frame(listss2, header = TRUE)
ggplot(t2, aes(x=listss2)) + 
  geom_histogram(binwidth = 1, boundary = 0.5, color = "red") +
  labs(x = "Do dai bai hat tinh bang phut",
       title = "Tan suat xuat hien cua nhung bai hat co do dai tu 1 den 10ph")
#Tinh xac suat xuat hien cua cac bai hat co do dai hon 6
1-pnorm(5, mean(listss2), sd(listss2))