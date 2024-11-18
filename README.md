# YNAB_MonthEnd
Utilities to handle month-end activities on a YNAB budget

* Define month end
  * default: 1st of the month, accounts are all transacting in the current month
* Confirm month end activities IS RUNNABLE
  * default: 
* Retrieve month end activities
  * Need some sort of way to define actions 
  * example:
    * [FETCH] transactions from [PAYEE]
    * [ACTION] Compute X%
    * [MOVE] $N to [CATEGORY]
* Execute month end activities
  * DRY-RUN