from ..core import Core


# from kryptobot import ticker
# listener = Listener(ticker, {'interval':'15s'})
class BaseListener(Core):

    # publisher is a pubsub to subscribe to
    def __init__(self, publisher, publisher_params, config=None):
        super().__init__(config)
        publisher.subscribe(self.on_message, **publisher_params)
        self.publisher = publisher

    # Extend class and override on_message method
    def on_message(self):
        print('ticked')
