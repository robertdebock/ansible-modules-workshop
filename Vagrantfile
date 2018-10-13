Vagrant.configure("2") do |config|

  # Install required plugins
  required_plugins = %w( vagrant-hostmanager )
  plugin_installed = false
  required_plugins.each do |plugin|
    unless Vagrant.has_plugin?(plugin)
      system "vagrant plugin install #{plugin}"
      plugin_installed = true
    end
  end

  # If new plugins installed, restart Vagrant process
  if plugin_installed === true
    exec "vagrant #{ARGV.join' '}"
  end
  config.vm.box_check_update = true
  config.vm.graceful_halt_timeout=15
  config.vbguest.auto_update = false
  config.ssh.insert_key = false
  config.ssh.forward_agent = true
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = false
  config.hostmanager.manage_guest = true
  config.hostmanager.ignore_private_ip = false
  config.hostmanager.include_offline = true

  config.vm.define "controlnode", primary: true do |web|
    web.vm.box = "fedora/28-cloud-base"
    web.vm.synced_folder ".", "/vagrant", type: "nfs"
    web.vm.network "private_network", ip: "192.168.22.4", :netmask => "255.255.255.0",  auto_config: true
    web.vm.provider :virtualbox do |vb|
      vb.customize [
          "modifyvm", :id,
          "--name", "controlnode",
      ]
    end
    web.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.galaxy_role_file = "roles/requirements.yml"
    ansible.galaxy_roles_path = "roles"
    ansible.playbook = "prepare.yml"
    ansible.verbose = "vv"
    end
  end

  config.vm.define "managednode" do |db|
    db.vm.box = "fedora/28-cloud-base"
    db.vm.synced_folder ".", "/vagrant", disabled: true
    db.vm.network "private_network", ip: "192.168.22.5", :netmask => "255.255.255.0",  auto_config: true
    db.vm.provider :virtualbox do |vb|
      vb.customize [
          "modifyvm", :id,
          "--name", "managednode",
      ]
    end
  end
end

