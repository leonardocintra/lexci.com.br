import Footer from "../../components/Footer";
import Logo from "../../components/Logo";
import Worklab from "../../components/Worklab";

export default function Inicio() {
  return (
    <div className="container mx-auto mt-4">
      <Logo></Logo>
      <Worklab />
      <Footer></Footer>
    </div>
  );
}
