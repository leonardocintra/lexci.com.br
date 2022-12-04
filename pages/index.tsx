import Head from 'next/head'
import Footer from './footer/Footer'
import Inicio from './inicio/Inicio'

export default function Home() {
  return (
    <div>
      <Head>
        <title>Lexci - Laboratorio</title>
        <meta name="description" content="Site de consulta de exame da Lexci" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Inicio />
      <Footer />
    </div>
  )
}
