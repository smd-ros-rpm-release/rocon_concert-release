Name:           ros-indigo-concert-service-manager
Version:        0.6.1
Release:        0%{?dist}
Summary:        ROS concert_service_manager package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/concert_service_manager
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-concert-msgs
Requires:       ros-indigo-genpy
Requires:       ros-indigo-rocon-console
Requires:       ros-indigo-rocon-interactions
Requires:       ros-indigo-rocon-python-utils
Requires:       ros-indigo-roslaunch
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-unique-id
BuildRequires:  ros-indigo-catkin

%description
Component responsible for launching and managing concert services.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Nov 21 2014 Daniel Stonier <d.stonier@gmail.com> - 0.6.1-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.6.0-0
- Autogenerated by Bloom

