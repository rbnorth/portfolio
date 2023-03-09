## <ins>DynamoDB</ins>

### Managing Settings on DynamoDB Provisioned Capacity Tables

[DynamoDB Provisioned throughput](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html#ProvisionedThroughput.CapacityUnits.Read)

### Provisioned Capacity

**Read Capacity Units (RCU)**

*Example 1:*

10 strongly consistent reads per second of 4KB each

```
10*4KB/4KB = 10 RCU
```

*Example 2:*

10 strongly consistent reads per second of 11KB each

```
10*12KB/4KB = 30 RCU
```

*Example 3:*

20 eventually consistent reads per second of 12KB each

(you get twice as many RCU's with eventually consistent)

```
(20/2)*(12/4) = 30 RCU
```

*Example 4:*

36 eventually consistent reads per second of 16KB each

```
(36/2)*(16/4) = 72 RCU
```

**Write Capacity Units (WCU)**

*Example 1:* 

10 standard writes per second of 4KB each

```
10*4KB = 40 WCU
```

*Example 2:* 

12 standard writes per second of 9.5KB each

```
12*10KB = 120 WCU
```

*Example 3:*

10 transactional writes per second of 4KB each

```
10*2*4 = 80 WCU
```

*Example 4:*

12 transactional writes per second of 9.5KB each

```
12*2*10 = 240 WCU
```
### DynamoDB CLI Commands

### Import data
```
aws --profile dynamodb batch-write-item --request-items file://mystore.json
```
### SCAN API

##### Perform scan of ProductOrders table:
```
aws --profile dynamodb scan --table-name mystore
```
#### Use Page-Size Parameter:
```
aws --profile dynamodb scan --table-name mystore --page-size 1

aws --profile dynamodb scan --table-name mystore --page-size 2
````
#### Use Max-Items Parameter:
```
aws --profile dynamodb scan --table-name mystore --max-items 1
```
#### Use Projection-Expression Parameter:
```
aws --profile dynamodb scan --table-name mystore --projection-expression "created"

aws --profile dynamodb scan --table-name mystore --projection-expression "category"

aws --profile dynamodb scan --table-name mystore --projection-expression "colour"
```
#### Use Filter-Expression Parameter:
```
aws --profile dynamodb scan --table-name mystore --filter-expression "clientid = :username" --expression-attribute-values '{ ":username": { "S": "chris@example.com" }}'

aws --profile dynamodb scan --table-name mystore --filter-expression "size = :n" --expression-attribute-values '{ ":n": { "N": "12" }}'

aws --profile dynamodb scan --table-name mystore --filter-expression "size > :n" --expression-attribute-values '{ ":n": { "N": "12" }}'
```

### QUERY API

#### Use Key-Conditions Parameter:
```
aws --profile dynamodb query  --table-name mystore --key-conditions '{ "clientid":{ "ComparisonOperator":"EQ", "AttributeValueList": [ {"S": "chris@example.com"} ] } }'
```

#### Use Key-Condition-Expression Parameter:
```
aws --profile dynamodb query --table-name mystore --key-condition-expression "clientid = :name" --expression-attribute-values '{":name":{"S":"chris@example.com"}}'
```


