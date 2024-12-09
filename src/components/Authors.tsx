import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

const authorNames = [
  {
    name: "Janine Arzadon",
    imgSrc: "https://github.com/shadcn.png"
  },
  {
    name: "William Chua",
    imgSrc: "https://github.com/shadcn.png"
  },
  {
    name: "Jason Espallardo",
    imgSrc: "https://github.com/shadcn.png"
  },
  {
    name: "David Garcia",
    imgSrc: "https://github.com/shadcn.png"
  },
  {
    name: "Tyrece Tan",
    imgSrc: "https://github.com/shadcn.png"
  },
  
]

const Authors = () => {
  return (
    <div className="my-16 md:my-40">
      <h2 className="text-2xl mb-3 text-center">Authors</h2>
      <div className="border-2 rounded-md flex gap-4 p-10 justify-center flex-wrap m-6 mb-10 shadow-xl">
        {authorNames.map((e, id) => {
          return (
            <div key={id} className="flex flex-col items-center justify-center gap-2 colums-4 w-48">
              <Avatar className="w-24 h-24">
                <AvatarImage src={e.imgSrc} />
                <AvatarFallback>CN</AvatarFallback>
              </Avatar>
              <p>{e.name}</p>
            </div>
          )
        })}
        
    
      </div>
    </div>
    
  )
}

export default Authors