import Footer from "../../components/Footer";
import Logo from "../../components/Logo";
import Worklab from "../../components/Worklab";

export default function Main() {
  return (
    <div>
      <header className="relative flex items-center justify-center h-screen overflow-hidden">
        <div className="relative z-30 p-5">
          <Logo></Logo>
          <Worklab></Worklab>
          <Footer></Footer>
        </div>
        <video
          autoPlay
          loop
          muted
          className="absolute z-10 w-auto min-w-full min-h-full max-w-none opacity-60"
        >
          <source src={"video/video.mp4"} type="video/mp4" />
        </video>
      </header>
    </div>
  );
}
