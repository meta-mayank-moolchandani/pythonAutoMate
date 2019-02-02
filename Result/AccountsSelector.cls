public class AccountsSelector extends fflib_SObjectSelector {

  public List<Schema.SObjectField> getSObjectFieldList(){
		return (new List<Schema.SObjectField>{
			Account.Id 
		});
	}

	public Schema.SObjectType getSObjectType(){
		return Account.sObjectType;
	}

  public List<Account> getById(Set<ID> idSet){
		return (List<Account>)selectSObjectsById(idSet);
	}
}