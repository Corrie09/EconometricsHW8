* Load the data    <-- make sure you're directory is set at the place where youre data is
use "assignment8.dta", clear  

*first some data exploration: 
*describe 

*tab time
*tab state
*codebook store

*summarize wage_st, detail
*tabstat wage_st, by(state) statistics(mean min max n)
*count if missing(wage_st)


*actual graphs:

*February 1992 graph
twoway (histogram wage_st if state==1 & time==0, ///
            width(0.10) start(4.25) percent ///
            fcolor(navy%60) lcolor(navy) lwidth(thin)) ///
       (histogram wage_st if state==0 & time==0, ///
            width(0.10) start(4.25) percent ///
            fcolor(green%60) lcolor(dkgreen) lwidth(thin)), ///
    xlabel(4.25(0.10)5.75, labsize(small)) ///
    ylabel(0(10)40, labsize(small)) ///
    title("February 1992", size(medium)) ///
    xtitle("Wage Range", size(small)) ///
    ytitle("Percent of Stores", size(small)) ///
    legend(label(1 "New Jersey") label(2 "Pennsylvania") ///
           size(small) position(1) ring(0)) ///
    name(feb1992, replace)

*November 1992 graph
twoway (histogram wage_st if state==1 & time==1, ///
            width(0.10) start(4.25) percent ///
            fcolor(navy%60) lcolor(navy) lwidth(thin)) ///
       (histogram wage_st if state==0 & time==1, ///
            width(0.10) start(4.25) percent ///
            fcolor(green%60) lcolor(dkgreen) lwidth(thin)), ///
    xlabel(4.25(0.10)5.75, labsize(small)) ///
    ylabel(0(10)90, labsize(small)) ///
    title("November 1992", size(medium)) ///
    xtitle("Wage Range", size(small)) ///
    ytitle("Percent of Stores", size(small)) ///
    legend(label(1 "New Jersey") label(2 "Pennsylvania") ///
           size(small) position(1) ring(0)) ///
    name(nov1992, replace)

* To combine the two graphs side by side
*graph combine feb1992 nov1992, ///
    cols(2) ///
    title("Distribution of Starting Wage Rates") ///
    note("Source: Card and Krueger (1994) replication", size(vsmall))
	
* Export individual graphs
*graph export "figure1_feb1992.png", as(png) name(feb1992) replace width(2400)
*graph export "figure1_nov1992.png", as(png) name(nov1992) replace width(2400)
	




	
	
	
	
	
	
	
	