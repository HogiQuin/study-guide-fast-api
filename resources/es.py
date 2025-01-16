TEXT_ES = {
  "spanish_mexico": {
    "text": "Los microservicios son una arquitectura avanzada que divide una aplicación en servicios pequeños e independientes. Cada servicio está diseñado para realizar una tarea específica y se comunica con otros a través de APIs ligeras como HTTP o gRPC. Esta arquitectura ofrece alta escalabilidad, aislamiento de fallos y flexibilidad para despliegues continuos. Sin embargo, también presenta retos como la gestión de comunicaciones entre servicios, la supervisión de fallos distribuidos y la sincronización de dependencias.\n\nUn principio clave de los microservicios es la independencia. Cada servicio tiene su propia base de datos, lo que garantiza una autonomía total y minimiza los conflictos. Esto facilita el desarrollo simultáneo por diferentes equipos. Herramientas como RabbitMQ o Kafka son usadas para manejar comunicaciones asíncronas, mientras que Prometheus y Grafana permiten supervisión en tiempo real. Finalmente, Kubernetes suele ser utilizado para la orquestación de contenedores, simplificando el despliegue de microservicios en entornos distribuidos.",
    "questions": [
      {
        "question": "¿Cuál es la principal ventaja de los microservicios?",
        "options": [
          "A. Centralizar todos los servicios.",
          "B. Incrementar la escalabilidad y flexibilidad.",
          "C. Reducir la necesidad de APIs.",
          "D. Fusionar todas las bases de datos."
        ],
        "correct_answer": "B"
      },
      {
        "question": "¿Qué herramienta se utiliza para la orquestación de contenedores?",
        "options": [
          "A. Kubernetes",
          "B. RabbitMQ",
          "C. Prometheus",
          "D. Terraform"
        ],
        "correct_answer": "A"
      },
      {
        "question": "¿Cómo gestionan los microservicios las comunicaciones asíncronas?",
        "options": [
          "A. Utilizando HTTP.",
          "B. Con buses de mensajes como RabbitMQ o Kafka.",
          "C. Compartiendo archivos locales.",
          "D. Centralizando las bases de datos."
        ],
        "correct_answer": "B"
      },
      {
        "question": "¿Cuál es un principio fundamental de los microservicios?",
        "options": [
          "A. Una base de datos centralizada para todos los servicios.",
          "B. Independencia total entre los servicios.",
          "C. Código compartido entre los servicios.",
          "D. Reducir las APIs utilizadas."
        ],
        "correct_answer": "B"
      },
      {
        "question": "¿Qué herramienta permite la supervisión en tiempo real de los microservicios?",
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
}
