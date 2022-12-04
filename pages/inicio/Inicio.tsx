import Image from 'next/image';
import Worklab from '../worklab/Worklab';

export default function Inicio() {
    return (
        <div>
            <div className='bg-[url("/img/lab1.png")] h-96 w-full p-24 bg-cover'>
                <Image src={'/img/logolexci.png'} alt='Logo Lexci' width={290} height={200} />
            </div>

            <Worklab />
        </div>
    )
}