#### Write a query to get the top 4 salaried employees

```sql
select grosspay from tblpayemployees order by grosspay DESC limit 4;
```
```sql
select * from (select @rank :=@rank+1 as rank, grosspay,employeenumber from tblpayemployees,(select @rank :=0) r order by grosspay desc) m where rank<5;( rank=3, rank between 8 and 15)
```

#### Write a query to get all the employees who are ranked between 8 and 15 based on the present --basic paid to them
```sql
select * from (select @rank :=@rank+1 as rank, grosspay,employeenumber from tblpayemployees,(select @rank :=0) r order by grosspay desc) m where rank between 8 and 15;

```sql
select @row_num := if(@prev_value=o.employeenumber,@row_num+1,1) as rownumber, o.employeenumber,o.name,@prev_value :=o.employeenumber from tblemployees o,(select @row_num :=1) x,(select @prev_value :='') y order by o.employeenumber limit 10;
```
```sql
select distinct(t.name), m.grosspay from tblemployees as t,tblpayemployees as m where t.employeenumber = m.employeenumber order by grosspay desc limit 1 offset 9;
```

#### Write a query to get the top 4 salaried employees
Use ROW_NUMBER function
Without using any pre-defined functions
```sql
select * from (select @rank :=@rank+1 as rank, grosspay,employeenumber from tblpayemployees,(select @rank :=0) r order by grosspay desc) m where rank<5;( rank=3, rank between 8 and 15)
```
















