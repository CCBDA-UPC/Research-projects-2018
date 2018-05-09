
# Vagrant #
## Introduction to Vagrant ##

Today\`s IT enterprise is always looking for the latest technology that allow businesses to run with fewer resources and to use them in efficient way while providing the infrastructure to meet customer needs. The growing awareness of the advantages provided by virtualization technology has turned it in one of the most important issue of the computing industry. However, working with virtual development environments require a lot of manual work and configurations and today's modern applications have a lot of moving parts, technologies to choose from and a lot more overall complexity. Hence, **automation tools** like Vagrant have gained quite wide popularity and have outclassed the traditional approaches.

Vagrant is a set of tools that attempts to make it easier to build and manage virtual machines through a simple and uniform command-line interface. Furthermore, Vagrant facilitates sharing and distributing virtual development environments between teams and people working on different platforms. Specifically, it helps to create and configure lightweight, reproducible and portable deployment environment. It was originally authored by Mitchell Hashimoto and it is an open source software distributed under an MIT license. The source code of Vagrant is available at https://github.com/mitchellh/vagrant.

Apart from the virtualization solution, the programming language, the framework and the operating system used, Vagrant creates the complete deployment environment with just one simple command: $ vagrant up.  Vagrant is a Swiss Army knife for development environments. It automates all the necessary tasks to run the virtual development environment, from downloading, installing and booting the VM (it supports all major virtual solutions: VirtualBox, VMWare, and Hyper-V) to configuring various resources (RAM, CPUs, network connections and shared folders) and installing additional software within the VM by using software configuration tools such as Ansible, Chef, Puppet, and Salt.

Prior to Vagrant, the preferred method of working on a web application was to install and configure all the needed software locally on the development machine. Everything must be installed manually by the developers and once the software is installed it has to be configured manually as well. Manual setup of development environment can lead to a difference between development and production as there might be functionalities that works in development but doesn't work the same in production. It is also easy for the development environments to get out of sync, as each developer is responsible for managing its own environment. This creates difficulties in keeping the environment in sync with other team members and especially it creates confusion for new team members. Furthermore in the traditional approach it is difficult to manage multiple projects, as each project requires different configuration of their services and usually the developers end up having a system with poorly configured dependencies or a system that is running a lot of services that individual applications may not need. 

In a world with Vagrant, although the application is executed in the developer’s machine, they are no longer responsible for the installation of the server-side software. The developers can simply run vagrant up and have a fully running development environment up and ready in one or two minutes. Even though this time depends on many factors, Vagrant dramatically reduces the amount of time needed to rebuild the development environment. System engineers are responsible for preparing and configuring server-side software, whereas the developers simply use the prefabricated VMs that they may treat as a black box. As Vagrant behaves identically across different operating systems (Linux, Mac OS and Windows), the developers can work on the operating system they feel more productive on. It is also easier to work with a team as the VM images can be shared without efforts. Furthermore, working with multiple projects is also facilitated because each project has it own virtual machine. Moreover Vagrant\`s features can be extended with plug-ins if it is necessary and if there is something Vagrant cannot do with the development environment.

In summary, as a layer on top of existing and well-known virtualization solutions, Vagrant is a useful tool to manage the complexity of virtual machines. Although it is possible to achieve what Vagrant does with only plain desktop virtualization, there is a major downside of this approach: it would be completely manual. 


## Configuring the development environment ##

In this section we will describe how to set up and initialize the development environment for a single Vagrant virtual machine. We will also briefly explain the main Vagrant components.

### Setting up the development environment ###

Setting up a working environment is the most important step before using Vagrant. Despite the operating system used, to start exploring Vagrant, it is needed to install a provider software and the Vagrant software itself.

Firstly, it is necessary to install the software to manage the VM environment (hypervisor/ provider). The providers are the “back end of Vagrant”. Vagrant  does not provide any virtualization functionality itself but it sits on top of existing virtualization solutions. Initially, the only hypervisor supported by Vagrant was VirtualBox. Nowadays, they also offer support for other hypervisors like VMware Fusion, Hyper-V and vCloud Air, but Vagrant community is still broadly supporting VirtualBox (https://www.virtualbox.org) as an open source and freely available provider. In addition Vagrant offer an official VMware provider(https://www.vagrantup.com/vmware/). The choice of provider is very important when working with Vagrant because errors encounters when using Vagrant environment are not only related to Vagrant itself but also to the provider application. After deciding which provider to use, they can be downloaded at their corresponding official website and installed depending on the operating system. 

The next step is installing Vagrant software itself. After selecting the appropriate version for your operating system, a copy of the latest version of the Vagrant installer can be downloaded from the Vagrant website (https://www.vagrantup.com/downloads.html).  

To set up the environment in Ubuntu Linux Environment, using VirtualBox provider the following steps should be followed:
```
sudo apt-get install virtualbox
sudo apt-get install vagrant
```
### Vagrant components ###

Once we have a working environment, we can start using Vagrant. But before starting exploring it, it is reasonable to briefly introduce the main components of Vagrant: providers, Vagrantfile, boxes and plugins. We described providers shortly in the previous section.

**VagrantFile** is a special file that contains the information that Vagrant requires to create the environment. The instructions  are expressed in Vagrant\`s DSL (Ruby) and they define how the development environment would look like. A powerful technique to manage and track changes in Vagrant environment is to keep Vagrantfiles and projects in a source control system (e.g. Git, SVN).  By using these source code repositories, the modification of the projects  will be less risky and the sharing of Vagrant projects will be much simpler.   

**Boxes** are precreated base image of operating system that are used by Vagrant to build the development environment and to run provisioning on top of it. To avoid building a virtual machine from scratch (time-consuming and resource-intensive) Vagrant use the predefined base image and clones it, to rapidly create a usable machine. These snapshotted base images can help for optimization process; several base applications can be pre installed in image so that we can minimize the provisioning process in Vagrant. Vagrant saves the downloaded box file for future usage to avoid downloading them again as they are quite large due to already-installed operating systems that they contain. When we configure Vagrantfile, we have to define the box that we are going to use, as illustrated in the end of this subsection. If the box specified on Vagrantfile could not be found during the runtime, Vagrant will automatically download the required box. Other approach would be to add Vagrant box manually before running `Vagrant up` command. This can be done by executing: 
```
vagrant box add <box-address>
```
Box address is referring either to one of these three: 
* A shorthand name of public catalog of available Vagrant images, for example: "hashicorp/precise64".
* A URL to a box in a catalog. 
* Direct URL to a box file.

Another approach would be adding the shorthand name of public catalog of available Vagrant images in Vagrantfile as specified on `config.vm.box` parameter shown below:
```
config.vm.box = "hashicorp/precise64"
```
We will see this part in details in the following subsection, when trying to launch our first Vagrantfile configuration. 

**Plugin** is used to designate new commands and configurations in Vagrantfile, that will extend the feature and functionality of the use case. For instance, Vagrant was not built to specialize in cloud architecture, especially with huge amount of cloud providers nowadays. With the existence of Vagrant plugins, we can remotely manage our architecture and configuration in cloud using Vagrantfile integrated with cloud service provider. There are also another use case of plugin development such as networking, provisioning, and some other items that can be seen at https://github.com/hashicorp/vagrant/wiki/Available-Vagrant-Plugins.

There are two ways to install vagrant plugin, first one is installing Vagrant plugin from a known gem source and the second one is installing Vagrant plugin from our local file source. For the first one, user can just specify the plugin name on the last parameter of Vagrant command execution, while for the second, user need to define the path for .gem file residing on the local file system. Shell commands for both can be seen as follow.
```
# use plugin name
vagrant plugin install plugin-name
```
```
# use local .gem file
vagrant plugin install /path/to/my-plugin.gem
```
This elasticity allows Vagrant to adapt with current trends in software development automation process easily. We will discuss more about cloud service provider plugins, specifically for Amazon Web Services (AWS) in the third section to see the actual implementation of having Vagrant on the cloud.

### Initializing the development environment ###

Running Vagrant is quite simple. First, by using Vagrant version command, we can verify that Vagrant is successfully installed and can continue with initializing the development environment and interacting with it. In Ubuntu Linux Environment, the following commands should be executed:
```
vagrant init precise64 http://files.vagrantup.com/precise64.box
vagrant up
```
The first command informs the user that a new Vagrantfile is created in the current directory.  Up to this point Vagrant environment is provisioned using a single box, but to use different operating systems and operating environment, the user need to obtain different Vagrant boxes. VagrantCloud (https://app.vagrantup.com/boxes/search) can be used to find Vagrant boxes. The output of the first command indicates that we are ready to run the second: `vagrant up`.  Some of the most important results outputted by the second command are: a status message showing that the default machine is being started with the provider chosen, a message indicating the forwarding ports, shared folders and networking (after the box file is downloaded and started). 

After these two commands finish running, a fully featured virtual machine will be running in the background. The user can execute `vagrant ssh` to access this machine. A command-line interface will be opened in the new virtual machine and the user can make all the modification that he/she wants: from creating files to installing programs. Once finished with the environment, the user can decide to stop the machine and keep the environment available for later use by executing `vagrant halt` or can decide to destroy the machine and discard the entire working environment by executing `vagrant destroy`.

The initial Vagrantfile contains only basic configuration related with the Vagrant environment itself and the box that serves as the base template of the environment.  The basic unit of a Vagrantfile is a configuration object, which represents a virtual machine. Therefore, the operations added on the configuration will define the operation of the machine. The first line starts a block of Vagrant configuration and each Vagrantfile requires at least one configuration.  The second line defines the box that we are going to use.

```
# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
End
```
There are also two more important elements that should be taken into consideration when working with Vagrant machines: **sharing the files** with the machine and **communicating with the machine over the network**. 

To ensure synchronization between the virtual machine and the host machine, Vagrant supports setting up **shared folders**. Having a shared file system enable developers edit files using their own editor on the host machine and have everything automatically synchronized in the virtual development environment. This filesystem also give them a place to store files that will not be destroyed from `vagrant destroy` and will be available the next time a machine is created using `vagrant up`. By default, Vagrant shares the project directory (the directory where Vagrantfile is) of the host machine with the /vagrant directory inside the virtual machine. By using `config.vm.share_folder` directive in Vagrantfile we can overwrite the location of the default share folder. The configuration below, shows that the virtual machine will have `/data` directory synced with `./data`   directory on the host machine. 

```
Vagrant.configure(2) do |config|
  ...
  config.vm.share_folder "data", "/data", "./data"
End
```
In the same way, Vagrant automatically configures different options for **communicating with the virtual machine**. This is especially important for web projects, because while the project code and all of its dependencies run isolated within the virtual machine, the developers can continue using their own browsers and development tools to access their project. There exist a large number of ways this communication can be configured and in this report we will only go through **forwarded ports**. By using `config.vm.forward_port` directive in Vagrantfile we can forward port 80 on the virtual machine to port 8080 on the host machine. 

```
Vagrant.configure(2) do |config|
  ...
  config.vm.forward_port 80, 8080
End
```

To sum up, Vagrant has a very simple workflow. By just using `vagrant up`, `vagrant ssh`, `vagrant destroy`, users can simply manage their development environments. Moreover, even though the syntax of Vagrantfile is in Ruby, no Ruby-specific knowledge is necessary since the Vagrantfile is composed only of variable assignment, function calls and configuration blocks. In addition,  shared folders and forwarded ports enables developers to continue using the development tools they are more comfortable and efficient with.

## Provisioning Vagrant environment ##

In order for a developer to have a complete development environment, all the necessary software for the project being developed must be installed on the virtual machine. Vagrants enables automatic installation of the software as part as the development environment creation process.  The real power of Vagrant is not only speeding up the creation of development environments from a Vagrantfile, but also provisioning these environments in a repeatable way. Provisioner is a term that is used to refer to different methods that Vagrant use to install and configure software. Vagrant supports automated provisioning, ensuring in this way environment stability and saving time by automating this process through shell scripts and configuration management.  

Using automated provisioning offered by Vagrant, a set of problems related with setting up development environments manually can be avoided. In practice, when a new server must be configured even the same configuration guides are followed (giant Readme files with steps for each platform), the server might end up slightly different and these differences can lead to a lot of issues and to developers claiming “but it worked on my machine”. Automated provisioning ensures development environments to be identically configured and have identically installed softwares. The more team members use Vagrant, the more quickly these benefits are realized. 

In this section we will go through Vagrant provisioning, using both shell scripts and configuration management tools.

### Basic provisioning with Vagrant using shell scripts ###

The basic method of provisioning is to use shell commands and run them in the Vagrant machine. Depending on the complexity of the task the user can choose between running simple shell commands, executing shell scripts in a Vagrantfile and provisioning with external shell script. 

For very basic provisioning (e.g. displaying a message to users on login), the user can directly add a command to be executed using the provisioning command in Vagrantfile, which will take two arguments: the type of provisioner being executed (in this case shell) and the command to be executed by the shell with the inline argument. After the environment is started with `vagrant up` command and after the virtual environment is accessed using the `vagrant ssh` command, the message will be displayed for the user.  Furthermore, by using vagrant provision command, Vagrant allows provisioners to be executed multiple times on an environment.

```
# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.provision "shell",
     inline: "echo 'Vagrant Cookbook Example Environment' > /etc/motd"
End
```

To deal with more complicated tasks, instead of using single inline string arguments, the users can define shell scripts (set of commands) in the Vagrantfile, using the multiline string feature of Ruby. E.g. provisioning a new Vagrant environment, by installing *nginx web server* and replacing the default web directory.  In this example we can see that Vagrant can also be used to extend the utility of local computing environments, for instance enabling a virtual machine to listen on local ports through port forwarding. After modifying the Vagrantfile as shown below, we can open the browser and visit http://localhost:8080 in the host machine and access the newly installed web server.

```
# -*- mode: ruby -*-
# vi: set ft=ruby :
$nginx_install = <<SCRIPT
if [ ! -x /usr/sbin/nginx ]; then
apt-get install -y nginx;
Fi

# Default NGINX directory: /usr/share/nginx/html
# Replace this with symbolic link to vagrant directory.
if [ ! -L /usr/share/nginx/html ]; then
rm -rf /usr/share/nginx/html
ln -s /vagrant/html /usr/share/nginx/html
fi
SCRIPT
Vagrant.configure(2) do |config|
config.vm.box = "precise64"
  	config.vm.box_url = "http://files.vagrantup.com/precise64.box"
config.vm.provision "shell", inline: $nginx_install
config.vm.network "forwarded_port", guest:80, host:8080
end
```

In the case when provisioning operations are large and very complex, it is recommended to create and maintain them separately from the Vagrantfile. In this case we need to configure vagrant to use the script, by using `config.vm.provision` directive. For the same example as above, in this case the content of Vagrantfile will be:

```
# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
config.vm.box = "precise64"
  	config.vm.box_url = "http://files.vagrantup.com/precise64.box"
     config.vm.provision "shell", path: "nginx-install.sh"
     config.vm.network "forwarded_port", guest:80, host:8080
end
```
Figure below shows setting up the development environment in our local machine

![alt text](https://github.com/ferdidolot/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/vagrant-local-1.PNG)

### Provisioning using configuration management tool ###

In  the previous section, we have seen that Vagrant can take benefit of basic provisioning that is mostly part of the operating system, such as shell command. Going over shell command can somehow be very complicated since we have to create a proper scripting and programming to ensure everything works perfectly. We also have to maintain our script (doing proper test of the configuration script itself) in the case of project expansion and change of deployment process. 

Additionally, configuration management tool, however, provides simplicity on doing machine configuration task. By using it, we can minimize our effort of doing proper shell scripting and programming, and use well developed tool to provision our machine better. There are a lot of available configuration management tool among which the most popular are: Puppet, Chef, Salt and Ansible. This flexibility of Vagrant makes this tool easily to adjust with automation growth in software industry.

To illustrate this, we will shortly see one example on how to integrate Vagrant with Ansible. Firstly, user should have Ansible installed on the Vagrant host machine. This is a very basic requirement since Vagrant need to run Ansible inside of the Vagrantfile. In this section, we will not talk about details for Ansible installation, but it can be found at http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html. 

Secondly, user needs to define associated Ansible playbook provisioning script inside of Vagrantfile. Example is shown below:

```
Vagrant.configure("2") do |config|
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end
```

This way, we can put Ansible script on the same version control as Vagrant and run them together to provide powerful integration between each component. Vagrant can be used to specifically build architecture environment such as virtual machines and cloud instances, meanwhile Ansible can be used for provisioning tools.

We can take benefit of Vagrant posistioning by choosing between basic one with shell script and provisioning with configuration management tools.


## Vagrant in cloud ##

Vagrant can be used with cloud providers to automatically manage architecture and configuration in cloud. This flexibility can be achieved by developing plugin in Vagrant for the cloud provider. One of the most popular cloud provider that support this capability is Amazon Web Services (AWS) and some other cloud providers are: AWS, Azure, Google, Hp, Digitalocean, Cloudstack. 

In this section, we will be focusing on how we can make use of Vagrant in AWS cloud service environment. It is important to highlight that in this report, we will not be covering the basic configuration of AWS instance. We are assuming that the reader is familiar with AWS configuration and terminology hence it is advised for the reader to explore about AWS feature and console in order to proceed in this section. Some useful information regarding AWS can be found on https://aws.amazon.com/getting-started/. 

### Vagrant in AWS ###

From previous section, we already saw an example of Vagrant managing virtual environment using virtualbox, while in AWS cloud,Vagrant will be managing virtual machines as instances running in AWS. Vagrant will provide easy access to AWS instances creation and termination, as well as AWS instances provisioning and configuration. 

First, we will need to add dummy box to be installed for AWS by running this command: 
```
vagrant box add <box-name> https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box
```

In order to be able to use AWS in Vagrant, it is necessary to install AWS plugin in Vagrant. To install AWS plugin, simply run
```
vagrant plugin install vagrant-aws
```

During our experiment, we had difficulties when installing Vagrant on Ubuntu 16.04 environment. The reader is advised to go to `Vagrant plugin installation issues` section to see Vagrant plugin installation issue and how to fix it.

The next step is to create Vagrantfile containing information about AWS instances. Example of Vagrantfile can be seen as follow: 
```
Vagrant.configure("2") do |config|
  config.vm.box = "dummy"

  config.vm.provider :aws do |aws, override|
    aws.access_key_id = "YOUR KEY"
    aws.secret_access_key = "YOUR SECRET KEY"
    aws.keypair_name = "KEYPAIR NAME"

    aws.ami = "ami-7747d01e"

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "PATH TO YOUR PRIVATE KEY"
  end
end
```

There are several AWS parameters that are normally defined in Vagrantfile, such as:
* access_key_id:  Your AWS access key 
* secret_access_key: Your AWS access key 
* keypair_name: The name of the keypair to be used in AWS.
* ami: The AMI id to boot. We can find this information in AWS AMI section. 
* username: Your virtual machine/instance username, and also path to your private key
* security_group: list of AWS security group for running this instance. Information about security group can be found on https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html. 
* Instances_type: AWS instance type tier such as micro, macro, medium, etc. 

Complete configuration can be seen on https://github.com/mitchellh/vagrant-aws. AWS Vagrant plugin then pass this information to AWS, the same as we are opening AWS web console, and creates the VM accordingly to the information we set. 


The figures below shows setting up the development environment in our AWS.

![alt text](https://github.com/ferdidolot/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/vagrant-aws-1.PNG)

![alt text](https://github.com/ferdidolot/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/vagrant-aws-2.PNG)

The figures below shows the EC2 web management console.

![alt text](https://github.com/ferdidolot/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/vagrant-aws-3.PNG)

### Vagrant AWS plugin installation issues ###

**Trigger**: after executing command
```
vagrant plugin install vagrant-aws
```

**Error message**: 
```
/usr/lib/ruby/2.3.0/rubygems/specification.rb:946:in \`all=': undefined method \`group_by\' for nil:NilClass (NoMethodError)
```

**Fix**: create file `vagrant-plugin.patch` with the following contents:
```
---
 lib/vagrant/bundler.rb | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

diff --git a/lib/vagrant/bundler.rb b/lib/vagrant/bundler.rb
index 5a5c185..c4a3837 100644
--- a/lib/vagrant/bundler.rb
+++ b/lib/vagrant/bundler.rb
@@ -272,7 +272,6 @@ module Vagrant

   	# Reset the all specs override that Bundler does
   	old_all = Gem::Specification._all
-  	Gem::Specification.all = nil

   	# /etc/gemrc and so on.
   	old_config = nil
@@ -286,6 +285,8 @@ module Vagrant
   	end
   	Gem.configuration = NilGemConfig.new

+  	Gem::Specification.reset
+
   	# Use a silent UI so that we have no output
   	Gem::DefaultUserInteraction.use_ui(Gem::SilentUI.new) do
 	return yield
  ```
**Apply patch** 

```
sudo patch --directory /usr/lib/ruby/vendor_ruby/vagrant < vagrant-plugin.patch
```
We have seen that Vagrant can also be used in AWS environment and will provide easier configuration management to our cloud environment. We can also apply the same method for other cloud providers.

## References ##

[Vagrant's documentation site](https://www.vagrantup.com/docs/)

[Vagrant community](https://www.vagrantup.com/community.html)

[Vagrant Virtual Development Environment Cookbook](http://1.droppdf.com/files/n9TVZ/vagrant-virtual-development-environment-cookbook-by-chad-thompson.pdf)

[Vagrant: Up and Running](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwiX9eiPmfbaAhUmh6YKHUCSA18QFggoMAA&url=https%3A%2F%2Fisidore.co%2Fcalibre%2Fget%2Fpdf%2F5829&usg=AOvVaw23jSL6pU_Ik2iGUIhTphlf)

[Pro-Vagrant](http://pepa.holla.cz/wp-content/uploads/2016/10/Pro-Vagrant.pdf)

[Vagrant AWS plugin installation issue's solution](https://stackoverflow.com/questions/36811863/cant-install-vagrant-plugins-in-ubuntu/36991648)

## To learn more ##

[Running multiple instances on AWS](http://blog.wimwauters.com/vagrant-aws-launch-multiple-instances/)

[Vagrant in google cloud environment](https://github.com/mitchellh/vagrant-google) 

[Vagrant AWS Lambda](https://mblum.me/2016/07/deploying-aws-lambda-functions/)

[Vagrant plugin development](https://www.slideshare.net/ru_Parallels/vagrant-plugin-development)

