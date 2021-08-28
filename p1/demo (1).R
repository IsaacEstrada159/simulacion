dim = 3
dur = 20
pos = rep(0, dim)

for  (t in 1:dur) {
    cual = sample(1:dim, 1)
    if (runif(1) < 0.5) {
        pos[cual] = pos[cual] + 1
    } else {
        pos[cual] = pos[cual] - 1
    }
    
   
}
print(pos)
