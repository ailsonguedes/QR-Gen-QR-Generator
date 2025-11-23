import styles from './NavBar.module.css'

export function NavBar() {
    return (
        <nav className={styles.navBarContainer}>
            <div className={styles.navBarLeft}>
                <svg className={styles.navBarLogo} width="32" height="32" viewBox="0 0 32 32" fill="none">
                    <rect width="32" height="32" rx="6" fill="#2D728F"/>
                    <path d="M8 10h15 M8 13v10 M11 23h11 M22 13v7
                             M12 13h6 M12 16v4 M15 20h3 M15.5 16.5h2" 
                          stroke="white" 
                          strokeWidth="2" 
                          strokeLinecap="round"/>
                </svg>
                <h2 className={styles.navBarLeftTitle}>QR Gen</h2>
            </div>

            <div className={styles.navBarRight}>
                <a className={styles.navBarRightLink} href="#">Home</a>
                <a className={styles.navBarRightLink} href="#">Contact</a>
                <a className={styles.navBarRightLink} href="#">About</a>
            </div>
        </nav>
    )
}
