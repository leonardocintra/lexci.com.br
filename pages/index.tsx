import Head from 'next/head'

export default function Home() {
  return (
    <div className='container'>
      <Head>
        <title>Lexci - Laboratorio</title>
        <meta name="description" content="Site de consulta de exame da Lexci" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className='text-center'>
        <br />
        <br />
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

      <footer className='text-center'>
        2019 - 2022 | Desenvolvido by Leonardo Cintra | @leonardocintra
      </footer>
    </div>
  )
}
