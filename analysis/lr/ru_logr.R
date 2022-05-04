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

# # # # # # # # # # # #
# Logistic Regression #
# # # # # # # # # # # #
df.glm.fit = glm(S.P ~ sentiment + reply_count + retweet_count
                  + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((S.P - df.glm.probs)**2)
df_glm_mean = list(c('S.P', temp))

df.glm.fit = glm(NASDAQ ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((NASDAQ - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('NASDAQ', temp)

df.glm.fit = glm(DowJones ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((DowJones - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('DowJones', temp)

df.glm.fit = glm(Silver ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((Silver - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('Silver', temp)

df.glm.fit = glm(Gold ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((Gold - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('Gold', temp)

df.glm.fit = glm(Palladium ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((Palladium - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('Palladium', temp)

df.glm.fit = glm(Bitcoin ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((Bitcoin - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('Bitcoin', temp)

df.glm.fit = glm(Ruble ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((Ruble - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('Ruble', temp)

df.glm.fit = glm(Hryvnia ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((Hryvnia - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('Hryvnia', temp)

df.glm.fit = glm(Soybean ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((Soybean - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('Soybean', temp)

df.glm.fit = glm(Wheat ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((Wheat - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('Wheat', temp)

df.glm.fit = glm(Natural.Gas ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((Natural.Gas - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('Natural.Gas', temp)

df.glm.fit = glm(Corn ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, family=quasibinomial)
df.glm.probs = predict(df.glm.fit, df_norm, type="response")
temp = mean((Corn - df.glm.probs)**2)
df_glm_mean[[length(df_glm_mean)+1]] = c('Corn', temp)

df_glm_mean