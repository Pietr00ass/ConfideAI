import { useState } from 'react'
import api from '../api/api'

export default function Crypto() {
  const [path, setPath] = useState('')
  const [remove, setRemove] = useState(false)
  const [msg, setMsg] = useState('')
  const enc = async () => {
    const { data } = await api.post('/crypto/encrypt', { filepath: path, remove_original: remove })
    setMsg(data.status)
  }
  const dec = async () => {
    const { data } =
 await api.post('/crypto/decrypt', { filepath: path, remove_original: remove })
    setMsg(data.status)
  }
  return (
    <div className="p-4">
      <input value={path} onChange={e=>setPath(e.target.value)} placeholder="File path" />
      <label><input type="checkbox" checked={remove} onChange={e=>setRemove(e.target.checked)} /> Remove original</label>
      <button onClick={enc}>Encrypt</button>
      <button onClick={dec}>Decrypt</button>
      <div>{msg}</div>
    </div>
  )
}
