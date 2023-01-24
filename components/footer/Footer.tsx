export default function Footer() {
  return (
    <div className="container border-t-4 mt-5 py-4 max-w-5xl">
      <footer className="text-gray-400">
        <div className="flex justify-center text-gray-900 text-lg space-x-2">
          <h2 className="text-lg font-semibold">Laboratório Lexci</h2>
          <h2> - </h2>
          <h2> CNPJ 02.312.477/0001-38</h2>
        </div>
        <div className="flex justify-center mt-2 text-blue-700 italic">
          <h4 className="text-sm">Todos os direitos reservados</h4>
        </div>
        <div className="flex flex-col sm:flex-row justify-center items-center space-x-2 mt-4">
          <div className="flex">2016 - 2023</div>
          <div className="flex">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              strokeWidth={1.5}
              stroke="currentColor"
              className="w-6 h-6 mr-2"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M9 17.25v1.007a3 3 0 01-.879 2.122L7.5 21h9l-.621-.621A3 3 0 0115 18.257V17.25m6-12V15a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 15V5.25m18 0A2.25 2.25 0 0018.75 3H5.25A2.25 2.25 0 003 5.25m18 0V12a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 12V5.25"
              />
            </svg>
            Desenvolvido by Leonardo Cintra | @leonardocintra
          </div>
        </div>
      </footer>
    </div>
  );
}
