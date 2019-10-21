library("signal")
library("readr")
library("zoo")
library("xts")
options(dplyr.print_max = 30)

#' Retrieve data from the file passed as input. NA are given
#' an approximate value using na.approx from the zoo library.
#'
#' @param fpath A string containg the full path to file.
#' @return A list containg the data.
get_data = function(fpath){
    data = read_csv(fpath, col_names = c('date', 'y'), skip=1,
                    col_types = cols(.default = "d", date = "D"))
    data$date = as.Date(data$date)
    data$y = na.approx(data$y)
    return(data[1:30,])
    #return(data)
}

clean_NA = function(data){
    data = data[complete.cases(data[ ,1]),]
    return(data)
}

#' Smooth values in an array using the Savitzky–Golay filter.
#'
#' @param y An array of values.
#' @return The smoothed values of y.
data_smoother = function(y){
    return(sgolayfilt(y, p=3, n=9))
}

#' Replace spurious values in an array.
#'
#' @param y An array of values.
#' @return The smoothed values of y.
remove_spikes = function(data){
    diff = data$y - data$y_smoothed
    simple_std = sqrt(mean(diff**2))
    cond = diff <= 5*simple_std
    return(data[cond,])
}

#' make dataframe an xts (time-series) object.
#'
#' @param data A dataframe with a time column.
#' @return an xts object. 
make_xts_object = function(data){
    data = xts(data, order.by=data$date)
    data = data[, 2, drop = FALSE]
    return(data)
}

#' Compute increments in values.
#'
#' @param data An xts object.
#' @return an xts object with additional columns for time increments. 
compute_increment = function(data){
    print(data)
    print(lag(data, k = +1, na.pad = TRUE)) #laggin by index, not time.
    #print(diff(data,lag=1,differences=1))
    return(data)
}

#diff(xts5,lag=12,differences=1) 

#' Master function to call data processing functions above.
#'
#' @param fpath A string containg the full path to file.
#' @return a post-processed list. 
run_preprocessing = function(fpath){
    M = get_data(fpath)
    M = clean_NA(M)
    M$y_smoothed = data_smoother(M$y)
    M = remove_spikes(M)
    M = make_xts_object(M)
    M = compute_increment(M)
    return(M)
}




