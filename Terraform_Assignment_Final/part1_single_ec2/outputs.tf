output "ec2_public_ip" {
  value = aws_instance.single_ec2.public_ip
}

output "frontend_url" {
  value = "http://${aws_instance.single_ec2.public_ip}:3000"
}

output "backend_api_url" {
  value = "http://${aws_instance.single_ec2.public_ip}:5000/api/data"
}
