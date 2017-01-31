Name     : jdk-datanucleus-rdbms
Version  : 3.2.9
Release  : 5
URL      : https://repo1.maven.org/maven2/org/datanucleus/datanucleus-rdbms/3.2.9/datanucleus-rdbms-3.2.9.jar
Source0  : https://repo1.maven.org/maven2/org/datanucleus/datanucleus-rdbms/3.2.9/datanucleus-rdbms-3.2.9.jar
Source1  : https://repo1.maven.org/maven2/org/datanucleus/datanucleus-rdbms/3.2.9/datanucleus-rdbms-3.2.9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-datanucleus-rdbms-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-datanucleus-rdbms package.
Group: Data

%description data
data components for the jdk-datanucleus-rdbms package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/datanucleus-rdbms.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/datanucleus-rdbms.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/datanucleus-rdbms.xml \
%{buildroot}/usr/share/maven-poms/datanucleus-rdbms.pom \
%{buildroot}/usr/share/java/datanucleus-rdbms.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/datanucleus-rdbms.jar
/usr/share/maven-metadata/datanucleus-rdbms.xml
/usr/share/maven-poms/datanucleus-rdbms.pom
