library(rpart)
library(party)
library(caTools)
library(datasets)
library(dplyr)
library(stats)
library(magrittr)
library(tree)

set.seed(420)
data = read.csv('/Users/GiovanniFlores/Downloads/merged_data_daily.csv')


data[is.na(data)] <- 0


dim(data)


######## BAGGING DAILY DATA #############


data$NASDAQ = as.numeric(data$NASDAQ)
dt = sort(sample(nrow(data), nrow(data)*0.8))

train = data[dt, ]
test = data[-dt, ]

tree = tree(NASDAQ~sentiment + reply_count + retweet_count + like_count + quote_count + tweet_count, data=train) # builds tree to predict NASDAQ using all variables
plot(tree)
text(tree, pretty=1)

prediction = predict(tree, newdata=test)

mean((prediction - test$NASDAQ) * (prediction - test$NASDAQ)) 
# MSE = 464151.8


data$Bitcoin = as.numeric(data$Bitcoin)
dt = sort(sample(nrow(data), nrow(data)*0.8))
train = data[dt, ]
test = data[-dt, ]
tree = tree(Bitcoin~sentiment + reply_count + retweet_count + like_count + quote_count + tweet_count, data=train)
plot(tree)
text(tree, pretty=1)

prediction = predict(tree, newdata=test)

mean((prediction - test$Bitcoin) * (prediction - test$Bitcoin))
# MSE = 1766091


data$Ruble = as.numeric(data$Ruble)
dt = sort(sample(nrow(data), nrow(data) * 0.8))

train = data[dt,]
test = data[-dt, ]
tree = tree(Ruble~sentiment + reply_count + retweet_count + like_count + quote_count + tweet_count, data=train)
plot(tree)
text(tree, pretty=1)
prediction = predict(tree, newdata=test)


mean((prediction - test$Ruble) * (prediction - test$Ruble)) # 182.9397


data$DowJones = as.numeric(data$DowJones)
dt = sort(sample(nrow(data), nrow(data) * 0.8))
train = data[dt,]
test = data[-dt, ]
tree = tree(DowJones~sentiment + reply_count + retweet_count + like_count + quote_count + tweet_count, data=train)
plot(tree)
text(tree, pretty=1)
prediction = predict(tree, newdata=test)
summary(prediction)
mean((prediction - test$DowJones) * (prediction - test$DowJones))
# MSE = 770160.7

data$sentiment = as.numeric(data$sentiment)
dt = sort(sample(nrow(data), nrow(data) * 0.8 ))
train = data[dt,]
test = data[-dt,]
tree = tree(sentiment~reply_count + retweet_count + like_count + quote_count + tweet_count, data=train)
plot(tree)
text(tree, pretty=1)
prediction = predict(tree, newdata=test)
summary(prediction)
mean((prediction - test$sentiment) * (prediction - test$sentiment))
# MSE = 0.0007550203


data$Palladium = as.numeric(data$Palladium)
dt = sort(sample(nrow(data), nrow(data) * 0.8))
train = data[dt,]
test = data[-dt,]
tree = tree(Palladium~sentiment + reply_count + like_count + retweet_count, data=train)
plot(tree)
text(tree, pretty = 1)
prediction = predict(tree, newdata=test)
print(prediction)
mean((prediction - test$Palladium) * (prediction - test$Palladium)) # 86852.6

data$Gold = as.numeric(data$Gold)
dt = sort(sample(nrow(data), nrow(data) * 0.8))
train = data[dt,]
test = data[-dt,]
tree = tree(Gold~sentiment + reply_count + like_count + retweet_count, data=train)
plot(tree)
text(tree, pretty = 1)
prediction = predict(tree, newdata=test)
summary(prediction)
mean((prediction - test$Gold) * (prediction - test$Gold)) # 1102.542



####### BAGGING HOURLY DATA ####################

hourly_data = read.csv('/Users/GiovanniFlores/Downloads/hourly_merge_shame_tier.csv')
hourly_data

# df_norm_no0 = df_norm[!(is.na(df_norm$Gold.change) | df_norm$Gold.change==""), ]

norm_hourly_data_SP = hourly_data[!(is.na(hourly_data$S.P.change) | hourly_data$S.P.change==""),]


norm_hourly_data_SP$S.P.change = as.factor(norm_hourly_data_SP$S.P.change) 
dt = sort(sample(nrow(norm_hourly_data_SP), nrow(norm_hourly_data_SP) * 0.8))
train = norm_hourly_data_SP[dt,]
test = norm_hourly_data_SP[-dt,]

norm_tree = tree(S.P.change~sentiment + reply_count + like_count + retweet_count, data=train)
plot(norm_tree)
text(norm_tree, pretty = 1)
prediction = predict(norm_tree, newdata=test)
prediction
mean((prediction == test$S.P.change) * (prediction == test$S.P.change))








##### RANDOM FOREST DAILY #####



library(randomForest)


str(data)

index = sample(2, nrow(data), replace = TRUE, prob=c(0.8,0.2)) # 80/20

rf.train = data[index==1, ]
rf.test = data[index==2, ]

rfm = randomForest(sentiment~reply_count + like_count + retweet_count, data=rf.train)

sentiment_pred = predict(rfm, rf.test)

rf.test$sentiment_pred = sentiment_pred
# View(rf.test$sentiment_pred)

cfm = table(rf.test$sentiment, rf.test$sentiment_pred)


accuracy = sum(diag(cfm)/sum(cfm))
accuracy  # 0.5


rfm = randomForest(NASDAQ~sentiment + reply_count + like_count + retweet_count + quote_count + tweet_count, data=rf.train)

nasdaq_pred = predict(rfm, rf.test)

rf.test$nasdaq_pred = nasdaq_pred


cfm = table(rf.test$NASDAQ, rf.test$nasdaq_pred)


accuracy = sum(diag(cfm)/sum(cfm))
accuracy  # 0.167


rfm = randomForest(DowJones~sentiment + reply_count + like_count + retweet_count + quote_count + tweet_count, data=rf.train)

dowjones_pred = predict(rfm, rf.test)

rf.test$dowjones_pred = dowjones_pred

cfm = table(rf.test$DowJones, rf.test$dowjones_pred)


accuracy = sum(diag(cfm)/sum(cfm))
accuracy  # 0.167


rfm = randomForest(Palladium~sentiment + reply_count + like_count + retweet_count + quote_count + tweet_count, data=rf.train)

palladium_pred = predict(rfm, rf.test)

rf.test$palladium_pred = palladium_pred

cfm = table(rf.test$Palladium, rf.test$palladium_pred)

accuracy = sum(diag(cfm)/sum(cfm))
accuracy # 0.167


rfm = randomForest(S.P~sentiment + reply_count + like_count + retweet_count + quote_count + tweet_count, data=rf.train)

sp_pred = predict(rfm, rf.test)

rf.test$sp_pred = sp_pred

cfm = table(rf.test$S.P, rf.test$sp_pred)

accuracy = sum(diag(cfm)/sum(cfm))
accuracy # 0.167

rfm = randomForest(Silver~sentiment + reply_count + like_count + retweet_count + quote_count + tweet_count, data=rf.train)

silver_pred = predict(rfm, rf.test)

rf.test$silver_pred = silver_pred

cfm = table(rf.test$Silver, rf.test$silver_pred)

accuracy = sum(diag(cfm)/sum(cfm))
accuracy # 0.167

rfm = randomForest(Gold~sentiment + reply_count + like_count + retweet_count + quote_count + tweet_count, data=rf.train)

gold_pred = predict(rfm, rf.test)

rf.test$gold_pred = gold_pred

cfm = table(rf.test$Gold, rf.test$gold_pred)

accuracy = sum(diag(cfm)/sum(cfm))
accuracy # 0.167


rfm = randomForest(Bitcoin~sentiment + reply_count + like_count + retweet_count + quote_count + tweet_count, data=rf.train)

bitcoin_pred = predict(rfm, rf.test)

rf.test$bitcoin_pred = bitcoin_pred


cfm = table(rf.test$Bitcoin, rf.test$bitcoin_pred)

accuracy = sum(diag(cfm)/sum(cfm))
accuracy # 0.167

rfm = randomForest(Ruble~sentiment + reply_count + like_count + retweet_count + quote_count + tweet_count, data=rf.train)

ruble_pred = predict(rfm, rf.test)

rf.test$ruble_pred = ruble_pred


cfm = table(rf.test$Ruble, rf.test$ruble_pred)

accuracy = sum(diag(cfm)/sum(cfm))
accuracy # 0.333


rfm = randomForest(Hryvnia~sentiment + reply_count + like_count + retweet_count + quote_count + tweet_count, data=rf.train)

hryvnia_pred = predict(rfm, rf.test)

rf.test$hryvnia_pred = hryvnia_pred


cfm = table(rf.test$Hryvnia, rf.test$hryvnia_pred)
View(cfm)

accuracy = sum(diag(cfm)/sum(cfm))
accuracy # 0.1677









