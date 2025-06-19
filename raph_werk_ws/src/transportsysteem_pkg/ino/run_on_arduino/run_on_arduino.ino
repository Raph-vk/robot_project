#include <ros.h>
#include <std_msgs/Bool.h>

// Define pins
const int IRbeginPin = 12;
const int IRendPin   = 4;

const int ENA = 9;
const int IN1 = 8;
const int IN2 = 7;

// Motor speed (0–255)
int speed = 255;

// ROS node handle
ros::NodeHandle nh;

// Publishers for the two IR sensors
std_msgs::Bool ir_begin_msg;
ros::Publisher ir_begin_pub("/ir_begin", &ir_begin_msg);

std_msgs::Bool ir_end_msg;
ros::Publisher ir_end_pub("/ir_end", &ir_end_msg);

// Motor control flag
bool motor_running = false;

// Subscriber callback for motor on/off
void motorCommandCallback(const std_msgs::Bool& msg) {
  motor_running = msg.data;
  if (motor_running) {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    analogWrite(ENA, speed);
  } else {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    analogWrite(ENA, 0);
  }
}
ros::Subscriber<std_msgs::Bool> motor_sub("/motor_command", &motorCommandCallback);

void setup() {
  // Motor pins
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  // IR sensor pins
  pinMode(IRbeginPin, INPUT);
  pinMode(IRendPin,   INPUT);

  // Initialize ROS
  nh.initNode();
  nh.advertise(ir_begin_pub);
  nh.advertise(ir_end_pub);
  nh.subscribe(motor_sub);
}

void loop() {
  // Read IR sensors (HIGH when beam unbroken, LOW when blocked)
  bool beamAtStart = (digitalRead(IRbeginPin) == LOW);
  bool beamAtEnd   = (digitalRead(IRendPin)   == LOW);

  // Prepare and publish begin sensor state
  ir_begin_msg.data = beamAtStart;
  ir_begin_pub.publish(&ir_begin_msg);

  // Prepare and publish end sensor state
  ir_end_msg.data = beamAtEnd;
  ir_end_pub.publish(&ir_end_msg);

  // Handle ROS callbacks
  nh.spinOnce();
  delay(100);
}
