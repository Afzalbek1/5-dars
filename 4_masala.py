
from database import query_sql


query_sql("""
    create table if not exists teacher(
        id serial primary key,
        name varchar(50) not null,
        phone varchar(50),
        subject varchar(50) not null,
        is_active bool default true
            
)

""")

query_sql("""
    create table if not exists student(
        id serial primary key,
        name varchar(50) not null,
        phone varchar(50) not null unique,
        course int default 1,
        univer varchar(100) not null,
        teacher_id int references teacher(id))

    """)

name = input("name : ")
phone=input("phone : ")
subject=input("subject : ")

query_sql("""

insert into teacher (name, phone, subject) values(%s,%s,%s)

""",(name,phone,subject))



query_sql("select s.name, s.phone, t.name, t.subject from student s join teacher t on s.teacher_id = t.id",fetchall=True)

