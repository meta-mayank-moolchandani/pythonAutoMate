public class AccountServiceImpl implements IAccountService{
	
	public AccountsSelector accountSelectorObject = new AccountsSelector();
    
    public static AccountServiceImpl accountServiceObject= new AccountServiceImpl();
    
    public static AccountServiceImpl getInstanceOf(){
    	return accountServiceObject;
    }
    
    public List<Account> getById(Set<Id> idSet){
    	return accountSelectorObject.getById(idSet);
    }
}
