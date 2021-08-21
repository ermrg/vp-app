# The first stage
# Build React static files
FROM node:13.12.0-alpine as build

WORKDIR /app/pwaap
COPY ./app/package.json ./
COPY ./app/package-lock.json ./
RUN npm ci --silent
COPY ./app/ ./
RUN npm run build

# The second stage
# Copy React static files and start nginx
FROM nginx:stable-alpine
COPY --from=build /app/pwaap/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]