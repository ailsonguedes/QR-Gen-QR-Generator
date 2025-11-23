# Usa uma imagem base Node
FROM node:18-alpine as build

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependência
COPY package.json package-lock.json ./

# Instala as dependências
RUN npm install

# Copia o código fonte
COPY . .

# Constrói o aplicativo React (gera a pasta 'dist')
RUN npm run build

# --- Estágio de Serviço (Servir o app construído via Nginx) ---
FROM nginx:alpine

# Remove a configuração padrão do Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copia a saída da construção do React para o diretório de serviço do Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Copia um arquivo de configuração customizado (necessário para roteamento React/Vite)
# Você precisará criar um arquivo 'nginx.conf'
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expõe a porta 80 (padrão do Nginx)
EXPOSE 80

# Comando padrão para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]
