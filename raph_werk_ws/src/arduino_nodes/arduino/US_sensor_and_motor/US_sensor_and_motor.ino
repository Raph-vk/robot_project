/*
  Ultrasonic Sensor HC-SR04 ROS Publisher with Motor Control via ROS Subscriber
*/

#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Range.h>
#include <std_msgs/Bool.h> // Include standard Bool message type

ros::NodeHandle nh;

// ---- Sensor Publisher Setup ----
sensor_msgs::Range range_msg;
ros::Publisher pub_range("sensor_info", &range_msg);



// ---- Motor Control Setup ----
const int motorPin = 13; // Digital pin connected to the motor switch
bool motor_state = false; // Store the motor state (on/off)

// Callback function to handle incoming boolean messages
void motorCallback(const std_msgs::Bool &msg) {
  motor_state = msg.data; // Update the motor state
  digitalWrite(motorPin, motor_state ? HIGH : LOW); // Control motor accordingly
}

// ROS Subscriber to receive motor control commands
ros::Subscriber<std_msgs::Bool> sub_motor("motor_switch", &motorCallback);



// ---- Ultrasound Sensor Setup ----
const int trigPin = 11;
const int echoPin = 12;
long duration;
double distance_mm;

#define MAX_RANGE 1.00
#define MIN_RANGE 0.10

#define USE_ROS //use ROS functionality

void setup() {

#ifdef USE_ROS
  nh.initNode(); // Initialize ROS node
  nh.advertise(pub_range); // Advertise the sensor data topic
  nh.subscribe(sub_motor); // Subscribe to motor control topic
#else
  Serial.begin(115200); // For debugging without ROS
#endif

  // Setup pin modes
  pinMode(trigPin, OUTPUT); // Trigger pin for ultrasonic
  pinMode(echoPin, INPUT);  // Echo pin for ultrasonic
  pinMode(motorPin, OUTPUT); // Motor control pin
  digitalWrite(motorPin, LOW); // Start with motor off
}

unsigned long publisher_timer;

void loop() {
  if (millis() > publisher_timer) {

    // Trigger the ultrasonic sensor
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Read the echo pin and compute distance
    duration = pulseIn(echoPin, HIGH);
    distance_mm = duration * 0.00034 / 2; // Convert to mm (speed of sound)

#ifdef USE_ROS
    // Populate the ROS Range message
    range_msg.range = distance_mm;
    range_msg.radiation_type = sensor_msgs::Range::ULTRASOUND;
    range_msg.field_of_view = 0.5;
    range_msg.min_range = MIN_RANGE;
    range_msg.max_range = MAX_RANGE;

    // Clamp the range values
    if (range_msg.range > MAX_RANGE) range_msg.range = MAX_RANGE;
    if (range_msg.range < MIN_RANGE) range_msg.range = MIN_RANGE;

    // Set the message header
    range_msg.header.stamp = nh.now();
    range_msg.header.frame_id = "distance_sensor_frame";

    // Publish the message
    pub_range.publish(&range_msg);
#else
    Serial.print("Distance (mm): ");
    Serial.println(distance_mm);
#endif

    // Update the timer to run every 100 ms
    publisher_timer = millis() + 100;
  }

  nh.spinOnce(); // Process ROS messages (including the subscriber)
}