// Generated by gencpp from file xarm_planner/pose_planRequest.msg
// DO NOT EDIT!


#ifndef XARM_PLANNER_MESSAGE_POSE_PLANREQUEST_H
#define XARM_PLANNER_MESSAGE_POSE_PLANREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Pose.h>

namespace xarm_planner
{
template <class ContainerAllocator>
struct pose_planRequest_
{
  typedef pose_planRequest_<ContainerAllocator> Type;

  pose_planRequest_()
    : target()  {
    }
  pose_planRequest_(const ContainerAllocator& _alloc)
    : target(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _target_type;
  _target_type target;





  typedef boost::shared_ptr< ::xarm_planner::pose_planRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xarm_planner::pose_planRequest_<ContainerAllocator> const> ConstPtr;

}; // struct pose_planRequest_

typedef ::xarm_planner::pose_planRequest_<std::allocator<void> > pose_planRequest;

typedef boost::shared_ptr< ::xarm_planner::pose_planRequest > pose_planRequestPtr;
typedef boost::shared_ptr< ::xarm_planner::pose_planRequest const> pose_planRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xarm_planner::pose_planRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xarm_planner::pose_planRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::xarm_planner::pose_planRequest_<ContainerAllocator1> & lhs, const ::xarm_planner::pose_planRequest_<ContainerAllocator2> & rhs)
{
  return lhs.target == rhs.target;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::xarm_planner::pose_planRequest_<ContainerAllocator1> & lhs, const ::xarm_planner::pose_planRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace xarm_planner

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::xarm_planner::pose_planRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xarm_planner::pose_planRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_planner::pose_planRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_planner::pose_planRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_planner::pose_planRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_planner::pose_planRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xarm_planner::pose_planRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f4b4e41b93b97f9307dacbb0795153e4";
  }

  static const char* value(const ::xarm_planner::pose_planRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf4b4e41b93b97f93ULL;
  static const uint64_t static_value2 = 0x07dacbb0795153e4ULL;
};

template<class ContainerAllocator>
struct DataType< ::xarm_planner::pose_planRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xarm_planner/pose_planRequest";
  }

  static const char* value(const ::xarm_planner::pose_planRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xarm_planner::pose_planRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "geometry_msgs/Pose target\n"
"\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::xarm_planner::pose_planRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xarm_planner::pose_planRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.target);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct pose_planRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xarm_planner::pose_planRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xarm_planner::pose_planRequest_<ContainerAllocator>& v)
  {
    s << indent << "target: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.target);
  }
};

} // namespace message_operations
} // namespace ros

#endif // XARM_PLANNER_MESSAGE_POSE_PLANREQUEST_H
