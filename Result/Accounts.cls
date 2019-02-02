public class Accounts extends fflib_SObjectDomain {

    public Accounts(List<Account> sObjectList) {
        super(sObjectList);
    }

    public class Constructor implements fflib_SObjectDomain.IConstructable {
        public fflib_SObjectDomain construct(List<SObject> sObjectList) {
            return new Accounts(sObjectList);
        }
    }
    
    public override void onBeforeInsert(){
    }

    public override void onAfterInsert() {
    }

    public override void onBeforeUpdate(Map<Id,sObject> existingRecords){
    }

    public override void onAfterUpdate(Map<Id,SObject> existingRecords) {
    }

}