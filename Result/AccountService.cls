
public class AccountService implements IAccountService{
	
	List<Account> getByAccountId(Set<Id> idSet){
		return AccountServiceImpl.getInstanceOf().getById(idSet);
	}
    
}