import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className='container'>
      <Head>
        <title>Lexci - Laboratorio</title>
        <meta name="description" content="Site de consulta de exame da Lexci" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1>
          Bem vindo ao Lexci
        </h1>

        <p>
          Pesquisar meu exame
        </p>

        <div>
          <h4 className="text-center"> Consulta de exames </h4>
          <iframe src="https://worklabweb.com.br/frame.php?Cliente=769&i=3" name="I1" width="500" height="150"></iframe>
        </div>
      </main>

      <footer>
        2019 - 2022 | Desenvolvido by Leonardo Cintra | @leonardocintra
      </footer>
    </div>
  )
}
