// src/hooks/useTheme.ts
import { useState, useEffect } from 'react';

// Define os valores possíveis do tema
type Theme = 'dark' | 'light';

export function useTheme() {
  
  // 1. Tenta ler o tema do localStorage, ou usa 'dark' como padrão
  const getInitialTheme = (): Theme => {
    if (typeof window !== 'undefined') {
      const savedTheme = window.localStorage.getItem('theme');
      
      // LÓGICA ATUALIZADA: 
      // Se um tema foi salvo, usa ele. Caso contrário, retorna 'dark'.
      return (savedTheme === 'dark' || savedTheme === 'light') ? savedTheme : 'dark';
    }
    // Retorna 'dark' para o contexto de Server-Side Rendering (SSR) também
    return 'dark'; 
  };

  // O estado inicial agora carrega 'dark' se não houver preferência
  const [theme, setTheme] = useState<Theme>(getInitialTheme());

  // Função para alternar o tema (mantida)
  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  // Efeito que aplica a mudança (no <html> e no localStorage) (mantido)
  useEffect(() => {
    const htmlElement = document.documentElement;
    
    // Remove a classe/atributo anterior
    htmlElement.removeAttribute('data-theme');

    // Adiciona o novo
    if (theme === 'dark') {
      htmlElement.setAttribute('data-theme', 'dark');
      window.localStorage.setItem('theme', 'dark');
    } else {
      // Quando o tema é 'light', ainda salvamos para o localStorage
      htmlElement.setAttribute('data-theme', 'light');
      window.localStorage.setItem('theme', 'light');
    }
  }, [theme]); // Roda sempre que o 'theme' mudar

  return { theme, toggleTheme };
}