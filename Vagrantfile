Vagrant.configure("2") do |config|

  config.vm.box_check_update = true
  config.vm.graceful_halt_timeout=15
  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vbguest.auto_update = false
  end
  config.ssh.insert_key = false
  config.ssh.forward_agent = true

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

