from MyCoolFuncs import funcA, funcC
from matplotlib.pyplot import (plot, show,
                               title,
                               xlabel,
                               ylabel,
                               xticks,
                               yticks,
                               )

funcA()
funcC()

plot([1,2,3,5,3,-4])
title("grafico xpto")
xlabel("Xpto")
ylabel("Eixo do Y")
xticks([0,1,2,3,4,5])
yticks([0,1,2,3,4,5])
show()