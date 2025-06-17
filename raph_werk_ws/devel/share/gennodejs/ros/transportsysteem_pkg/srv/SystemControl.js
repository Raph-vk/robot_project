// Auto-generated. Do not edit!

// (in-package transportsysteem_pkg.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class SystemControlRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.instruction = null;
    }
    else {
      if (initObj.hasOwnProperty('instruction')) {
        this.instruction = initObj.instruction
      }
      else {
        this.instruction = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SystemControlRequest
    // Serialize message field [instruction]
    bufferOffset = _serializer.string(obj.instruction, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SystemControlRequest
    let len;
    let data = new SystemControlRequest(null);
    // Deserialize message field [instruction]
    data.instruction = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.instruction.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'transportsysteem_pkg/SystemControlRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4251c9c3720afa4138d846da006deeed';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Request: The state the system should go to ("start", "dump")
    string instruction
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SystemControlRequest(null);
    if (msg.instruction !== undefined) {
      resolved.instruction = msg.instruction;
    }
    else {
      resolved.instruction = ''
    }

    return resolved;
    }
};

class SystemControlResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.result = null;
    }
    else {
      if (initObj.hasOwnProperty('result')) {
        this.result = initObj.result
      }
      else {
        this.result = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SystemControlResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SystemControlResponse
    let len;
    let data = new SystemControlResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'transportsysteem_pkg/SystemControlResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'eb13ac1f1354ccecb7941ee8fa2192e8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Response: Whether the state transition was successfully executed
    bool result
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SystemControlResponse(null);
    if (msg.result !== undefined) {
      resolved.result = msg.result;
    }
    else {
      resolved.result = false
    }

    return resolved;
    }
};

module.exports = {
  Request: SystemControlRequest,
  Response: SystemControlResponse,
  md5sum() { return 'acc3bbca6f8e73aa0ef1136aa9bdba5b'; },
  datatype() { return 'transportsysteem_pkg/SystemControl'; }
};
