export default function FileTree({ files }) {
  return (
    <ul className="p-4">
      {files.map(f => <li key={f}>{f}</li>)}
    </ul>
  )
}
