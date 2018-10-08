Vagrant.configure("2") do |config|

  config.vm.define "controlnode" do |web|
    web.vm.box = "fedora/28-cloud-base"
  end

  config.vm.define "managednode" do |db|
    db.vm.box = "fedora/28-cloud-base"
  end
end

