import Image from "next/image";

interface BannerProps {}

export default function Banner(props: BannerProps) {
  return (
    <div className="rounded-2xl shadow-lg shadow-blue-300 mb-4">
      <div className='bg-[url("/img/banner-mobile.png")] sm:bg-[url("/img/lab1.png")] p-24 rounded-md bg-right-top bg-cover'>
        <Image
          src={"/img/logolexci.png"}
          alt="Logo Lexci"
          width={290}
          height={200}
        />
      </div>
    </div>
  );
}
