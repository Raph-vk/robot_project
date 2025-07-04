// Generated by gencpp from file robotarm/manipulatorGoal.msg
// DO NOT EDIT!


#ifndef ROBOTARM_MESSAGE_MANIPULATORGOAL_H
#define ROBOTARM_MESSAGE_MANIPULATORGOAL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robotarm
{
template <class ContainerAllocator>
struct manipulatorGoal_
{
  typedef manipulatorGoal_<ContainerAllocator> Type;

  manipulatorGoal_()
    : manipulator_start(false)  {
    }
  manipulatorGoal_(const ContainerAllocator& _alloc)
    : manipulator_start(false)  {
  (void)_alloc;
    }



   typedef uint8_t _manipulator_start_type;
  _manipulator_start_type manipulator_start;





  typedef boost::shared_ptr< ::robotarm::manipulatorGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robotarm::manipulatorGoal_<ContainerAllocator> const> ConstPtr;

}; // struct manipulatorGoal_

typedef ::robotarm::manipulatorGoal_<std::allocator<void> > manipulatorGoal;

typedef boost::shared_ptr< ::robotarm::manipulatorGoal > manipulatorGoalPtr;
typedef boost::shared_ptr< ::robotarm::manipulatorGoal const> manipulatorGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robotarm::manipulatorGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robotarm::manipulatorGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::robotarm::manipulatorGoal_<ContainerAllocator1> & lhs, const ::robotarm::manipulatorGoal_<ContainerAllocator2> & rhs)
{
  return lhs.manipulator_start == rhs.manipulator_start;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::robotarm::manipulatorGoal_<ContainerAllocator1> & lhs, const ::robotarm::manipulatorGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace robotarm

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::robotarm::manipulatorGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robotarm::manipulatorGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotarm::manipulatorGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotarm::manipulatorGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotarm::manipulatorGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotarm::manipulatorGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robotarm::manipulatorGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3868a330ea8e060554882c30a838b6a7";
  }

  static const char* value(const ::robotarm::manipulatorGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3868a330ea8e0605ULL;
  static const uint64_t static_value2 = 0x54882c30a838b6a7ULL;
};

template<class ContainerAllocator>
struct DataType< ::robotarm::manipulatorGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robotarm/manipulatorGoal";
  }

  static const char* value(const ::robotarm::manipulatorGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robotarm::manipulatorGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Goal\n"
"bool manipulator_start\n"
;
  }

  static const char* value(const ::robotarm::manipulatorGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robotarm::manipulatorGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.manipulator_start);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct manipulatorGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robotarm::manipulatorGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robotarm::manipulatorGoal_<ContainerAllocator>& v)
  {
    s << indent << "manipulator_start: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.manipulator_start);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOTARM_MESSAGE_MANIPULATORGOAL_H
