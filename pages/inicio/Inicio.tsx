import Image from "next/image";
import Worklab from "../worklab/Worklab";

export default function Inicio() {
  return (
    <div className="container mx-auto">
      <div className="rounded-2xl shadow-2xl shadow-blue-300 mb-4">
        <div className='bg-[url("/img/lab1.png")] p-24 '>
          <Image
            src={"/img/logolexci.png"}
            alt="Logo Lexci"
            width={290}
            height={200}
          />
        </div>
      </div>
      <Worklab />
    </div>
  );
}
