output "alb_dns_name" {
  value = aws_lb.ecs_alb.dns_name
}

output "flask_ecr_repository_url" {
  value = aws_ecr_repository.flask_backend.repository_url
}

output "express_ecr_repository_url" {
  value = aws_ecr_repository.express_frontend.repository_url
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.main_cluster.name
}
