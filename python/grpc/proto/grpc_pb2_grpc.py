# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpc_pb2 as grpc__pb2


class GreeterStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.audio_classify = channel.unary_unary(
        '/audio.Greeter/audio_classify',
        request_serializer=grpc__pb2.VideoRequest.SerializeToString,
        response_deserializer=grpc__pb2.VideoReply.FromString,
        )


class GreeterServicer(object):
  """The greeting service definition.
  """

  def audio_classify(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'audio_classify': grpc.unary_unary_rpc_method_handler(
          servicer.audio_classify,
          request_deserializer=grpc__pb2.VideoRequest.FromString,
          response_serializer=grpc__pb2.VideoReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'audio.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
