server {
    listen 80;
    server_name capability.aroha.co.in;
    rewrite ^ https://capability.aroha.co.in/$1 permanent;
}
server {
    listen 443 ssl;
    #listen 80;
    server_name capability.aroha.co.in;

    #ssl on;
    ssl_certificate /etc/letsencrypt/live/capability.aroha.co.in-0001/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/capability.aroha.co.in-0001/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    access_log /var/log/nginx/capability_ssl.access.log;
    error_log /var/log/nginx/capability_ssl.error.log;
    location / {
        proxy_pass http://ec2-54-148-166-223.us-west-2.compute.amazonaws.com:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        client_max_body_size 100M;
    }
}