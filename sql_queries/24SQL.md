## 03/24/17

#### Write a query to display the currentdate in all possible formats

```sql
Yet to come
```

#### Write a Query to List out all employees where the present basic is perfectly rounded of to 100. 
#### Ex: If Basic of A is 2011, Basic of B is 2100 , Basic of C is 2101 and Basic of D is 2200 . Then Only B and D should be displayed

```sql
select grosspay from tblpayemployees  where mod(grosspay,100)=0;
```

#### Write a query to find out employees whose names have Leading or Trailing spaces
```sql
select name from tblemployees where substr(name,1,1) = ' ' or substr(name,-1,1) = ' ';
```
```sql
select name from tblemployees where LEFT(name,1) = ' ' or RIGHT(name,1) = ' ';
```

#### Write a update query to remove trailing spaces from the employee names. Ex: If the employee 
name is Naseeruddin Shah    , then after running the update query the name should be Naseeruddin Shah.(without any spaces at the end)
```sql
update tblemployees set name=RTRIM(name)
```

#### Write a similar update query to remove the leading spaces from the employee names
```sql
update tblemployees set name=LTRIM(name)
```

#### Write a query to find list of employees and payments where the employee is paid VDA but not PF

```sql
select  distinct(t1.EmployeeNumber),t1.ParamCode from tblpayemployeeparamdetails as t1 left join tblpayemployeeparamdetails as t2 on
t1.EmployeeNumber=t2.EmployeeNumber and t2.ParamCode='pf' where t1.ParamCode='vda' and t2.EmployeeNumber is null;
```
