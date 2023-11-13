#!/bin/bash
set -e
chown -R www-data:www-data /var/www/html
php /install.php &
exec apache2-foreground
