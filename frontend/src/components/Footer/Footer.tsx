import { useEffect, useState } from 'react';

import { useTheme } from '../../hooks/useTheme'; // <-- Ajuste o caminho se necessário
import styles from './Footer.module.css'

const GITHUB_ICON_URL = "https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/github.svg";
const MAIL_ICON_URL = "https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/mail.svg";
const API_ICON_URL = "https://cdn.jsdelivr.net/npm/lucide-static@0.554.0/icons/arrow-up-right-from-square.svg"
const MOON_ICON_URL = "https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/moon.svg";
const SUN_ICON_URL = "https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/sun.svg";

export function Footer(){
    const {theme, toggleTheme} = useTheme();
    const [isIconAnimating, setIsIconAnimating] = useState(false);

    const handleToggleTheme = () => {
        toggleTheme();
        setIsIconAnimating(true);
    };

    useEffect(() => {
        if (!isIconAnimating){
            return;
        }

        const timeoutId = window.setTimeout(() => {
            setIsIconAnimating(false);
        }, 400);

        return() => window.clearTimeout(timeoutId);
    }, [isIconAnimating]);

    return (
        <footer className={styles.footerContainer}>
        <div className={styles.footerLeftContainer}>
          <p className={styles.textLeftFooter}>&copy; 2025 QR Gen - QR Generator. Todos os direitos reservados.</p>
        </div>

        <div className={styles.footerRightContainer}>
            <button className={styles.footerRightButtonThemeToggle} 
                    onClick={handleToggleTheme}
                    title='Alterar tema'>
                {theme === 'light' ? (
                    <img className={`${styles.footerRightIcon} ${isIconAnimating} ${styles.themeIconSlide}`} 
                        key='sun'
                        src={SUN_ICON_URL} 
                        alt="tema claro"
                        onAnimationEnd={() => setIsIconAnimating(false)}
                        width="20" height="20"/>
                ) : (
                    <img className={`${styles.footerRightIcon} ${isIconAnimating} ${styles.themeIconSlide}`} 
                     key='moon'
                     src={MOON_ICON_URL} 
                     alt="tema escuro"
                     onAnimationEnd={() => setIsIconAnimating(false)}
                     width="20" height="20"/>
                )}
            </button>

            <a className={styles.footerRightLink} href="mailto:ailsonsixseven@gmail.com" target="_blank">
                <img className={styles.footerRightIcon} src={MAIL_ICON_URL} alt='E-mail' width="20" height="20"></img>
            </a>
            <a className={styles.footerRightLink} href="" target="_blank">
                <img className={styles.footerRightIcon} src={GITHUB_ICON_URL} alt='Repositorio' width="20" height="20"></img>
            </a>
            <a className={styles.footerRightLink} href="" target="_blank">
                <img className={styles.footerRightIcon} src={API_ICON_URL} alt='API' width="20" height="20"></img>
            </a>
        </div>
      </footer>
    )
}