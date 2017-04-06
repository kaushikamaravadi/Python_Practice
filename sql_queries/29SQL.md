## 03/29/17

#### Write a query which returns Name, FatherName, DOB of employees whose PresentBasic is 
1. Greater than 30000.
1. Less than 3000.
1. Between 3000 and 5000

```sql
select name,FatherName, DOB from tblemployees where presentbasic between 3000 and 5000;
```
```sql
select name,FatherName, DOB from tblemployees where presentbasic > 3000;
```
```sql
select name,FatherName, DOB from tblemployees where presentbasic < 3000;
```

#### Write a query which returns All the details of employees whose Name 
1. Ends with 'KHAN'
2. Starts with 'CHANDRA'
3. Is 'RAMESH' and their initial will be in the range of alphabets a-t. Ex: If an employee name is T.Ramesh, then your query should return his record. If an employee name is W Ramesh, then your query shouldn’t return his record.

```sql
select * from tblemployees where name like '%khan';
```
```sql
select * from tblemployees where name like 'chandra%';
```
```sql
select name from tblemployees where name regexp '^[A-T].RAMESH';
``` 

#### Select all the centers where max Length of the employee name is twice the min length of the employee name

```sql
select name from tblemployees where char_length(name)=2*(select min(char_length(name)) from tblemployees);
```

#### Write a query to find out all the departments where no employee has the Present Basic rounded of to 100

```sql
select distinct(departmentcode),presentbasic from tblemployees where mod
(presentbasic,100)=0;
```

#### Write a query to find out all the departments where all employee have their Present Basic rounded of to 100

```sql
select distinct(departmentcode),presentbasic from tblemployees where mod(presentbasic,100)!=0;
```
