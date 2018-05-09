# Spring Session DynamoDB
An implementation of Spring Session extension based on AWS DynamoDB as a Session Repository


# Disclaimer
This work still under development and should be used for experimentation purposes only. **Please 
use on your own responsibility**.

# Configuration
```
@Configuration
@EnableDynamoDBHttpSession
@EnableConfigurationProperties(DynamoDBSpringSessionConfiguration.class)
public class SessionConfig {

  @Bean
  public DynamoDB dynamoDB() {
    return new DynamoDB(AmazonDynamoDBClientBuilder.standard().withRegion(Regions.EU_WEST_1).build());
  }
}
```

Override defaults in your properties with:
```
spring.session.dynamodb.tableName
spring.session.dynamodb.maxInactiveIntervalInSeconds
```

# Misc
- Docker compose config can be found in /docker
- Example DynamoDB table CloudFormation configuration can be found in /cloudformation
  
  Then configure e.g.:  
  ```
     @Bean
      @Profile("local")
      public DynamoDB localDynamoDB() {
        AwsClientBuilder.EndpointConfiguration endpointConfiguration = new AwsClientBuilder.EndpointConfiguration("http://localhost:7777", "eu-west-1");
        return new DynamoDB(AmazonDynamoDBClientBuilder.standard()
                                                       .withEndpointConfiguration(endpointConfiguration)
                                                       .build());
      }
    ```

