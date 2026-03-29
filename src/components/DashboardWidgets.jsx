const STATUS_VARIANTS = {
  'In Stock': 'success',
  'Low Stock': 'warning',
  'Out of Stock': 'danger',
  Pending: 'warning',
  Approved: 'info',
  Completed: 'success',
  Cancelled: 'neutral',
  Received: 'success',
  'In Transit': 'info',
  Delayed: 'danger',
}

export function Stat({ label, value, hint, tone = 'default' }) {
  return (
    <article className={`stat-card stat-card--${tone}`}>
      <p className="stat-card__label">{label}</p>
      <h3 className="stat-card__value">{value}</h3>
      {hint ? <p className="stat-card__hint">{hint}</p> : null}
    </article>
  )
}

export function StatusPill({ status }) {
  const variant = STATUS_VARIANTS[status] || 'neutral'
  return <span className={`status-badge status-badge--${variant}`}>{status}</span>
}
