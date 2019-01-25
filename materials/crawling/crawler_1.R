install.packages("httr")
install.packages('rvest')

library(rvest)
library(httr)

oneProduct <- "http://www.amorepacificmall.com/aprenew/shop/prod/shop_prod_product_review_ajax.do"

query <- list(i_sProductcd="SPR20180907000040878",
             i_sTypecd="0004",
             i_iNowPageNo="1",
             i_iGrade="",
             i_sFlagSort="")

res <- POST(oneProduct, body = query)
result <- content(res, "text")

reviews <- html_nodes(read_html(result), 'dd') %>% html_text()
reviews

aaaa <- matrix(reviews, nrow=4) 
tt <- aaaa[4, ]
tt[1]