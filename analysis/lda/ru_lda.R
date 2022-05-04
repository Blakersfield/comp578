# Libraries
library(MASS)
library(ISLR)
library(caret)
library(dplyr)

# Data read
df <- read.csv('C:/Users/casas/Desktop/hourly_merge_shame_tier.csv')
df[is.na(df)] <- 0

# Data normalization
norm = preProcess(as.data.frame(df), method=c("range"))
df_norm = predict(norm, as.data.frame(df))

# Attach normalized data
attach(df_norm)

dim(df_norm)
head(df_norm)
summary(df_norm)

# Train test split
train = sample(1:nrow(df_norm[1]), nrow(df_norm)/2)
df_norm_train = df_norm[train, ]
df_norm_test = df_norm[-train, ]

df_norm_dep = df_norm
df_norm_dep = df_norm_dep[-1:-13]
df_norm_dep = df_norm_dep[-14:-26]

# # # # # # # #
# LDA Analysis #
# # # # # # # #
#'
#' S.P NASDAQ Silver Gold Palladium Bitcoin Ruble Hryvnia
#' Soybean Wheat Natural.Gas Corn
#'
df.lda.fit = lda(S.P ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$S.P)
df_lda_mean = list(c('S.P', temp))

df.lda.fit = lda(NASDAQ ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$NASDAQ)
df_lda_mean[[length(df_lda_mean)+1]] = c('NASDAQ', temp)

df.lda.fit = lda(DowJones ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$DowJones)
df_lda_mean[[length(df_lda_mean)+1]] = c('DowJones', temp)

df.lda.fit = lda(Silver ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$Silver)
df_lda_mean[[length(df_lda_mean)+1]] = c('Silver', temp)

df.lda.fit = lda(Gold ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$Gold)
df_lda_mean[[length(df_lda_mean)+1]] = c('Gold', temp)

df.lda.fit = lda(Palladium ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$Palladium)
df_lda_mean[[length(df_lda_mean)+1]] = c('Palladium', temp)

df.lda.fit = lda(Bitcoin ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$Bitcoin)
df_lda_mean[[length(df_lda_mean)+1]] = c('Bitcoin', temp)

df.lda.fit = lda(Ruble ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$Ruble)
df_lda_mean[[length(df_lda_mean)+1]] = c('Ruble', temp)

df.lda.fit = lda(Hryvnia ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$Hryvnia)
df_lda_mean[[length(df_lda_mean)+1]] = c('Hryvnia', temp)

df.lda.fit = lda(Soybean ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$Soybean)
df_lda_mean[[length(df_lda_mean)+1]] = c('Soybean', temp)

df.lda.fit = lda(Wheat ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$Wheat)
df_lda_mean[[length(df_lda_mean)+1]] = c('Wheat', temp)

df.lda.fit = lda(Natural.Gas ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$Natural.Gas)
df_lda_mean[[length(df_lda_mean)+1]] = c('Natural.Gas', temp)

df.lda.fit = lda(Corn ~ sentiment, data=df_norm)
df.lda.pred = predict(df.lda.fit, df_norm_test)
df.lda.class = df.lda.pred$class
temp = mean(df.lda.class==df_norm_test$Corn)
df_lda_mean[[length(df_lda_mean)+1]] = c('Corn', temp)

df_lda_mean