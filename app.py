 
import streamlit as st
from streamlit_option_menu import option_menu


st. set_page_config(layout="wide")

def main():
    st.title("Welcome, Data Chad! 📊")
    st.header("Question Pool - Big Data Architecture and Core Technologies")

    st.write("Need Help? Use [ChatGPT 😎](https://chat.openai.com/)")

    st.markdown(
    """
1.		Describe the functions and features of HDP
2.		Describe the nature of the Hadoop Distributed File System
3.		Elucidate the function of the NameNode and DataNodes in a Hadoop cluster
4.		Elucidate the MapReduce in Hadoop
5.		Elucidate the Yarn in Hadoop
6.		Elucidate the HDFS in Hadoop
7.		Point out the limitation in the HDFS
8.		Point out the limitation in the MapReduce
9.		Point out the limitation in the Yarn
10.		Explain the functionality of Mapper class
11.		Explain the functionality of Reducer  class
12.		Categorize the characteristics of the Hadoop
13.		Summarize the different types of data types in Hive
14.		Describe the Resource Manager in Yarn
15.		Describe the Node Manager in Yarn
16.		Explain the merits and demerits of Yarn
17.		Explain the merits and demerits of MapReduce
18.		Explain the merits and demerits of HDFS
19.		compare and evaluate the major hadoop distributions and their ecosystem
20.		Elucidate the Hadoop architecture and its components
21.		Demonstrate the working of MapReduce and Yarn
22.		Design a code to convert RDD into a Dataframe
23.		Summarize what you have understand by term Pillars of Big Data
24.		Illustrate the 5 V’s of big data.
25.		Illustrate with example as to how the executer memory in apache spark is calculated.
26.		Do we have primary key concept in hive. Explain
27.		Illustrate with example that how the files are split , replicated and stored in HDFS. 
28.		What is dynamic partitioning and when is it used and its advantages?
29.		List the Five Pillars of security and how they are implemented with HDP.
30.		What is the need for broadcast variables in Spark.
31.		Explain the reason behind mapreduce being slower in processing data comparison to other framework.
32.		Point out the defferences Between Data Analytics and Data Science
33.		Show the Difference between supervised and unsupervised learning? 
34.		Elucidate the Supervised learning
35.		Elucidate the unsupervised learning
36.		You are given a data set consisting of variables with more than 30 percent missing values. How will you deal with them?
37.		Design a code for start and stop services     from Ambari Web Console
38.		Explain with diagram the sliding window operation
39.		Write a command to connect Hive to Spark SQL. 
40.		List the analytic algorithms provided in Apache Spark. 
41.		How can you set up automatic cleanups in Spark to deal with metadata that has built up?  
42.		Elucidate with a diagram the architecture of spark Unified stack
43.		Elucidate the difference between Tableau Desktop and IBM Cognos
44.		If the model is not durable, then what would you change to make the model durable? 
45.		Illustrate the procedure for Query Generation. 
46.		How do you create security features for cubes? 
47.		Illustrate the  working of Dynamic Query Mode.
48.		What is ETL?
49.		What is a data warehouse and how is it different from a data mart
50.		What   are   the   factors   affecting   the   modern   decision   making   process   in   business organisations? 
51.		Explain with the diagram the process flow in data warehouse
52.		List the responsibilities of Cognos Administrator 
53.		List the types of Tabular filter in the report studio?
54.		Write a procedure for Viewing tabular data in Cognos.
55.		List the responsibilities of the Cognos Administrator 
56.		Illustrate with example the cardinality in Cognos.
57.		How System optimization with large data sets in lists is achieved?
58.		Write down the steps to add a data source to the exploration 
59.		How do GDSS differ from a normal DSS List any 5 characteristics of group decision support system.
60.		Diagrammatically explain the stages of Data warehousing 
61.		Illustrate with example the data warehouse architecture with respect to: 
        I)	Staging area.
        II)	Staging area and Mart
62.		Illustrate the functions performed by OLAP
63.		Differentiate between OLTP and OLAP
64.		List the types of Dimensional Modeling
65.		What are the different types of data warehousing
66.		What is the difference between a Database and a Data Warehouse?
67.		What is the difference between ER Modelling vs. Dimensional Modelling?
68.		Provide a couple of current Data Warehouse solutions widely used in the Industry.
69.		What is DDDM ?
70.		How Cognos Analytics helps in decision making
71.		Explain IBM Cognos event Studio 
72.		Explain IBM Cognos Metric Studio
73.		Which one is faster: multidimensional OLAP or relational OLAP : Justify.
74.		Elucidate the purpose of Drill up and drill down in IBM Cognos exploration
75.		What are the three levels of decision making that software such as IBM analytics support?
76.		List the different types of prompts and gateways available in Cognos.
77.		Illustrate the benefits of Data Warehouse.
78.		What are the functions of Query Management Process.
79.		Identify and explain the distinct usage patterns in DSS
80.		What are the types of Decision Support Systems ?
81.		Explain the role of each process in DSS
82.		What are two types of intermediaries that reflect different types of support for the manager
83.		What is the purpose of IBM Cognos Software Development Kit
84.		Understanding how Big SQL fits in the Hadoop architecture
85.		Write down the steps showing how Db2 Big SQL processes HDFS data.
86.		Implement the Start and stop Big SQL using Ambari and command line
87.		Implement how we Connecting to Big SQL using command line 
88.		Describe and create Big SQL schemas and tables
89.		How can we get Connected to Big SQL using IBM Data Server Manager
90.		Describe and list the Big SQL data types
91.		Demonstrate the working with various Big SQL DDLs 
92.		Describe Big SQL supported file formats
93.		Illustrate query Big SQL tables using various DMLs
94.		How can we Configure authentication for Big SQL
95.		How can we Configure authorization of Big SQL objects
96.		Explain the concept of Big SQL
97.		Write a Big SQL query to create a table
98.		What are the two levels of isolation and what is the major difference between the 2 levels?
99.		List out the three types of page locks that can be held.
100.		Is it possible for you to alter the table (adding a column to it) while some other person is accessing the table and even updating some values in it?Justify
101.		Mention the length of physical storage of the given data types of DB2 – DATE, TIMESTAMP, TIME
102.		Mention a credible reason why SELECT is not preferred in embedded SQL programs?
103.		Describe the challenges of working with unstructured data in Db2?
104.		Name the four buffer pools in Db2.
105.		Write  SQL statements showing the difference between SMALLINT and INTEGER
106.		Why SELECT is not preferred in Embedded SQL programs?
107.		Demonstrate how we can create a view in big SQL
108.		Demonstrate how we can load data in big SQL
109.		Usually, which is more important for DB2 system performance – CPU processing or I/O access?
110.		Explain about HBase
111.		Point out the differences between HBase and relational database
112.        Elucidate the purpose of DB2 big SQL 
113.		When can an insert of a new primary key value threaten referential integrity?
114.		Summarize the Big SQL for best practice 
115.		Draw a neat diagram of Big SQL architecture describing its components in detail.
116.		What is the result of this query if no rows are selected:
            SELECT SUM(SALARY)
            FROM EMP
            WHERE QUAL=?MSC?
117.		As a DB2 DBA how would you approach a job or a query which is consuming more time than normal? Which commands would you use and what all steps would you take to resolve it?
118.		What is the function of buffer manager? 
119.		Write a SQL statement  to retrieve nth row from particular table.
120.		Illustrate the use of ALTER statement

    """
)


with st.sidebar:
    selected = option_menu('Subjects',['BDAC','BDT ⛔','NOS ⛔','TOC ⛔'], default_index=0)
    st.header("Note 🔔")
    st.write("- Site under construction")
    st.write("- ⛔ : No Access, Your access is limited to BDAC for now!")


if __name__ == '__main__':
    main()

