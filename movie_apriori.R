install.packages(c("arules", "arulesViz", "visNetwork", "igraph" ))

library(arules) ## 연관관계 분석을 위한 aprior() 를 쓰기 위함
library(arulesViz) ## 시각화에 필요
library(visNetwork) ## 시각화 중 네트워크 표현에 필요
library(igraph) ## 시각화 결과물을 인터렉티브(움직이게) 해줌

## 파일 로드
title = "신과함께-죄와벌"
support = 0.005
confidence = 0.6
sortorder = "lift"

par(mfrow=c(1, 1))
######################################
# movie <- read.csv(paste0("C:/Users/student/Desktop/Final_proj/csv/", title, "_ap_nosw.csv") , header = T, fileEncoding="UTF-8")
# movie.list<-split(movie$word, movie$num)
# movie.transaction<-as(movie.list, "transactions")
# movie.transaction
# # 모델링
# rules1 <- apriori(movie.transaction, parameter = list(supp = support, conf = confidence, target = "rules"))
# summary(rules1)
# # 결과 출력
# inspect(sort(rules1))
# 
# ## 시각화
# subrules1 <- head(sort(rules1, by=sortorder), 20) ## lift 기준으로 상위 20개만을 시각화
# ig1 <- plot( subrules1, method="graph", control=list(type="items") )
# 
# ######################################
# movie <- read.csv(paste0("C:/Users/student/Desktop/Final_proj/csv/", title, "_ap_jwsw.csv"), header = T, fileEncoding="UTF-8")
# movie.list<-split(movie$word, movie$num)
# movie.transaction<-as(movie.list, "transactions")
# movie.transaction
# # 모델링
# rules2 <- apriori(movie.transaction, parameter = list(supp = support, conf = confidence, target = "rules"))
# summary(rules2)
# # 결과 출력
# inspect(sort(rules2))
# 
# ## 시각화
# subrules2 <- head(sort(rules2, by=sortorder), 20) ## lift 기준으로 상위 20개만을 시각화
# ig2 <- plot( subrules2, method="graph", control=list(type="items") )
# 
# ######################################
# movie <- read.csv(paste0("C:/Users/student/Desktop/Final_proj/csv/", title, "_ap_swsw.csv"), header = T, fileEncoding="UTF-8")
# movie.list<-split(movie$word, movie$num)
# movie.transaction<-as(movie.list, "transactions")
# movie.transaction
# # 모델링
# rules3 <- apriori(movie.transaction, parameter = list(supp = support, conf = confidence, target = "rules"))
# summary(rules3)
# # 결과 출력
# inspect(sort(rules3))
# 
# ## 시각화
# subrules3 <- head(sort(rules3, by=sortorder), 20) ## lift 기준으로 상위 20개만을 시각화
# ig3 <- plot( subrules3, method="graph", control=list(type="items") )

######################################
movie <- read.csv(paste0("C:/Users/student/Desktop/Final_proj/csv/", title, "_ap_jwswsw.csv"), header = T, fileEncoding="UTF-8")
movie.list<-split(movie$word, movie$num)
movie.transaction<-as(movie.list, "transactions")
movie.transaction
# 모델링
rules4 <- apriori(movie.transaction, parameter = list(supp = support, conf = confidence, target = "rules"))
summary(rules4)
# 결과 출력
inspect(sort(rules4))

## 시각화
subrules4 <- head(sort(rules4, by=sortorder), 20) ## lift 기준으로 상위 20개만을 시각화
inspect(subrules4)
ig4 <- plot( subrules4, method="graph", control=list(type="items") )


# saveAsGraph seems to render bad DOT for this case
tf <- tempfile( )
saveAsGraph( subrules4, file = tf, format = "dot" )

# clean up temp file if desired
#unlink(tf)

#########################################

# 인터렉티브 코드
ig_df <- get.data.frame( ig4, what = "both" )
visNetwork(
  nodes = data.frame(
    font.size = 30
    ,id = ig_df$vertices$name
    ,value = ig_df$vertices$support # could change to lift or confidence
    ,title = ifelse(ig_df$vertices$label == "",ig_df$vertices$name, ig_df$vertices$label)
    ,ig_df$vertices
  )
  , edges = ig_df$edges
) %>%
  visEdges(  ig_df$edges ) %>%
  visOptions( highlightNearest = T )

