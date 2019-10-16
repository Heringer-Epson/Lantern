#Source:
#https://support.rstudio.com/hc/en-us/articles/218221837-Profiling-with-RStudio

#The fellowing packages may need to be installed if they have not already
#been downloaded.
#install.packages('profvis')
#install.packages('ggplot2')

#Call the profvis library.
library(profvis)

#Example 1: Simple test case.
profvis({
  data(diamonds, package = "ggplot2")
  
  plot(price ~ carat, data = diamonds)
  m <- lm(price ~ carat, data = diamonds)
  abline(m, col = "red")
})

#Example 2: Profiling individuals functions requires calling profvis
#with the function.
plotter = function() profvis({
  data(diamonds, package = "ggplot2")
  plot(price ~ carat, data = diamonds)
  m <- lm(price ~ carat, data = diamonds)
  abline(m, col = "red")  
})
plotter()

#Example 3: Calling profvis outside the function will only give the
#cumulative time taken by that function.
plotter = function() {
  data(diamonds, package = "ggplot2")
  plot(price ~ carat, data = diamonds)
  m <- lm(price ~ carat, data = diamonds)
  abline(m, col = "red")  
}
profvis({plotter()})