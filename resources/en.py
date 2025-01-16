TEXT_EN = {
  "text": "Microservices represent an advanced architecture where an application is divided into independent and specialized services. These services operate autonomously and communicate through lightweight APIs like HTTP or gRPC. Microservices offer increased scalability, fault tolerance, and flexibility for continuous deployment. However, they also introduce challenges such as managing interservice communications, monitoring distributed failures, and synchronizing dependencies.\n\nA key principle of microservices is independence. Each service has its own database, ensuring full autonomy and reducing the risk of conflicts. Tools like RabbitMQ or Kafka are used to handle asynchronous communications, while Prometheus and Grafana enable real-time monitoring. Finally, Kubernetes is commonly used for container orchestration, simplifying the deployment of microservices in distributed environments.",
  "questions": [
    {
      "question": "What is the primary advantage of microservices?",
      "options": [
        "A. Centralizing all services.",
        "B. Improving scalability and flexibility.",
        "C. Reducing the need for APIs.",
        "D. Merging all databases."
      ],
      "correct_answer": "B"
    },
    {
      "question": "Which tool is used for container orchestration?",
      "options": [
        "A. Kubernetes",
        "B. RabbitMQ",
        "C. Prometheus",
        "D. Terraform"
      ],
      "correct_answer": "A"
    },
    {
      "question": "How do microservices handle asynchronous communications?",
      "options": [
        "A. By using HTTP.",
        "B. With message buses like RabbitMQ or Kafka.",
        "C. By sharing local files.",
        "D. By centralizing databases."
      ],
      "correct_answer": "B"
    },
    {
      "question": "What is a fundamental principle of microservices?",
      "options": [
        "A. A centralized database for all services.",
        "B. Total independence among services.",
        "C. Shared code between services.",
        "D. Reduced use of APIs."
      ],
      "correct_answer": "B"
    },
    {
      "question": "Which tool enables real-time monitoring of microservices?",
      "options": [
        "A. MySQL",
        "B. Prometheus",
        "C. Kubernetes",
        "D. Git"
      ],
      "correct_answer": "B"
    }
  ]
}
