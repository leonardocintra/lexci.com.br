import Image from "next/image";

export default function Logo() {
  return (
    <div className="flex items-center justify-center">
      <Image
        src={"/img/logolexci.png"}
        alt="Logo Lexci"
        width={290}
        height={200}
      />
    </div>
  );
}
