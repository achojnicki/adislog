from ..constants import MSG_FORMAT, LOG_LEVELS

from json import dumps
from pika import BlockingConnection, ConnectionParameters, PlainCredentials


class rabbitmq_emiter:
    def __init__(self,
                 rabbitmq_host,
                 rabbitmq_port,
                 rabbitmq_queue,
                 rabbitmq_credentials,
                 **kwargs
                 ):
         
        self._rabbitmq_host=rabbitmq_host
        self._rabbitmq_port=rabbitmq_port
        self._rabbitmq_credentials=rabbitmq_credentials,
        self._rabbitmq_queue=rabbitmq_queue
        
        self._connection=BlockingConnection(
            ConnectionParameters(
                host=rabbitmq_host,
                port=rabbitmq_port,
                credentials=rabbitmq_credentials
                ))
        
        self._rabbitmq_channel=self._connection.channel()
        
        self._rabbitmq_channel.queue_declare(queue=rabbitmq_queue)
        
    def emit(self,
             message:str,
             datetime:str,
             filename:str,
             function: str,
             line_number:int,
             log_level:int,
             pid:int,
             ppid:int,
             cwd:str,
             excpt_data=None):
        
        msg={
            'message':message,
            'datetime':datetime,
            'filename':filename,
            'function':function,
            'line_number':line_number,
            'log_level':LOG_LEVELS[log_level],
            'pid':pid,
            'ppid':ppid,
            'cwd':cwd,
            }
        msg=dumps(msg)

        self._rabbitmq_channel.basic_publish(
            exchange="",
            routing_key=self._rabbitmq_queue,
            body=msg
        )
        
    
        
