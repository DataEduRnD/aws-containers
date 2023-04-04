FROM nginx:latest
COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
EXPOSE 7070

# nginx 컨테이너만 단독 실행 시에는 코멘트 해제
# CMD ["nginx", "-g", "daemon off;"]  

# docker build --no-cache -t nginx ./nginx ; 이미지 빌드
# docker run -p 80:80 -p 7070:7070 nginx ; 컨테이너 시작