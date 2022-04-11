server {
    listen 80;
    server_name api.productivity.aroha.co.in;
    access_log /var/log/nginx/api_productivity.access.log;
    error_log /var/log/nginx/api_productivity.error.log;
    location / {
        proxy_pass http://ec2-54-148-166-223.us-west-2.compute.amazonaws.com:8047;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        client_max_body_size 100M;
    }


}