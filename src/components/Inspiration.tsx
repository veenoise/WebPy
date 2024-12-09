import { cn } from "@/lib/utils";
import Marquee from "@/components/ui/marquee";
import bitfloat from './../../src/assets/12bitflaot.jpg'
import theresistor from './../../src/assets/theresistor.png'
import sazzer from './../../src/assets/sazzer.webp'
import john from './../../src/assets/john.jpeg'
import kraneq from './../../src/assets/kraneq.jpg'
import nidrach from './../../src/assets/nidrach.png'

const reviews = [
  {
    name: "theresistor",
    username: "u/theresistor",
    body: "The thing that always irritates me about pro-dynamic-typing arguments is the claim that the errors caught by static typing never come up in practice. That's just a load of bologna.",
    img: theresistor,
  },
  {
    name: "sazzer",
    username: "u/sazzer",
    body: "I don't hate dynamic typing, but I do prefer static typing for the peace of mind it gives you in a lot of situations - just like yours above.",
    img: sazzer,
  },
  {
    name: "12bitfloat",
    username: "@12bitfloat",
    body: "Dynamically typed languages suck. God I hate them It's like one big clunky free for all. I don't understand how people can work in Python or even JavaScript and tell me that they're good languages with a straight face.",
    img: bitfloat,
  },
  {
    name: "John Hoffmann",
    username: "@johnhoffmann",
    body: "When I write JavaScript on the other hand, my experience is the opposite. I spend as much time debugging as writing. That means that I spent 1/2 the day “creating problems” rather than solving them.",
    img: john,
  },
  {
    name: "kraneq",
    username: "u/kraneq",
    body: "feels like all the code i write with python works fast and its going everything smooth and easy to write but the next day there are tones of memory problems, process kills itself for loading too much data, it's slow to run and on the other hand c# just takes care of everything easily, a bit more code, but easier to undertand, self documented due to types, etc",
    img: kraneq,
  },
  {
    name: "nidrach",
    username: "u/nidrach",
    body: "I just see them as hiding information. Data is almost always supposed to be a type and with typed languages you just keep track in code of that. Being more explicit usually makes things more readable and unlike boilerplate types don't really add bulk.",
    img: nidrach,
  },
];

const firstRow = reviews.slice(0, reviews.length / 2);
const secondRow = reviews.slice(reviews.length / 2);

const ReviewCard = ({
  img,
  name,
  username,
  body,
}: {
  img: string;
  name: string;
  username: string;
  body: string;
}) => {
  return (
    <figure
      className={cn(
        "relative w-64 cursor-pointer overflow-hidden rounded-xl border p-4",
        // light styles
        "border-gray-950/[.1] bg-gray-950/[.01] hover:bg-gray-950/[.05]",
        // dark styles
        "dark:border-gray-50/[.1] dark:bg-gray-50/[.10] dark:hover:bg-gray-50/[.15]",
      )}
    >
      <div className="flex flex-row items-center gap-2">
        <img className="rounded-full" width="32" height="32" alt="" src={img} />
        <div className="flex flex-col">
          <figcaption className="text-sm font-medium dark:text-white">
            {name}
          </figcaption>
          <p className="text-xs font-medium dark:text-white/40">{username}</p>
        </div>
      </div>
      <blockquote className="mt-2 text-sm">{body}</blockquote>
    </figure>
  );
};


const Inspiration = () => {
  return (
    <div className="my-16 md:my-40">
      <h2 className="text-2xl mb-5 text-center">Inspiration</h2>
      <div className="relative flex w-full flex-col items-center justify-center overflow-hidden bg-background">
        <Marquee pauseOnHover className="[--duration:20s]">
          {firstRow.map((review) => (
            <ReviewCard key={review.username} {...review} />
          ))}
        </Marquee>
        <Marquee reverse pauseOnHover className="[--duration:20s]">
          {secondRow.map((review) => (
            <ReviewCard key={review.username} {...review} />
          ))}
        </Marquee>
        <div className="pointer-events-none absolute inset-y-0 left-0 w-1/3 bg-gradient-to-r from-white dark:from-background"></div>
        <div className="pointer-events-none absolute inset-y-0 right-0 w-1/3 bg-gradient-to-l from-white dark:from-background"></div>
      </div>
    </div>
  )
}

export default Inspiration