library(lattice)
library(sp)
library(viridisLite)
library(reshape2)

datos<- data.frame()

g <- function(x,y) { # modificamos para que sea interesante
  return((10* cos(x^2) - 10 * x + 12 * cos(y^2) -5* y))
}
x <- seq(-1, 6, 0.4)
y <-  x
z <- outer(x, y, g)

low <- -1
high <- 6
j <- seq(0.25, 4, 0.25)
replicas <- 50 #puntitos

for (step in j) {

replica <- function(t) {
  curr <- c(runif(1, low, high), runif(1, low, high))
  best <- curr
  for (tiempo in 1:t) {
    
    delta <- runif(1, 0, step)
    
    left <- curr +c(-delta,0)
    
    right <- curr + c(delta,0)
    
    up <- curr + c(0,-delta)
    
    down <- curr + c(0,delta)
    
    puntos<- c(left,right,up,down)
    
    for(p in 1:8){
      if(puntos[p] < (-1)){
        puntos[p] <- puntos[p]+6 
      }
      if(puntos[p] > 6){
        puntos[p] <- puntos[p]-1
      }
    }
    
    ux<-c()
    uy<-c()
    
    for(q in 1:8){
      if(q %% 2 == 0){
        uy <- c(uy,puntos[q])
      }else{
        ux <- c(ux,puntos[q])
      }
    }
    
    ug<- c()
    
    for(r in 1:4){
      ug <- c(ug, g(ux[r], uy[r]) )
    }
    ppmax <- which.max(ug)
    curr <- c(ux[ppmax], uy[ppmax])
    if(g(curr[1],curr[2]) > g(best[1],best[2])){
    
      best <- curr
    }
  }
  return(best)
}

suppressMessages(library(doParallel))
registerDoParallel(makeCluster(detectCores() - 1))

for (pot in 1:40) { #numero de imagenes a repeticiones dadas
  tmax <- pot
  resultados <- foreach(i = 1:replicas, .combine=c) %dopar% replica(tmax)

  
ux<- c()
uy<- c()

sal<-(2*replicas)

for(q in 1:sal){
  if(q %% 2 == 0){
    uy <- c(uy,resultados[q])
  }else{
    ux <- c(ux,resultados[q])
  }
}


val <- c()
for(r in 1:replicas){
  val <- c(val, g(ux[r], uy[r]))
}
  
maximo <- which.max(val)
x <- seq(-1, 6, 0.4) 
y <-  x
z <- outer(x, y, g)

dimnames(z) <- list(x, y)
d <- melt(z)
names(d) <- c("x", "y", "z")


png(paste0("t7_", tmax, ".png", sep=""), width=500, height=500)
plot(levelplot(z ~ x * y, data = d))
trellis.focus("panel", 1, 1, highlight=FALSE)
lpoints(ux, uy, pch=1, col="red", cex=2)
trellis.unfocus()
trellis.focus("panel"[1], 1, 1, highlight=FALSE)
lpoints(ux[maximo], uy[maximo], pch=20, col="green",cex=3)
trellis.unfocus()

graphics.off()

}
ultimo<-min(val)
datos<- rbind(datos,c(step,ultimo))
}



stopImplicitCluster()