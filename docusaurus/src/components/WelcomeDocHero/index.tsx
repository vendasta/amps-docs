import type {ReactElement} from 'react';
import styles from './styles.module.css';

const TITLE = 'Welcome';

export function WelcomeDocHero(): ReactElement {
  return (
    <div className={styles.welcomeWrap} aria-label="Welcome to documentation">
      <div className={styles.welcomeSpin} aria-hidden />
      <div className={styles.welcomeInner}>
        <div className={styles.orbA} aria-hidden />
        <div className={styles.orbB} aria-hidden />
        <div className={styles.orbC} aria-hidden />
        <div className={styles.shimmer} aria-hidden />
        <header className={styles.welcomeHeader}>
          <h1 className={styles.welcomeTitle}>
            <span className={styles.titleTrack}>
              {TITLE.split('').map((char, i) => (
                <span
                  key={i}
                  className={styles.titleChar}
                  style={{animationDelay: `${0.35 + i * 0.06}s`}}
                >
                  {char}
                </span>
              ))}
            </span>
          </h1>
          <p
            className={styles.welcomeLead}
            style={{animationDelay: '0.75s'}}
          >
            Browse <strong>Guru card contents</strong> and{' '}
            <strong>SOP</strong> (standard operating procedures) using the sidebar.
            This site is the internal reference for Vendasta Services documentation.
          </p>
          <p
            className={styles.welcomeHint}
            style={{animationDelay: '0.95s'}}
          >
            Use the categories on the left to open Guru cards or SOP documents.
          </p>
        </header>
      </div>
    </div>
  );
}
