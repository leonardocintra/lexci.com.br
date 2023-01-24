import Footer from "../../components/footer/Footer";
import Banner from "../../components/header/banner";
import Worklab from "../../components/worklab/Worklab";

export default function Inicio() {
  return (
    <div className="container mx-auto mt-4">
      <Banner></Banner>
      <Worklab />
      <Footer></Footer>
    </div>
  );
}
