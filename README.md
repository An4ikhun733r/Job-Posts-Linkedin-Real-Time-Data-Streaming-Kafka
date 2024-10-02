
# Real-Time LinkedIn Job Post Streaming

## Structure of the Project
![image](https://github.com/user-attachments/assets/6835760b-9b9e-42c7-893e-40af84c509ba)


## Overview

This project enables real-time streaming of LinkedIn job postings to Kafka, where the data is processed and stored in the cloud. By utilizing various AWS services, this application showcases the power of real-time data processing, cloud storage, and advanced data visualization.

## Key Features

- **Real-Time Data Streaming**: Job postings are streamed in real-time from LinkedIn to Kafka, allowing immediate access to the latest job listings.
- **Cloud Storage**: Data is stored securely in Amazon S3, ensuring durability and accessibility.
- **Data Processing**: AWS Glue is used to transform and prepare data for analysis.
- **Querying and Analysis**: Amazon Athena allows for querying the stored data using standard SQL, making it easy to analyze job posting trends.
- **Data Visualization**: Amazon QuickSight provides powerful visualization tools to gain insights from job posting data, enabling data-driven decision-making.

## Technologies Used

- **Apache Kafka**: For real-time data streaming and messaging.
- **AWS S3**: For scalable and secure storage of job postings.
- **AWS Glue**: For ETL (Extract, Transform, Load) processes to clean and prepare data.
- **Amazon Athena**: For serverless SQL querying of S3 data.
- **Amazon QuickSight**: For creating interactive dashboards and visualizations.
- **Python**: For writing the crawler and Kafka producer/consumer applications.

## Project Structure

The project consists of the following main components:

- **Data Crawler**: Collects job postings from LinkedIn.
- **Kafka Producer**: Streams job data to a Kafka topic.
- **Kafka Consumer**: Consumes data from the Kafka topic and processes it for storage in S3.
- **AWS Glue**: Manages ETL jobs to prepare data for analysis.
- **Amazon Athena**: Queries the data stored in S3.
- **Amazon QuickSight**: Visualizes the queried data for insights.

## Dataset used
Every day, thousands of companies and individuals turn to LinkedIn in search of talent. This dataset contains a nearly comprehensive record of 124,000+ job postings listed in 2023 and 2024. 
https://www.kaggle.com/datasets/arshkon/linkedin-job-postings


## Amathon S3 Buckets Obtained Through Real Time Streaming
![image](https://github.com/user-attachments/assets/96fb22b4-c907-4419-a732-f957d3c3cd64)

## Amathon Arthena Table
![image](https://github.com/user-attachments/assets/f9f78a85-7d13-4304-9288-3452acfadcf8)

## Visualisations obtained
![image](https://github.com/user-attachments/assets/7d85b8ad-26eb-46bc-addf-f80334b53978)

## Getting Started

### Prerequisites

- Python 3.x
- Kafka
- AWS account with S3, Glue, Athena, and QuickSight access

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

3. Set up your Kafka server and configure the producer and consumer.

4. Configure AWS credentials for S3, Glue, and Athena.

5. Run the crawler to start collecting job postings.

### Usage

1. Start the Kafka producer to stream job postings.
2. Start the Kafka consumer to process and store data in S3.
3. Use AWS Glue to prepare the data.
4. Query the data using Amazon Athena.
5. Create visualizations in Amazon QuickSight.

## Conclusion

This project demonstrates the integration of various technologies for real-time data streaming, cloud storage, and data visualization. It serves as a powerful tool for analyzing job market trends and gaining insights into job postings from LinkedIn.

For any questions or contributions, please feel free to reach out!
