var opt ={ host: 'chichiapp.ir'
, port: 5672
, login: 'guest'
, password: 'guest'
, connectionTimeout: 10000
, authMechanism: 'AMQPLAIN'
, vhost: '/'
, noDelay: true
, ssl: { enabled : false
       }
};
var amqp = require('amqp');


var connection = amqp.createConnection(opt);
var channel = connection.channels;

// add this for better debuging
connection.on('error', function(e) {
  console.log("Error from amqp: ", e);
});

// Wait for connection to become established.
connection.on('ready', function () {
  // Use the default 'amq.topic' exchange
  connection.queue('my-queue', function (q) {
      // Catch all messages
      q.bind('#');



      // Receive messages
      q.subscribe(function (message) {
        // Print messages to stdout
        console.log(message);
      });
  });
});
