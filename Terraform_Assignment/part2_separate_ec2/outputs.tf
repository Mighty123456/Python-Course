output "backend_ec2_public_ip" {
  value = aws_instance.backend_ec2.public_ip
}

output "frontend_ec2_public_ip" {
  value = aws_instance.frontend_ec2.public_ip
}

output "frontend_app_url" {
  value = "http://${aws_instance.frontend_ec2.public_ip}:3000"
}

output "backend_api_url" {
  value = "http://${aws_instance.backend_ec2.public_ip}:5000/api/data"
}
