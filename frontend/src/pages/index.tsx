import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import { useEffect, useState } from "react";

const fetchCompanies = () => {
  return fetch("http://localhost:20002/companies")
    .then((res) => res.json())
    .then((res) => {
      console.log(res);
      return JSON.stringify(res);
    })
    .catch((err) => {
      console.error(err);
    });
};

const Home: NextPage = () => {
  const [companies, setCompanies] = useState("");
  useEffect(() => {
    fetchCompanies().then((result) => {
      setCompanies(result || "");
    });
  }, []);

  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <pre>{companies}</pre>
      </main>

      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{" "}
          <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
  );
};

export default Home;
