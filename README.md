# mdm_app_deployment
This project showcases an example structure of an Ansible playbook that can add MDM devices to an IRM (Infrastructure Resource Modeling) application or deploy applications to those devices via APIs.

Requirements
------------

⚠️ Make sure when you pass store_id variable the store ID letter is uppercase

Role Variables
--------------

#### POS-ADHOC 
( Adds pos's to IRM on an adhoc basis. To be used in an AWX job that is tied to a user-submitted form)

To run the task use this cmd as an example: ```ansible-playbook tests/test.yml -t pos_adhoc -e '{"store_id":"ABC123", "pos_numbers": ["01", "02"], "ip_address":"10.xx.xx.2"}'"```

```pos_number``` would be what it is in mdm, for example POS_XXXXXX_03 the pos_number would be '03'

#### KDS-ADHOC 
( Adds kds's to IRM on an adhoc basis. To be used in an AWX job that is tied to a user-submitted form)

 to run the task use ```ansible-playbook tests/test.yml -t kds_adhoc -e '{"store_id":"ABC123", "kds_letters": ["A", "B"], "ip_address":"10.xx.xx.2"}'"```

```kds_letter``` would be what it is in mdm, for example KDS_XXXXXX_A the kds_letter would be 'A'

#### Deploy 

pos_wave options:

pos-wave-1
pos-wave-2
pos-wave-3
pos-wave-4


```ansible-playbook tests/test.yml -t deploy -e "pos_wave=waveName pos_app_name='pos app name'"```


Example Playbook
----------------

Example on how to run a specific task in this role using a tag. Tags of each task can be found in the ```main.yml``` file

```ansible-playbook tests/test.yml -t kds_adhoc -e "store_id='ABC123' kds_letter='A' ip_address='8.8.8.8'"```


Author Information
------------------

Adam Winders
