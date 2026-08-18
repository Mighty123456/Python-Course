output "flask_ecr_url" {
  value = aws_ecr_repository.flask_backend.repository_url
}

output "express_ecr_url" {
  value = aws_ecr_repository.express_frontend.repository_url
}

output "alb_dns_name" {
  value = aws_lb.ecs_alb.dns_name
}
