# # # # # # # #
# Gold.change #
# # # # # # # #
df_norm_no0 = df_norm[!(is.na(df_norm$Gold.change) | df_norm$Gold.change==""), ]
train = sample(1:nrow(df_norm_no0[1]), nrow(df_norm_no0)/2)
df_norm_no0_train = df_norm_no0[train, ]
df_norm_no0_test = df_norm_no0[-train, ]
df_lda_fit = lda(Gold.change ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, data=df_norm_no0_train,
                 na.action = na.omit)
df_lda_pred = predict(df_lda_fit, df_norm_no0_test)
df_lda_class = df_lda_pred$class
df_table = table(df_lda_class, df_norm_no0_test$Gold.change)
df_lda_cm = list(df_table)
df_lda_cm_acc = list(sum(diag(df_table)/sum(df_table)))


# # # # # # # # #
# Silver.change #
# # # # # # # # #
df_norm_no0 = df_norm[!(is.na(df_norm$Silver.change) | df_norm$Silver.change==""), ]
train = sample(1:nrow(df_norm_no0[1]), nrow(df_norm_no0)/2)
df_norm_no0_train = df_norm_no0[train, ]
df_norm_no0_test = df_norm_no0[-train, ]
df_lda_fit = lda(Silver.change ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, data=df_norm_no0_train,
                 na.action = na.omit)
df_lda_pred = predict(df_lda_fit, df_norm_no0_test)
df_lda_class = df_lda_pred$class
df_table = table(df_lda_class, df_norm_no0_test$Silver.change)
df_lda_cm[[length(df_lda_cm)+1]] = df_table
df_lda_cm_acc[[length(df_lda_cm_acc)+1]] = sum(diag(df_table)/sum(df_table))


# # # # # # # # # #
# Palladium.change #
# # # # # # # # # #
df_norm_no0 = df_norm[!(is.na(df_norm$Palladium.change) | df_norm$Palladium.change==""), ]
train = sample(1:nrow(df_norm_no0[1]), nrow(df_norm_no0)/2)
df_norm_no0_train = df_norm_no0[train, ]
df_norm_no0_test = df_norm_no0[-train, ]
df_lda_fit = lda(Palladium.change ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, data=df_norm_no0_train,
                 na.action = na.omit)
df_lda_pred = predict(df_lda_fit, df_norm_no0_test)
df_lda_class = df_lda_pred$class
df_table = table(df_lda_class, df_norm_no0_test$Palladium.change)
df_lda_cm[[length(df_lda_cm)+1]] = df_table
df_lda_cm_acc[[length(df_lda_cm_acc)+1]] = sum(diag(df_table)/sum(df_table))


# # # # # # # # # # #
# Natural.Gas.change #
# # # # # # # # # # #
df_norm_no0 = df_norm[!(is.na(df_norm$Natural.Gas.change) | df_norm$Natural.Gas.change==""), ]
train = sample(1:nrow(df_norm_no0[1]), nrow(df_norm_no0)/2)
df_norm_no0_train = df_norm_no0[train, ]
df_norm_no0_test = df_norm_no0[-train, ]
df_lda_fit = lda(Natural.Gas.change ~ sentiment + reply_count + retweet_count
                 + like_count + quote_count + tweet_count, data=df_norm_no0_train,
                 na.action = na.omit)
df_lda_pred = predict(df_lda_fit, df_norm_no0_test)
df_lda_class = df_lda_pred$class
df_table = table(df_lda_class, df_norm_no0_test$Natural.Gas.change)
df_lda_cm[[length(df_lda_cm)+1]] = df_table
df_lda_cm_acc[[length(df_lda_cm_acc)+1]] = sum(diag(df_table)/sum(df_table))


df_lda_cm
df_lda_cm_acc