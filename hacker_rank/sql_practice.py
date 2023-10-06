
# select customer_id form order
# group by customer_id
# order by count(customer_id) desc, customer_id limit 1;

# select id,first,last from customer
# where LENGTH(first) + LENGTH(last) <12
# order by LENGTH(first) + LENGTH(last) desc, first, last,id;

# SELECT customer_id, CONCAT(TRIM(FIRST_NAME), “ “, TRIM(LAST_NAME)) AS full_name
#  , LENGTH(CONCAT(TRIM(FIRST_NAME), TRIM(LAST_NAME))) AS length_name
# FROM customer
# WHERE LENGTH(CONCAT(TRIM(FIRST_NAME), TRIM(LAST_NAME)))  < 12 ,
# ORDER BY  LENGTH(CONCAT(TRIM(FIRST_NAME), TRIM(LAST_NAME)))  ASC,
#       CONCAT(UPPER(TRIM(FIRST_NAME)), “ “, UPPER(TRIM(LAST_NAME))) ASC,
#       CUSTOMER.ID ASC;

# SELECT DISTINCT prof.name AS "PROFESSOR.NAME", cou.name AS "COURSE.NAME"
# FROM professor prof
# INNER JOIN schedule sch
# ON sch.professor_id = prof.id
# INNER JOIN course cou
# ON sch.course_id = cou.id
# WHERE cou.department_id <> prof.department_id;

# select name from students s
# inner join friends f
# on s.id=f.id
# inner join packages p_p
# on p_p.id=s.id
# inner join packages p_f
# on p_f.id = f.fried_id
# where 1=1 and p_p.salaray< p_f.salary
# order by p_f.salary



# SELECT X, Y FROM FUNCTIONS F1
#     WHERE EXISTS(SELECT * FROM FUNCTIONS F2 WHERE F2.Y = F1.X
#     AND F2.X = F1.Y AND F2.X > F1.X) AND (X != Y)
# UNION
# SELECT X,Y FROM FUNCTIONS F1 WHERE X = Y AND
#     ((SELECT COUNT(*) FROM FUNCTIONS WHERE X = F1.X AND Y = F1.X) > 1)
#       ORDER BY X;


# select n, if(p is null,'root',if(n in (select p from bst),'inner','leaf'))
# from bst;
# SELECT N,
# CASE
# WHEN P is NULL THEN 'Root'
# WHEN N in (SELECT P FROM BST) THEN 'Inner'
# ELSE 'Leaf'
# END
# FROM BST
# ORDER by N;