variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Project name used for tagging resources"
  type        = string
  default     = "college-bus-tracker"
}

variable "instance_type" {
  description = "EC2 instance type (t2.micro is free tier eligible)"
  type        = string
  default     = "t2.micro"
}

variable "public_key_path" {
  description = "Path to your SSH public key file"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}

variable "docker_image" {
  description = "Docker Hub image for bus tracker"
  type        = string
  default     = "yourusername/college-bus-tracker:latest"
}
