## 1. Services for data science at AWS  

Data science in a wide understanding is defined as a multidisciplinary field which deals with technologies, processes, and systems to extract knowledge and information from data. Data science composition range between the aspects of managing and processing data to the methods and theories for analysis and optimization.

Amazon Web Services has great capability and a wide range of tools that can help data scientists in many aspects like building secure and scalable big data applications. Defining itself as the most complete platform for Big Data AWS offers flexible and low cost resources with easy scalability and well conected resources simplfying proccesses within its tools as well as a range of other big data tools compability. AWS provides everything you need to collect, store, process, analyze, and visualize big data on the cloud,  some of the avaliable tool are presented under its categories bellow.

#### Big data
- Amazon EMR
- Amazon Elasticsearch Service
- Amazon Athena
    
#### Real-time Big Data
- Amazon Kinesis Firehose
- Amazon Kinesis Streams
- Amazon Kinesis Analytics

#### Big Data Storage & Databases
- Amazon S3
- Amazon DynamoDB
- Amazon Aurora
- Amazon RDS

#### Data Warehouse
- Amazon Redshift

#### Business Intelligence
- Amazon QuickSight

#### Artificial Inteligence
- Amazon Lex
- Amazon Polly
- Amazon Rekognition
- Amazon Machine Learning

#### Internet of Things
- AWS IoT
- AWS Greengrass

For this research we are going to be going in dept on 2 of this tools for a better understaing of their architecture and use. The chosen tools are Amazon Redshift, driven for Data Warehouse solutions, and Amazon Machine Learning as an Artificial Inteligence tool. 
  
## 2. Amazon Redshift  
  
### 2.1. Introduction  
Data warehouse aggregates structured data from one or many sources intending to compared and analyze this data to extract useful information through Business Intelligence (BI) techniques. Amazon Redshift is a fast, fully managed, petabyte-scale cloud-base data warehouse solution offered by Amazon Web Services that provides simple and cost-effective functionalities to analyze all your data using standard SQL and BI techniques. In the following subsections we will be going in dept on this tool to understand its architecture, functionalities, costs and benefits.  
  
### 2.2. Characteristics (how Amazon Redshift fits your necessities)  
  
While looking for a data warehouse solution, it should fit the necessities of your business model, providing good scalability and easy integration to the technologies already in use within the company.   
  
The use Amazon Redshift brings many benefits to its user:  
  
- **Fast**: Fast query performance through column based database, improving input and output efficiency, compression and allowing parallelization of queries across multiple nodes.  
- **Inexpensive**: Amazon Redshift offers its use for $0.25 per hour on small appliances no commitments need and scalable solution to petabytes of data for $1,000 per terabyte each year, being less than a tenth of the cost for other solutions.  
- **Extensible**: Through the use of Redshift Spectrum, users can extend power of analytics beyond the data stored on local disks to unstructured data in your Amazon S3 data lakes.  
- **Simple**: Providing automation for the common administrative tasks such ass management, monitoring, and scaling Amazon Redshift let the user focus on dept in data and business.  
- **Scalable**:  Amazon Redshift let you resize your cluster up and down as much is necessary by a simple API call  
- **Secure**:  Isolate clusters made easy using Amazon VPC. Data encryption at rest by AES-256 and SSL.  
- **Compatible**: Strong compatibility to many of DBS out there, standard SQL support and JDBC and ODBC drivers can be easily integrated.  
  
### 2.3. Architecture  
Amazon Redshift was designed to fulfill the needs of systems that can start with only a few GigaBytes of data and give them the possibility to scale it to PetaBytes or more. To achieve what they propose, the architecture of Amazon Redshift is organized as follow, at high level abstraction.  
  
Redshift was developed to work in a **Cluster** formation, were a cluster contains 2 or more **Compute Nodes** coordinated through a **Leader Node**. In this way, all client applications connect to the cluster through the Leader Node. Amazon Redshift is designed to implement certain SQL functions only on the **Leader Node. A query that uses any of these functions will return an error if it references tables that reside on the compute nodes.   
  
![Redshift Arch](./img/redshift-arch.png?raw=true)
  
#### 2.3.1. Clusters  
  
For each cluster one or more compute nodes exist where for 2 or more compute nodes a leader node is necessary to coordinate. Client applications are going to interact straigth with the leader node and the compute nodes will be transparent to external applications.  
  
#### 2.3.2. Leader node  
  
The leader node takes care of the communication with the client application. All communication with compute nodes are also handled by the leader node where it parses and develops execution plans to carry the database operations. The leader node compiles code and also distributes it to the compute nodes, assigning a portion of the data to each compute node.  
  
To improve performance, SQL statements are only distributed to the compute nodes when a query references tables that are stored on that nodes. Queries run exclusively on the leader node.   
  
#### 2.3.3. Compute nodes  
  
The leader node compiles code for individual elements of the execution plan and assigns the code to individual compute nodes. The compute nodes execute the compiled code assigned by the leader node and send intermediate results back to the it for final aggregation. A dedicated CPU compounds every compute node also memory and attached disk storage, that are determined by the node type.   
  
It is possible to increase the compute capacity and storage capacity of a cluster when necessary by increasing the number of nodes or upgrading the node type.  
  
These node types can be classified by two node types where each node provides two storage choices. These dense storage nodes and dense compute nodes can start with a single 160 GB node and scale up to multiple 16 TB nodes supporting even a petabyte of data or more.  Also, each node can have multiple slices where the data will be distributed.

### 2.4. Data Distribution
As stated in the previous paragraph a node is distributed in slices, and these nodes can have one or many slices. In this way the rows of that data that are distributed across the cluster, go to slices according to the table distribution style. And as well as any other data warehouse solution, how data is distributed affects the performance of the queries.

When creating tables the distribution style needs to be specified, and for Amazon Redshift which can be ALL, EVEN, or KEY:

- **ALL**: distributes the data to all nodes. It can be good for reading performance, however higher write cost and maintenance operations.
    
- **EVEN**: distributes the data evenly across nodes. It seems suitable when the created table does require to be joined with other tables on query time.
    
- **KEY**: distributes the data by a distribution key (DistKey) as a column of the table. It makes more efficient joins with when aggregation with other tables are necessary. 
    
It is important to mention that anyhow the table must contain a SortKey once that Redshift stores data sorted by this SortKey. Also, Redshift supports the use of primary and foreign keys but does not enforce them creating the necessity of enforcing these constraints in the application side when necessary.


### 2.5. Getting Started with Amazon Redshift
 AWS provide users with a complete Get Started Tutorial, like instanciated bellow, giving them the necessary requirements to evaluate the service. 
 
-   [Step 1: Set Up Prerequisites](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-prereq.html)
    
-   [Step 2: Create an IAM Role](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html)
    
-   [Step 3: Launch a Sample Amazon Redshift Cluster](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-launch-sample-cluster.html)
    
-   [Step 4: Authorize Access to the Cluster](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-authorize-cluster-access.html)
    
-   [Step 5: Connect to the Sample Cluster](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-connect-to-cluster.html)
    
-   [Step 6: Load Sample Data from Amazon S3](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-sample-db.html)
    
-   [Step 7: Find Additional Resources and Reset Your Environment](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-clean-up-tasks.html)

#### 2.5.1 Use Case
After the previous tutorial was followed the user is abble to create a connection to Amazon Redshift by configuring the ODBC/JDBC connection settings for the computer or selected BI tool driver.

The parameters should be taken fro the On the Configuration tab, under Cluster Database Properties.
![](./img/connect-cluster.png?raw=true)

In the example below the connection is made and Tableau is used for data visualization and analysis.
![Tableau1](./img/tableau-1.png?raw=true)

Just to show the use o Amazon Redshift the image bellow show the data for sales in the categories of products and its total revenue for the time dimension on month.
![Tableau1](./img/tableau-2.png?raw=true)



## 3. Amazon Machine Learning  
### 3.1. Introduction  
Amazon Machine Learning provides powerful algorithms and makes it easy for developers to build machine learning models without learning complex machine learning technologies or hiring experts.  
  
### 3.2. Ideal Usage Pattern  
Amazon Machine Learning can be used to apply machine learning to problems. For example, we can use it to predict if the incoming email is spam or not. In overall, we can use machine learning for the following situations:  
1. It's difficult to code the rules: There are many cases that we can't just use simple rule to classify or predict a target. A large number of factors could influence the answer. It's difficult for human to codes these complicated rules, so we can use machine learning to solve the problem.  
2. It's difficult to scale: When there are only a few tasks to be classified, we can do it manually. But if we have millions of tasks, it's tedious or impossible for us to do it manually, so we can apply machine learning to help us.

Amazon Machine Learning is perfect for developers who want to apply machine learning to their business model but are not experienced in machine learning technologies. Besides, Amazon Machine Learning doesn't require to build additional computation framewwork. It's light and simple.
  
### 3.3. Steps of Creating ML models  

#### 3.3.1. Create Datasources  
Data used by Amazon Machine Learning should be cleaned and well formatted. The data format must conform to [Amazon ML guidelines](https://docs.aws.amazon.com/machine-learning/latest/dg/understanding-the-data-format-for-amazon-ml.html). Datasource is a data object that Amazon Machine Learning uses to train an ML model, evaluate an ML model and generate prediction. The datasource contains metadata of the input data. When a datasource is created, Amazon Machine Learning reads the input data, computes descriptive statistics on its attributes and stores the statistics, schema and other information as part of the datasource object. After creating the datasource, we can use it to train an ML model. 
  
#### 3.3.2. Train ML Models  
Training ML model includes applying machine learning algorithm to the datasource. But we are not required to know the detail of the machine learning algorithm. Amazon Machine Learning applies correct algorithm automatically. The datasource should have one column as target. The machine learning algorithm will find the patterns in the training data that maps the input data attributes to the target and output an ML model that captures these patterns.  
  
Amazon Machine Learning supports three types of models: *Binary Classification Model*, *Multiclass Classification Model* and *Regression Model*.  
  
The example usage for these three models are as following:  
1. Binary Classification: Predict if the incoming email is spam or not.  
2. Multiclass Classification: Predict the movie type, such as romantic, comedy, documentary or thriller.  
3. Regression Model: The house pricing in the future years.  
  
Machine learning algorithms accept parameters that can be used to control certain properties of the training process and of the resulting ML model. We can set these parameters in Amazon Machine Learning conveniently. These following values can be set: maximum model size, maximum number of passes over training data, shuffle type, regularization type and regularization amount.  
  
**(1) Maximum Model Size**  
The model size is the size of the pattern that is created by Amazon Machine Learning during training of an ML model. By default, Amazon Machine Learning creates 100 MB model. We can instruct Amazon Machine Learning to create a smaller or larger model. What should be noticed is that Amazon Machine Learning charges fees based on the model training time. when the model size is larger, the training time maybe longer as well, the fees maybe higher as well.
  
**(2) Maximum Number of Passes over the Data**  
In order to find the best performance, Amazon Machine Learning may need to make multiple passes over the data to discover patterns. By default, it's 10 passes. We can change this number up to 100 passes. But if Amazon Machine Learning can't find more patterns in the later passes, it will stop automatically. For example, if we set Maximum Number of Passes over the Data to 20, but it can't find more patterns after 15 passes, it will stop training at 15 passes automatically.  
  
**(3) Shuffle Type**  
Shuffling is important in machine learning. Shuffling data can ensure the machine learning algorithm won't encounter one type of data too frequently. If the data is already shuffled before loading into datasources, then it's not necessary to set the shuffle type. Otherwise, it's a must to set the shuffle type and shuffle data before splitting data. Officially, it's recommended to set **sgd.shuffleType** to **auto** .  
  
**(4) Regularization Type and Amount**  
Regularization helps to prevent linear models from overfitting. L1 regularization reduces the number of features used in the model by pushing the weight of features that would otherwise have very small weights to zero. L2 regularization results in smaller weight to highly correlated features. The regularization type is set to L2 by default.  
  
#### 3.3.3. Evaluate ML Models  
Afte splitting the data, the testing data is used to evaluate the ML models. In order to prevent overfitting, we can also divide the input data into three parts. 60% data is for training, 20% data is for testing and the last 10% is for validation. If the performance of testing data is similar to that of validation data. It means the ML model doesn't have overfitting problem. Besides, we can use cross-validation to detect overfitting as well. We can set to use k-fold cross-validation method to perform cross-validation. K-fold means the data will be divided into k portions. Amazon Machine Learning will use the first k-1 portions to train the model and use the last 1 portion to do test the performance. The process will repeat k times with choosing different k-1 portions to train ML model. Performing k-fold cross-validation will create k models. Amazon Machine Learning generates a model performance metric for each model and each evaluation.  
  
#### 3.3.4. Evaluation Alerts  
If any of the validation criteria are not met by the evaluation, the Amazon Machine Learning console alerts the user by displaying the validation criterion that has been violated.

**(1) Evaluation of ML model is done on held-out data**  
   If the same datasourse are used for both training and evaluation. Amazon Machine Learning will alert the user.
   
**(2) Sufficient data was used for the evaluation of the predictive model**  
   If the number of records in the evaluation data is less than 10% of the records in the training data. The alert will appear. 
   
**(3) Schema matched**  
   If the schema for training data and evaluation data are not matched. It will trigger the alert. 
   
**(4) All records from evaluation files were used for predictive model performance evaluation**  
   All records in evaluation data are supposed to be used for evaluation. But if some record of the evaluation data can't be used for evaluation, it will cause an alert in Amazon Machine Learning. For example, some records in evaluation data don't have a target value, then these records are invalid and the alert will be triggered.
   
**(5) Distribution of target variable**  
   The distribution of the target value should be similar between training data and evaluation data. If not, it will trigger the alert.  
  
#### 3.3.5. Generate and Interpret Prediction  
Amazon Machine Learning has two types of predictions: batch prediction and real-time prediction. The real-time process is good for mobile application and websites and any other application which requires the prediction results interactively. Batch prediction is a set of data and Amazon Machine Learning will predict all the records together, so it may take longer time. Batch prediction is better for an application which doesn't need to get the prediction results interactively.  
  
### 3.4. Tutorial of using Amazon Machine Learning Console
##### Step 1: Import the data into S3.  
Amazon Machine Learning supports to load data from S3 and Amazon Redshift. Here we use the sample data source provided by Amazon. It is a csv file naming *banking.csv* and it can be obtained from Amazon Machine Learning page. After downloading data on Amazon, we can import into S3.
##### Step 2: Lauch a new Amazon Machine Learning model.  
Here we launch the standard setup to create our first ML model. On the input data page, we select the S3 bucket where we store the *banking.csv* file. After defining the data location, we can continue to verify data. If it's asked for grant S3 permission, just answer yes.  
##### Step 3: Set schema of the data  
On the schema page, we can now set the schema of our data source, such as the type of the data and the target of the data. After setting all the types of the data, we can continue to the next step.  
##### Step 4: Set the model setting  
Here we use the default setting of the ML model. The default setting will split into two sections, one contains 70% of data and the other contains 30% of data. The model will use the 70% data to for training, and use the 30% data for evaluation.  
##### Step 5: Review and create ML model  
Review the ML settings on the review page. If everything is correct, we can click on *Create ML model* and continue. When the model is created, we can check from the summary page that the model status is now *pending*. There are 3 types of status, *Pending*, *In Progress* and *Completed*. *Pending* means the model is in the queue. *In Progress* means the ML creates our model. When it has completed all actions, the status will be *Completed*. After a while, if we check the summary page again, the status will be changed to *Completed*.  
##### Step 6: Review the evaluation summary  
When the model is completed, we can redirect to **Evaluation Summary** page.  
  
![ML Model Performance](./img/score.jpg?raw=true)
  
The gray line in the chart indicates actual '0' in the dataset, and the black line in the chart indicates actual '1' in the dataset. All the area with red shadow means these records are incorrectly predicted. On the left side of the screenshot, we can see there is one setting names *Trade-off based on score threshold*. Currently, the value is set to 0.5, it means if one row has scored more than 0.5, it will be predicted to 1. Otherwise, it will be predicted to 0. Below the threshold, we can see the accuracy of the prediction is around 91%. We can adjust the threshold to higher or lower value to reach more accurate prediction. We can also choose to adjust the value in *Advanced metrics*. If we want lower false positive rate, we can drag the scroll bar to lower value. Please notice that the threshold will change correspondingly. After we set all the expected value of performance, we can click on the button *"Save score threshold at \*"*. After clicking on the save button, all the steps of creating an ML model is done.  
##### Step 7: Use the created ML model to predict value  
In the tutorial, we use the ML model to predict real-time data. At the right side of the ML model report page, we redirect to *"Try real-time predictions"* page. We can either input a row of data or paste one record. After populating the value for each field, we can click on the *"Create Prediction"* button to submit the record. The prediction result is displaying on the right side of the page.  
![Prediction Result](./img/Prediction_Result.jpeg?raw=true)
We can see that the prediction for my input data is "0".  
  
We can also use the Amazon Machine Learning to do the batch process. Please notice that the data should be stored S3 or Redshift as well which is similar to the "Step 1".

### 3.5. Sample Code of using Amazon Machine Learning API
Before using the Amazon Machine Learning API, we should do some preparations.

1. Import the data file into S3 bucket and grant read and write permissions to this s3 bucket.
2. Prepare the schema file to the input data file. The sample schema file can be found as *banking.csv.schema* and *banking-batch.csv.schema*.
3. Prepare the *recipe.json*. This file is used to instruct Amazon Machine Learning to transform data as a part of the machine learning process.
4. Add *AmazonMachineLearningFullAccess* permission to current user.

##### Step 1: Build the model
After completing the preparation, we can start the create datasources.The input data is splitted into two parts, one is for training process, and another is for testing process. 


    def create_data_sources(data_s3_url, input_data, train_percent=70):

        ml = boto3.client("machinelearning")
        train_ds_id = 'ds-' + base64.b32encode(os.urandom(10)).decode()
        spec = {
            "DataLocationS3": data_s3_url,
            "DataRearrangement": json.dumps({
                "splitting": {
                    "percentBegin": 0,
                    "percentEnd": train_percent
                }
            }),
            "DataSchema": open(input_data).read(),
        }
    
        ml.create_data_source_from_s3(
            DataSourceId = train_ds_id,
            DataSpec=spec,
            DataSourceName="training",
            ComputeStatistics=True
        )
        print("Training data set created\n")
    
        test_ds_id = 'ds-' + base64.b32encode(os.urandom(10)).decode()
    
        spec ={
            "DataLocationS3": data_s3_url,
            "DataRearrangement": json.dumps({
                "splitting":{
                    "percentBegin": train_percent,
                    "percentEnd":100
                }
            }),
            "DataSchema": open(input_data).read(),
        }
    
        ml.create_data_source_from_s3(
            DataSourceId=test_ds_id,
            DataSpec=spec,
            DataSourceName="testing",
            ComputeStatistics=True
        )
        print("Test data set created\n")
        return (train_ds_id,test_ds_id)

After creating the datasources, we can use the train datasource to create the model.
    
    def create_model(train_id, recipe):

    ml = boto3.client("machinelearning")
    model_id = 'ml-' + base64.b32encode(os.urandom(10)).decode()
    ml.create_ml_model(
        MLModelId=model_id,
        MLModelName="first_model",
        MLModelType="BINARY",  # we're predicting True/False values
        Parameters={
            # Refer to the "Machine Learning Concepts" documentation
            # for guidelines on tuning your model
            "sgd.maxPasses": "100",
            "sgd.maxMLModelSizeInBytes": "104857600",  # 100 MiB
        },
        Recipe=open(recipe).read(),
        TrainingDataSourceId=train_id
    )
    print("ML Model created")
    return model_id
 
 After the model is created, the model is ready is to be evaluated by using test datasource.
 
    def create_evaluation(model_id, test_id):
        ml = boto3.client("machinelearning")
        eval_id = 'eval-' + base64.b32encode(os.urandom(10)).decode()
        ml.create_evaluation(
            EvaluationId=eval_id,
            EvaluationName="evaluation",
            MLModelId=model_id,
            EvaluationDataSourceId=test_id
        )
        print("Evaluation created")
        return eval_id
 
After finishing these tree steps, we can go back to the Amazon Machine Learning console, we will find a new ml model and two more datasources are created.
 
##### Step 2: Use the model
Similar to step 1, we need to create datasource for the batch data.

    def create_data_sources(data_s3url, input_data):

        ml = boto3.client("machinelearning")
        ds_id = 'ds-' + base64.b32encode(os.urandom(10)).decode()
    
        ml.create_data_source_from_s3(
            DataSourceId=ds_id,
            DataSourceName="batch_prediction",
            DataSpec={
                "DataLocationS3": data_s3url,
                "DataSchema": open(input_data).read(),
            },
            ComputeStatistics=False
        )
        print("Batch datasource created")
        return ds_id
The batch datasource id is useful to do prediction, but we need to wait until the model is successfully created. The following *poll_until_completed* method is used to check model status.

    def poll_until_completed(model_id):

        ml = boto3.client("machinelearning")
        delay = 2
        while True:
            model = ml.get_ml_model(MLModelId=model_id)
            status = model['Status']
            if status in ['COMPLETED', 'FAILED', 'INVALID']:
                break
            delay *= random.uniform(1.1, 2.0)
            time.sleep(delay)

When the model creation is finished, the preiction process will start. The model can still be updated by calling *update_ml_model* API, such as optimize the threshold.
    
    def use_model(model_id, threshold, ds_id):

        ml = boto3.client('machinelearning')
    
        ml.update_ml_model(MLModelId=model_id, ScoreThreshold=threshold)
    
        bp_id = 'bp-' + base64.b32encode(os.urandom(10)).decode()
        ml.create_batch_prediction(
            BatchPredictionId=bp_id,
            BatchPredictionName="Batch Prediction for marketing sample",
            MLModelId=model_id,
            BatchPredictionDataSourceId=ds_id,
            OutputUri="s3://ccbda-upc-rui/output"
        )
        print("Batch prediction created")
        
The prediction result will be stored in the defined *OutputUri* location. If we get back to the Amazon Machine Learning console, one more prediction is added on the dashboard.

### 3.6. Cost Model  
There is no free tier for Amazon Machine Learning. The costs for Amazon Machine Learning are basically two parts: data analysis and model build fees and prediciton fees. Data analysis and model build fees are based on the number of compute hours required to perform them. The consuming time depends on the size of the input data, the number of attributes within it and the number and types of transformation applied. Prediction fees depend on the number of predictions performed. For Batch Prediction, it's $0.01 per 1000 prediction, rounded up to the next 1000. For Real-Time Prediction, it's $0.0001 per prediction, rounded up to the nearest penny. If Real-Time Prediction is used, Amazon Machine Learning will charge $0.001 per hour for each 10 MB of memory provisioned for the model. Officially, it recommended using Batch Prediction.  
  
### 3.7. Advantages and Disadvantages  
Amazon Machine Learning is very automatic, as soon as we load the data source and set the basic setting of the model, the model can be created automatically and is ready to be used to detect future datasources. We don't need to master the machine learning knowledge and we can benefit from machine learning. But the training process is black-box, we don't know what machine learning algorithm is applied to the model, so it's very hard to explain the model. 
  
Amazon Machine Learning supports tree types of models: *Binary Classification Model*, *Multiclass Classification Model* and *Regression Model*. These three models are supervised models. In other words, Amazon Machine Learning doesn't support unsupervised model.
