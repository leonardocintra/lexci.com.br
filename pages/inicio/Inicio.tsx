import Footer from "../../components/footer/Footer";
import Logo from "../../components/header/banner";
import Worklab from "../../components/worklab/Worklab";

export default function Inicio() {
  return (
    <div className="container mx-auto mt-4">
      <Logo></Logo>
      <Worklab />
      <Footer></Footer>
    </div>
  );
}
