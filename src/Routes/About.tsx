import Authors from "@/components/Authors"
import Hero from "@/components/Hero"
import Inspiration from "@/components/Inspiration"
import Principles from "@/components/Principles"

const About = () => {
  return (
    <div className="container mx-auto">
      <Hero />
      <Authors />
      <Inspiration />
      <Principles />
    </div>

  )
}

export default About