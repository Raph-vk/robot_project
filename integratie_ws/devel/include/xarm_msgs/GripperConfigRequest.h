// Generated by gencpp from file xarm_msgs/GripperConfigRequest.msg
// DO NOT EDIT!


#ifndef XARM_MSGS_MESSAGE_GRIPPERCONFIGREQUEST_H
#define XARM_MSGS_MESSAGE_GRIPPERCONFIGREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace xarm_msgs
{
template <class ContainerAllocator>
struct GripperConfigRequest_
{
  typedef GripperConfigRequest_<ContainerAllocator> Type;

  GripperConfigRequest_()
    : pulse_vel(0.0)  {
    }
  GripperConfigRequest_(const ContainerAllocator& _alloc)
    : pulse_vel(0.0)  {
  (void)_alloc;
    }



   typedef float _pulse_vel_type;
  _pulse_vel_type pulse_vel;





  typedef boost::shared_ptr< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> const> ConstPtr;

}; // struct GripperConfigRequest_

typedef ::xarm_msgs::GripperConfigRequest_<std::allocator<void> > GripperConfigRequest;

typedef boost::shared_ptr< ::xarm_msgs::GripperConfigRequest > GripperConfigRequestPtr;
typedef boost::shared_ptr< ::xarm_msgs::GripperConfigRequest const> GripperConfigRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::xarm_msgs::GripperConfigRequest_<ContainerAllocator1> & lhs, const ::xarm_msgs::GripperConfigRequest_<ContainerAllocator2> & rhs)
{
  return lhs.pulse_vel == rhs.pulse_vel;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::xarm_msgs::GripperConfigRequest_<ContainerAllocator1> & lhs, const ::xarm_msgs::GripperConfigRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace xarm_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e393f852f6dfd7f6b04a67b432cce09e";
  }

  static const char* value(const ::xarm_msgs::GripperConfigRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe393f852f6dfd7f6ULL;
  static const uint64_t static_value2 = 0xb04a67b432cce09eULL;
};

template<class ContainerAllocator>
struct DataType< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xarm_msgs/GripperConfigRequest";
  }

  static const char* value(const ::xarm_msgs::GripperConfigRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Grip velocity configuration: range is from 1 to 5000\n"
"float32 pulse_vel\n"
"\n"
;
  }

  static const char* value(const ::xarm_msgs::GripperConfigRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pulse_vel);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GripperConfigRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xarm_msgs::GripperConfigRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xarm_msgs::GripperConfigRequest_<ContainerAllocator>& v)
  {
    s << indent << "pulse_vel: ";
    Printer<float>::stream(s, indent + "  ", v.pulse_vel);
  }
};

} // namespace message_operations
} // namespace ros

#endif // XARM_MSGS_MESSAGE_GRIPPERCONFIGREQUEST_H
