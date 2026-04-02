import { Link } from 'react-router-dom'

export default function NotFoundPage() {
  return (
    <section className="page">
      <article className="card empty-state">
        <h3>Page not found</h3>
        <p>The page you are looking for does not exist.</p>
        <Link className="button" to="/">
          Back to dashboard
        </Link>
      </article>
    </section>
  )
}
