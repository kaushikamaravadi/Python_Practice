## 03/22/17

#### Write a query to Get a List of Employee who have a one part name.
 
```sql
select first_name  from NameSplit where middle_name is NULL and  last_name is NULL or middle_name='' and  last_name='' order by first_name;
```

#### Write a query to Get a List of Employee who have a three part name.

```sql
select name from tblemployees where name regexp '^[^ ]+[ ]+[^ ]+[ ]+[^ ]+$';
```

#### Write a query to get a list of Employee who have a First Middle Or last name as Ram, and not any thing else

```sql
create table NameSplit SELECT    SUBSTRING_INDEX(SUBSTRING_INDEX(Name, ' ', 1), ' ', -1) AS first_name,    If(  length(Name) - length(replace(Name, ' ','')e_name,    SUBSTRING_INDEX(SUBSTRING_INDEX(Name, ' ', 3), ' ', -1) AS last_name FROM tblemployees;

select * from NameSplit where first_name='Ram' or middle_name='ram' or last_name='ram';
```
#### Write a query which gives employee types in the organization.

```sql
select name , description from tblemployees as t, tblemployeetypes as s where t.employeetype = s.employeetype;
```

#### Write a Query to get all employees where reminder of employee number by 10 is a power of two

```sql
select name from tblemployees where mod(employeenumber,10)=1 or mod(employeenumber,10)=2 or mod(employeenumber,10)=4 or mod(employeenumber,10)=8;
```
