import { useState } from "react"
import { Textarea } from "@/components/ui/textarea"
import { Button } from "@/components/ui/button"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import jsPDF from 'jspdf'
import autoTable from 'jspdf-autotable'


const Home = () => {
  const [btnAllow, setBtnAllow] = useState(false);
  const [output, setOutput] = useState<OutputState>();
  const [input, setInput] = useState<any>();
  

  type OutputState = {
    token_list: [string, string][];
    error: string
  } | null;
  const loadFile = () => {
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
        setInput(reader.result)
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

  const resetFileInput = () => {
    setBtnAllow(false)
  }

  const postReq = () => {
    const sourceCode:any = document.getElementById("source-code");

    fetch("http://127.0.0.1:5000/", {
      method: "POST",
      headers: {
        'Content-Type': 'text/plain' 
      },
      body: sourceCode.value
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(result => {
      setOutput(result)
    })
    .catch(e => {
      console.error(`ERROR: ${e}`);
    })
  }

  const downloadPDF = () => {
    const doc = new jsPDF()
    autoTable(doc, { html: '#lexer-table' })
    doc.save('WebPy_Lexer_Table.pdf')
  }

  const inputField = (event:any) => {
    setInput(event.target.value)
  }

  return (
    <div className="min-h-[calc(100dvh-64px)] container mx-auto">
      <h2 className="text-center text-2xl m-5">WebPy</h2>
      <div className="border rounded-md p-4 bg-neutral-800">
        <Tabs defaultValue="input">
          <div className="w-full flex justify-center">
            <TabsList className="bg-neutral-300">
              <TabsTrigger value="input">Input</TabsTrigger>
              <TabsTrigger value="output" onClick={resetFileInput}>Output</TabsTrigger>
            </TabsList>
          </div>
          <TabsContent value="input">
            <Textarea placeholder="Type your code here." id="source-code" className="resize-none mb-4" rows={25} onChange={inputField} value={input} />
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
              
              <Button className="bg-[#FFDD6F] text-neutral-800 hover:bg-[#FFDD40] hover:text-neutral-700" onClick={postReq}>Analyze</Button>  
            </div>
          </TabsContent>
          <TabsContent value="output">
            <div className="mb-4 flex justify-end">
              <Button className="bg-[#FFDD6F] text-neutral-800 hover:bg-[#FFDD40] hover:text-neutral-700" onClick={downloadPDF}>Download PDF</Button>
            </div>
            
            <Table className="bg-neutral-200 table-auto" id="lexer-table">
              <TableCaption>Lexical Analyzer Lexeme-Token Table</TableCaption>
              <TableHeader>
                <TableRow>
                  <TableHead className="text-black font-bold">Lexemes</TableHead>
                  <TableHead className="text-black font-bold">Tokens</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {
                  output && output.token_list ?
                  (
                    output.token_list.map((content:[string, string], id) => {
                      return (
                        <TableRow key={id}>
                          <TableCell className="break-all"><pre>{JSON.stringify(content[0]).substring(1, JSON.stringify(content[0]).length - 1)}</pre></TableCell>
                          <TableCell><pre>{content[1]}</pre></TableCell>
                        </TableRow>
                      )
                  })) :
                  <></>
                }
                {
                  output && output.error ? 
                  (
                    <TableRow>
                      <TableCell colSpan={2}><pre>{output.error}</pre></TableCell>
                    </TableRow>
                  ):
                  <></>
                }
              </TableBody>
            </Table>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}

export default Home