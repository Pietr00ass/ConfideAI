import { useEffect, useState } from 'react'
import api from '../api/api'
import FileTree from '../components/FileTree'

export default function FileBrowser() {
  const [files, setFiles] = useState([])
  useEffect(() => {
    api.get('/crypto/list-files').then(r=>setFiles(r.data.files))
  }, [])
  return <FileTree files={files} />
}
