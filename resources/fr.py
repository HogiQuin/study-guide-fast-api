TEXT_FR = {
  "text": "Les microservices représentent une architecture avancée où une application est divisée en services indépendants et spécialisés. Ces services fonctionnent de manière autonome et communiquent via des API légères comme HTTP ou gRPC. Les microservices permettent une scalabilité accrue, une tolérance aux pannes et une flexibilité de déploiement continu. Cependant, cette architecture introduit des défis comme la gestion des communications interservices, la surveillance des défaillances distribuées, et la synchronisation des dépendances.\n\nUn concept clé des microservices est l'indépendance. Chaque service possède sa propre base de données, garantissant une autonomie totale et réduisant les risques de conflits. Cela favorise le développement simultané par plusieurs équipes. Les outils comme RabbitMQ ou Kafka sont utilisés pour gérer les communications asynchrones, tandis que Prometheus et Grafana permettent une supervision en temps réel. Enfin, Kubernetes est souvent utilisé pour l'orchestration des conteneurs, ce qui simplifie le déploiement des microservices dans des environnements distribués.",
  "questions": [
    {
      "question": "Quel est l'avantage principal des microservices ?",
      "options": [
        "A. Centraliser tous les services.",
        "B. Augmenter la scalabilité et la flexibilité.",
        "C. Réduire le besoin d'API.",
        "D. Fusionner toutes les bases de données."
      ],
      "correct_answer": "B"
    },
    {
      "question": "Quel outil est utilisé pour l'orchestration des conteneurs ?",
      "options": [
        "A. Kubernetes",
        "B. RabbitMQ",
        "C. Prometheus",
        "D. Terraform"
      ],
      "correct_answer": "A"
    },
    {
      "question": "Comment les microservices gèrent-ils les communications asynchrones ?",
      "options": [
        "A. En utilisant HTTP.",
        "B. Avec des bus de messages comme RabbitMQ ou Kafka.",
        "C. En partageant des fichiers locaux.",
        "D. En centralisant les bases de données."
      ],
      "correct_answer": "B"
    },
    {
      "question": "Quel est un principe fondamental des microservices ?",
      "options": [
        "A. Une base de données centralisée pour tous les services.",
        "B. Une indépendance totale entre les services.",
        "C. Un code partagé entre les services.",
        "D. Une réduction des API utilisées."
      ],
      "correct_answer": "B"
    },
    {
      "question": "Quel outil permet une supervision en temps réel des microservices ?",
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
