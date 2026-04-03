output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.bus_tracker_server.public_ip
}

output "instance_public_dns" {
  description = "Public DNS of the EC2 instance"
  value       = aws_instance.bus_tracker_server.public_dns
}

output "app_url" {
  description = "URL to access the Bus Tracker app"
  value       = "http://${aws_instance.bus_tracker_server.public_ip}:5000"
}

output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.bus_tracker_vpc.id
}

output "ssh_command" {
  description = "SSH command to connect to the server"
  value       = "ssh -i ~/.ssh/id_rsa ubuntu@${aws_instance.bus_tracker_server.public_ip}"
}
