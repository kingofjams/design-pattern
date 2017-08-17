from orderSubject import OrderSubject
from accountingObserver import AccountingObserver
from cashierObserver import CashierObserver
from dispatchingObserver import DispatchingObserver


subject_obj = OrderSubject()

print('客户下单!')

subject_obj.add_observer(AccountingObserver())
subject_obj.add_observer(CashierObserver())
subject_obj.add_observer(DispatchingObserver())


subject_obj.notify()
