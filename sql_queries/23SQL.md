## 03/23/17

#### Write a query to find the all the names which contain the word or a part of a word Suresh, sort the result in the order of similarity.
Ex: Suresh, Sures, Sure, Sur, Su, S (Names containing the word Suresh, later names containing Sures and so on)

```sql
select first_name from NameSplit where first_name like '%suresh%' union select first_name from NameSplit where first_name like '%sures%' union select first_name from NameSplit where first_name like '%sure%' union select first_name from NameSplit where first_name like '%sur%' union select first_name from NameSplit where first_name like '%su%' union select first_name from NameSplit where first_name like '%s%';
```

#### Display all names from tblEmployees by appending it with INDIAN at the end if the name starts from A-M, for names starting from N-Z append AMERICAN at the end.
Ex: Shyam should display as ShyamAMERICAN and Abdul should display as AbdulINDIAN

```sql
select concat(name,'INDIAN') as append from tblemployees where name rlike '^[A-M]' UNION select concat(name,'AMERICAN') from tblemployees where name rlike '^[N-Z]';
```

#### Write a query to find the name(s) having the largest number of characters in it. (Hint: Use aggregate functions)

```sql
select name,length(name) from tblemployees where length(name)=(select max(char_length(name)) from tblemployees);
```

#### Write a query to list all the employees whose name starts and ends with same character.

```sql
select name from tblemployees where substring(name,1,1)=substring(name,-1,1); 
```

#### Write a query to list all employees whose first and second character in their names are similar.

```sql
select name from tblemployees where substring(name,1,1)=substring(name,2,1);
```

