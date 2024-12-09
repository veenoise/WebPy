import { Link } from "react-router-dom"
import { Button } from "./ui/button"

const Hero = () => {
  return (
    <div className="h-[calc(100vh-64px)] flex flex-col items-center justify-center">
      <h1 className="text-4xl text-center mb-2">WebPy</h1>
      <p className="text-center mb-5">A statically-typed python programming language based on Python and C.</p>
      <Link to="/">
        <Button className="bg-[#FFDD6F] text-neutral-800 hover:bg-[#FFDD40] hover:text-neutral-700">Try now!</Button>
      </Link>
    </div>
  )
}



export default Hero