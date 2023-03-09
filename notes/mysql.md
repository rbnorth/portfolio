# MYSQL
todo: clean up notes


## contents

### base commands
        mysql -h localhost -u root -p
        \s
        show master status
        show slave status
        show processlist
        show full processlist
        set pager less
        set pager


mysql notes:

rebuild table:
        
        mysqldump db_name t1 > dump.sql
        mysql db_name < dump.sql

rebuild schema:
       
        mysqldump db_name > dump.sql
        mysql db_name < dump.sql

rebuild all schemas:

        mysqldump --all-databases > dump.sql
        mysql < dump.sql

rebuild tables with null alter:

        ALTER TABLE t1 ENGINE = InnoDB

checking table:

        show create table
        check table

myisam, archive, cvs repair:

        REPAIR TABLE t1

        mysqlcheck --repair --databases

        copying schemas between instances:

        mysqldump --help

        mysqladmin -h 'other_hostname' create db_name
        mysqldump db_name | mysql -h 'other_hostname' db_name

        mysqladmin create db_name
        mysqldump -h 'other_hostname' --compress db_name | mysql db_name

        mysqldump --quick db_name | gzip > db_name.gz

        mysqladmin create db_name
        gunzip < db_name.gz | mysql db_name


SELECT:

        SELECT * FROM pet WHERE name = 'Bowser'

        SELECT * FROM pet WHERE birth >= '1998-1-1'

        SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'

        SELECT * FROM pet WHERE species = 'snake' OR species = 'bird'

        SELECT * FROM pet WHERE (species = 'cat' AND sex = 'm') OR (species = 'dog' AND sex = 'f')

        SELECT name, birth FROM pet

        SELECT owner FROM pet

        SELECT DISTINCT owner FROM pet

        SELECT name, birth FROM pet ORDER BY birth

        SELECT name, birth FROM pet ORDER BY birth DESC

        SELECT name, species, birth FROM pet ORDER BY species, birth DESC

        SELECT name, birth, CURDATE(), TIMESTAMPDIFF(YEAR,birth,CURDATE()) AS age FROM pet

        SELECT name, birth, CURDATE(), TIMESTAMPDIFF(YEAR,birth,CURDATE()) AS age FROM pet ORDER BY age

        SELECT * FROM pet WHERE name LIKE '%w%'
        
        SELECT * FROM pet WHERE name LIKE '_____'

starts with:

        SELECT * FROM pet WHERE name REGEXP '^b'

ends with:

        SELECT * FROM pet WHERE name REGEXP 'fy$'

        SELECT * FROM pet WHERE name REGEXP '^.....$'
        SELECT * FROM pet WHERE name REGEXP '^.{5}$'

        SELECT COUNT(*) FROM pet

        SELECT owner, COUNT(*) FROM pet GROUP BY owner

### more than one table:

        SELECT pet.name, TIMESTAMPDIFF(YEAR,birth,date) AS age, remark FROM pet INNER JOIN event ON pet.name = event.name WHERE event.type = 'litter'

### The query uses an ON clause to match up records in the two tables based on the name values.

### An INNER JOIN permits rows from either table to appear in the result if and only if both tables meet the conditions specified in the ON clause.

### more information about tables:

        describe table

        show create table \G

batch mode:

        mysql < batch-file
        mysql < batch-file > mysql.out

programs:

        mysql
        mysqladmin
        mysqldump
        mysqlpump
        mysqlslap
        mysqlshow
        mysqlbinlog
        my_print_defaults 
        resolve_stack_dump
        perror

my.cnf:
        read_buffer
        sort_buffer
        read_rnd_buffer
        innodb_buffer



        SHOW VARIABLES
        SHOW STATUS

        CREATE USER 'root'@'127.0.0.1' IDENTIFIED BY 'root-password';
        CREATE USER 'root'@'::1' IDENTIFIED BY 'root-password';

grant tables:

user: User accounts, global privileges, and other non-privilege columns.

db: Database-level privileges.

tables_priv: Table-level privileges.

columns_priv: Column-level privileges.

procs_priv: Stored procedure and function privileges.

proxies_priv: Proxy-user privileges.

Object Information System Tables:
        event
        func
        plugin
        proc

log system tables:
        general_lg
        slow_log

        time zone:
        time_zone
        time_zone_leap_second
        time_zone_name
        time_zone_transition, time_zone_transition_type

replication system tables:
        gtid_executed
        ndb_binlog_index
        slave_master_info, slave_relay_log_info, slave_worker_info

optimizer system tables:

        innodb_index_stats, innodb_table_stats

mysql architecture using pluggable storage engines:

        connection start
        command start
                query strart
                        query-parse-start
                        query-parse-done
                        query-cache(miss,hit)
                        query-exec-start
                        |
                        |
                        query-exec-done
                query-done
                command done
        connection done

PROCEDURE ANALYSE(10, 2000);

        \s
        status

The table_open_cache and max_connections system variables affect the maximum number of files the server keeps open.

table_open_cache is related to max_connections

If table_open_cache is set too high, MySQL may run out of file descriptors and refuse connections, fail to perform queries, and be very unreliable

SHOW GLOBAL STATUS LIKE 'opened_tables'

FLUSH TABLES

### Optimizing Storage Layout for InnoDB Tables

OPTIMIZE TABLE

In InnoDB, having a long PRIMARY KEY (either a single column with a lengthy value, or several columns that form a long composite value) wastes a lot of disk space

Use the VARCHAR data type instead of CHAR to store variable-length

For tables that are big, or contain lots of repetitive text or numeric data, consider using COMPRESSED row format. 


### Optimizing InnoDB Disk I/O

typically recommended that innodb_buffer_pool_size is configured to 50 to 75 percent of system memory


Other InnoDB configuration options to consider when tuning I/O-bound workloads include innodb_adaptive_flushing, innodb_change_buffer_max_size, innodb_change_buffering, innodb_flush_neighbors, innodb_log_buffer_size, innodb_log_file_size, innodb_lru_scan_depth, innodb_max_dirty_pages_pct, innodb_max_purge_lag, innodb_open_files, innodb_page_size, innodb_random_read_ahead, innodb_read_ahead_threshold, innodb_read_io_threads, innodb_rollback_segments, innodb_write_io_threads, and sync_binlog


 Optimizing MyISAM Queries

## Optimizing Queries with EXPLAIN

# Permitted explainable statements for EXPLAIN are SELECT, DELETE, INSERT, REPLACE, and UPDATE

        {EXPLAIN | DESCRIBE | DESC}

        EXPLAIN 
        EXPLAIN EXTENDED
        EXPLAIN PARTITIONS

        explain format=json select * from event

        SELECT CONNECTION_ID()
        EXPLAIN FOR CONNECTION 373
        optimizer_prune_level
        optimizer_search_depth

        SELECT @@optimizer_switch\G

