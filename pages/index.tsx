import Head from "next/head";
import Inicio from "./inicio/Inicio";
import Main from "./inicio/main";

export default function Home() {
  return (
    <div className="">
      <Head>
        <title>Lexci - Laboratorio</title>
        <meta name="description" content="Site de consulta de exame da Lexci" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      {/* <div className="bg-red-400 flex items-center justify-center">
        <video autoPlay loop muted className="rounded-3xl m-2">
          <source src="video/video.mp4" type="video/mp4" />
        </video>
      </div> */}

      <Main></Main>
    </div>
  );
}
