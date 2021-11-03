library(ggplot2)
library(psych)

n <- 20
p <- data.frame(x = rnorm(n), y=rnorm(n), c=rnorm(n), m=rnorm(n))
xmax <- max(p$x)
xmin <- min(p$x)
p$x <- (p$x - xmin) / (xmax - xmin) 
ymax <- max(p$y)
ymin <- min(p$y)
p$y <- (p$y - ymin) / (ymax - ymin)  
cmax <- max(p$c)
cmin <- min(p$c)
p$c <- 2 * (p$c - cmin) / (cmax - cmin) - 1 

mmax=max(p$m)
mmin=min(p$m)
p$m=(p$m-mmin)/(mmax-mmin)+1 

p$g <- round(5 * p$c) 
paso <- floor(256 / 10)
niveles <- seq(0, 255, paso)
colores <- rgb(niveles, rep(0, 11), rev(niveles), max=255)
eps <- 0.001
fuerza <- function(i) {
  xi <- p[i,]$x
  yi <- p[i,]$y
  ci <- p[i,]$c
  mi=p[i,]$m * 800 
  fx <- 0
  fy <- 0
  for (j in 1:n) {
    cj <- p[j,]$c
    dir <- (-1)^(1 + 1 * (ci * cj < 0))
    dx <- xi - p[j,]$x
    dy <- yi - p[j,]$y
    factor <- dir * abs(ci - cj) / (sqrt(dx^2 + dy^2) + eps)
    fx <- fx - dx * factor
    fy <- fy - dy * factor
  }
  return(c(fx, fy)/(mi*200)) 
}
suppressMessages(library(doParallel))
registerDoParallel(makeCluster(detectCores() - 1))
system("rm -f p9_t*.png") 
tmax <- 100
digitos <- floor(log(tmax, 10)) + 1
tl <- "0"
while (nchar(tl) < digitos) {
  tl <- paste("0", tl, sep="")
}

p$vel=numeric(n)
for (iter in 1:tmax) {
  f <- foreach(i = 1:n, .combine=c) %dopar% fuerza(i)
  delta <- 0.02 / max(abs(f)) # que nadie desplace una paso muy largo
  p$x <- foreach(i = 1:n, .combine=c) %dopar% max(min(p[i,]$x + delta * f[c(TRUE, FALSE)][i], 1), 0)
  p$y <- foreach(i = 1:n, .combine=c) %dopar% max(min(p[i,]$y + delta * f[c(FALSE, TRUE)][i], 1), 0)
  v=foreach(i=1:n,.combine=c)%dopar% sqrt((delta * f[c(TRUE, FALSE)][i])^2 + (delta * f[c(FALSE, TRUE)][i])^2)
  p$vel=p$vel+v
  
  tl <- paste(iter, "", sep="")
  while (nchar(tl) < digitos) {
    tl <- paste("0", tl, sep="")
  }
  png(paste("p9_t", tl, ".png", sep=""))
  print( ggplot(data=p, aes(x=x ,y=y, size=m * 50, col=colores[g+8]) )+geom_point(show.legend =  TRUE)+xlim(c(0,1))+ylim(c(0,1))+  
           ggtitle(paste("Paso ", iter))  +scale_colour_manual(values=colores)  )+
    scale_shape_discrete(name  ="Payer")+ 
    scale_colour_discrete(name  ="Payer", labels=seq(-5,5 ))
  graphics.off()

  png(paste("p9_mat", tl, ".png", sep=""))
  pairs.panels(p[,c(1:4,6)], 
               main=paste("Paso ", tl, sep=""),
               method = "pearson", 
               hist.col = "purple",
               density = TRUE,  
               ellipses = FALSE,
               stars=TRUE,
               labels=c("Posición en x","Posición en y","Carga","Masa","Velocidad"))
  graphics.off()
}
stopImplicitCluster()

