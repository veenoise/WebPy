import { useState } from "react"
import { Textarea } from "@/components/ui/textarea"
import { Button } from "@/components/ui/button"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

const Home = () => {
  const [btnAllow, setBtnAllow] = useState(false)

  const loadFile = () => {
    const sourceCode:any = document.getElementById("source-code");
    const fileInput:any = document.getElementById("file");
    const file = fileInput.files[0];
    
    const dots = Array.from(file.name.matchAll(/\./g));
    const validFile = Array.from(file.name.matchAll(/\.wpy$/g));

    if (dots.length > 1 || validFile.length != 1) {
      alert("Invalid file");
    } else {
      const reader = new FileReader();
      reader.readAsText(fileInput.files[0]);

      reader.onload = function() {
        sourceCode.value = reader.result
      };
    
      reader.onerror = function() {
        console.log(reader.error);
      };
    }
  }

  const allowLoad = () => {
    const fileInput:any = document.getElementById("file");
    if (fileInput.files.length === 1) {
      setBtnAllow(true);
    } else {
      setBtnAllow(false);
    }
  }

  return (
    <div className="min-h-[calc(100dvh-64px)] container mx-auto">
      <h2 className="text-center text-2xl m-5">WebPy</h2>
      <div className="border rounded-md p-4 bg-neutral-800">
        <Tabs defaultValue="input">
          <div className="w-full flex justify-center">
            <TabsList className="bg-neutral-300">
              <TabsTrigger value="input">Input</TabsTrigger>
              <TabsTrigger value="output">Output</TabsTrigger>
            </TabsList>
          </div>
          
          <TabsContent value="input">
            <Textarea placeholder="Type your code here." id="source-code" className="resize-none mb-4" rows={25} />
            <div className="flex justify-end gap-3">
              <div className="flex items-center justify-center gap-2">
                <input 
                  id="file" 
                  name="file" 
                  type="file" 
                  accept=".wpy" 
                  onChange={allowLoad} 
                  className="bg-[#2B5B84] text-neutral-200"
                />
                <Button className="bg-[#2B5B84] text-neutral-200 hover:bg-[#205080] hover:text-neutral-300" id="load" onClick={loadFile} disabled={!btnAllow} >Load From File  </Button>  
              </div>
              
              <Button className="bg-[#FFDD6F] text-neutral-800 hover:bg-[#FFDD40] hover:text-neutral-700">Analyze</Button>  
            </div>
          </TabsContent>
          <TabsContent value="output">
            <p className="text-white">Error analyzing source code, please try again.</p>
          </TabsContent>
        </Tabs>
      </div>
      
      
    </div>
  )
}

export default Home