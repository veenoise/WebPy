import { Link, useLocation } from "react-router-dom"
import { Button } from "@/components/ui/button"

const NavigationBar = () => {
  const location = useLocation()

  return (
    <nav className="bg-[#2B5B84] text-white px-5 h-[64px] flex items-center justify-between">
      <h1 className="text-2xl font-bol">WebPy</h1>
      <div className="flex gap-2 md:gap-5">
        <Link to="/">
          <Button variant="ghost" className={location.pathname === "/" ? "underline" : ""}>Home</Button>
        </Link>
        <Link to="/about">
          <Button variant="ghost" className={location.pathname === "/about" ? "underline" : ""}>About</Button>
        </Link>
      </div>
    </nav>
  )
}

export default NavigationBar