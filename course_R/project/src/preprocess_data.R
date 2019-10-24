library("signal")
library("readr")
library("zoo")
library("xts")

#' Retrieve data from the file passed as input. NA are given
#' an approximate value using na.approx from the zoo library.
#'
#' @param fpath A string containg the full path to file.
#' @return A list containg the data.
get_data = function(fpath){
    data = read_csv(fpath, col_names = c('date', 'y'), skip=1,
                    col_types = cols(.default = "d", date = "D"))
    data$date = as.Date(data$date)
    return(data[nrow(data):1,])
}

clean_NA = function(data){
    data = data[complete.cases(data[ ,1:2]),]
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
    difference = data$y - data$y_smoothed
    simple_std = sqrt(mean(difference**2))
    cond = difference <= 5*simple_std
    return(data[cond,])
}

#' Make as new dataframe where the median value of the IR (y)
#' is stored for chunks of 25d. The stored date is the last (most
#' recent) one.
#'
#' @param data A dataframe with a date and y columns.
#' @return a reduced dataframe. 
compute_25d_chunks = function(data){
    out = list(date=c(), y=c())
    chunk = 25
    n = nrow(data)
    r = rep(1:ceiling(n/chunk),each=chunk)[1:n]
    d = split(data,r)
    for (i in d){
        out$date = c(out$date, tail(i$date, 1))
        out$y = c(out$y, mean(i$y))
    }
    out$date = as.Date(out$date, format="%Y-%m-%d")
    return(out)
}

#' make dataframe an xts (time-series) object. Note that
#' xts will convert all columns to character. To prevent this,
#' first create the time series object, then merge y column.
#'
#' @param data A dataframe with a time column.
#' @return an xts object. 
make_xts_object = function(data){
    aux = xts(data$date, order.by=data$date)
    data = merge(aux, data$y)
    data = data[, 2, drop = FALSE]
    colnames(data) = c('y')
    return(data)
}

#' Trim input dictionary to accept only values in the input time range.
#'
#' @param data An xts object.
#' @param time_period A string containg a time range. e.g. '1986/1986-02'.
#' @return a reduced dataframe. 
trim_date_range = function(data, time_period){
    return(data[time_period])        
}

#' Compute increments in values.
#'
#' @param data An xts object.
#' @return an xts object with additional columns for time increments. 
compute_increment = function(data){
    return(diff(data,lag=1,differences=1))
}

#' Master function to call data processing functions above.
#'
#' @param fpath A string containg the full path to file.
#' @param time_period A string containg a time range. e.g. '1986/1986-02'.
#' @return a post-processed list. 
run_preprocessing = function(fpath, time_period){
    M = get_data(fpath)
    M = clean_NA(M)
    M$y_smoothed = data_smoother(M$y)
    M = remove_spikes(M)
    
    
    M_1 = M
    M_1 = make_xts_object(M_1)
    M_1 = trim_date_range(M_1, time_period)
    M_1$y_increm = compute_increment(M_1)
    
    
    M_25 = compute_25d_chunks(M)
    M_25 = make_xts_object(M_25)
    M_25 = trim_date_range(M_25, time_period)
    M_25$y_increm = compute_increment(M_25)
    return(list('d1'=M_1, 'd25'=M_25))
}



#https://www.datacamp.com/community/blog/r-xts-cheat-sheet
