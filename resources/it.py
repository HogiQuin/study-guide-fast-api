TEXT_IT = {
  "text": "I microservizi rappresentano un'architettura avanzata in cui un'applicazione è suddivisa in servizi indipendenti e specializzati. Questi servizi operano in modo autonomo e comunicano tramite API leggere come HTTP o gRPC. I microservizi offrono maggiore scalabilità, tolleranza ai guasti e flessibilità nel deployment continuo. Tuttavia, questa architettura introduce sfide come la gestione delle comunicazioni tra servizi, il monitoraggio delle anomalie distribuite e la sincronizzazione delle dipendenze.\n\nUn principio fondamentale dei microservizi è l'indipendenza. Ogni servizio ha il proprio database, garantendo completa autonomia e riducendo i rischi di conflitti. Strumenti come RabbitMQ o Kafka vengono utilizzati per gestire le comunicazioni asincrone, mentre Prometheus e Grafana consentono il monitoraggio in tempo reale. Infine, Kubernetes è spesso utilizzato per l'orchestrazione dei container, semplificando il deployment dei microservizi in ambienti distribuiti.",
  "questions": [
    {
      "question": "Qual è il principale vantaggio dei microservizi?",
      "options": [
        "A. Centralizzare tutti i servizi.",
        "B. Migliorare scalabilità e flessibilità.",
        "C. Ridurre la necessità di API.",
        "D. Unificare tutti i database."
      ],
      "correct_answer": "B"
    },
    {
      "question": "Quale strumento viene utilizzato per orchestrare i container?",
      "options": [
        "A. Kubernetes",
        "B. RabbitMQ",
        "C. Prometheus",
        "D. Terraform"
      ],
      "correct_answer": "A"
    },
    {
      "question": "Come gestiscono i microservizi le comunicazioni asincrone?",
      "options": [
        "A. Utilizzando HTTP.",
        "B. Con bus di messaggi come RabbitMQ o Kafka.",
        "C. Condivisione di file locali.",
        "D. Centralizzando i database."
      ],
      "correct_answer": "B"
    },
    {
      "question": "Qual è un principio fondamentale dei microservizi?",
      "options": [
        "A. Un database centralizzato per tutti i servizi.",
        "B. Totale indipendenza tra i servizi.",
        "C. Codice condiviso tra i servizi.",
        "D. Riduzione dell'uso delle API."
      ],
      "correct_answer": "B"
    },
    {
      "question": "Quale strumento consente il monitoraggio in tempo reale dei microservizi?",
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
