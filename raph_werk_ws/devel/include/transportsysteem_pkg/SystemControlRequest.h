// Generated by gencpp from file transportsysteem_pkg/SystemControlRequest.msg
// DO NOT EDIT!


#ifndef TRANSPORTSYSTEEM_PKG_MESSAGE_SYSTEMCONTROLREQUEST_H
#define TRANSPORTSYSTEEM_PKG_MESSAGE_SYSTEMCONTROLREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace transportsysteem_pkg
{
template <class ContainerAllocator>
struct SystemControlRequest_
{
  typedef SystemControlRequest_<ContainerAllocator> Type;

  SystemControlRequest_()
    : instruction()  {
    }
  SystemControlRequest_(const ContainerAllocator& _alloc)
    : instruction(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _instruction_type;
  _instruction_type instruction;





  typedef boost::shared_ptr< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SystemControlRequest_

typedef ::transportsysteem_pkg::SystemControlRequest_<std::allocator<void> > SystemControlRequest;

typedef boost::shared_ptr< ::transportsysteem_pkg::SystemControlRequest > SystemControlRequestPtr;
typedef boost::shared_ptr< ::transportsysteem_pkg::SystemControlRequest const> SystemControlRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator1> & lhs, const ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator2> & rhs)
{
  return lhs.instruction == rhs.instruction;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator1> & lhs, const ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace transportsysteem_pkg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4251c9c3720afa4138d846da006deeed";
  }

  static const char* value(const ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4251c9c3720afa41ULL;
  static const uint64_t static_value2 = 0x38d846da006deeedULL;
};

template<class ContainerAllocator>
struct DataType< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "transportsysteem_pkg/SystemControlRequest";
  }

  static const char* value(const ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Request: The state the system should go to (\"start\", \"dump\")\n"
"string instruction\n"
;
  }

  static const char* value(const ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.instruction);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SystemControlRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::transportsysteem_pkg::SystemControlRequest_<ContainerAllocator>& v)
  {
    s << indent << "instruction: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.instruction);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TRANSPORTSYSTEEM_PKG_MESSAGE_SYSTEMCONTROLREQUEST_H
