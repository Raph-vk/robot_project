#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Range.h>
#include <std_msgs/Bool.h>

ros::NodeHandle nh;

sensor_msgs::Range range_msg;
ros::Publisher pub_range("sensor_info", &range_msg);

char frameid[] = "/ultrasound";

const int trigPin = 11;
const int echoPin = 12;
const int motorPin = 13;  // Change as needed (usually 13 for onboard LED or external transistor)

long duration;
double distance_mm;

#define MAX_RANGE 1.00
#define MIN_RANGE 0.10

void motorCallback(const std_msgs::Bool &msg) {
  digitalWrite(motorPin, msg.data ? HIGH : LOW);
}
ros::Subscriber<std_msgs::Bool> sub_motor("motor_state", motorCallback);

void setup() {
  nh.initNode();
  nh.advertise(pub_range);
  nh.subscribe(sub_motor);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motorPin, OUTPUT);
  digitalWrite(motorPin, LOW); // Start with motor off
}

unsigned long publisher_timer;

void loop() {
  if (millis() > publisher_timer) {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    distance_mm = duration * 0.00034 / 2;

    range_msg.range = distance_mm;
    range_msg.radiation_type = sensor_msgs::Range::ULTRASOUND;
    range_msg.field_of_view = 0.5;
    range_msg.min_range = MIN_RANGE;
    range_msg.max_range = MAX_RANGE;

    range_msg.range = max(range_msg.min_range, min(range_msg.max_range, range_msg.range));

    range_msg.header.stamp = nh.now();
    range_msg.header.frame_id = "distance_sensor_frame";
    pub_range.publish(&range_msg);

    publisher_timer = millis() + 100;
  }

  nh.spinOnce();
}
