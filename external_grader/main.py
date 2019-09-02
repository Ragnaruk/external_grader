import logging

import pika.exceptions

from receive_messages import receive_messages
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_CONSUMPTION_QUEUE


def main() -> None:
    """
    Initialize logger and start listening to messages from broker.
    https://edx.readthedocs.io/projects/edx-partner-course-staff/en/latest/exercises_tools/external_graders.html#olx-definition
    """
    logging.basicConfig(
        filename="grader.log",
        level=logging.INFO,
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    try:
        receive_messages(RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_CONSUMPTION_QUEUE)
    except pika.exceptions.AMQPConnectionError:
        logging.getLogger("ExternalGrader").error("Failed to connect to RabbitMQ broker.")
    except KeyboardInterrupt:
        logging.getLogger("ExternalGrader").info("Program has been stopped manually.")
    except Exception as exception:
        logging.getLogger("ExternalGrader").error(exception)


if __name__ == "__main__":
    main()
