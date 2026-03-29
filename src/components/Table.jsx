function EmptyState({ title, description, action }) {
  return (
    <div className="empty-state">
      <h3>{title}</h3>
      <p>{description}</p>
      {action ? <div>{action}</div> : null}
    </div>
  )
}

function TableToolbar({ search, filters = [], actions }) {
  const hasSearch = Boolean(search?.onChange)
  if (!hasSearch && !filters.length && !actions) return null

  return (
    <div className="search-filter-bar">
      <div className="search-filter-bar__left">
        {hasSearch ? (
          <input
            value={search.value}
            className="input"
            type="search"
            onChange={(event) => search.onChange(event.target.value)}
            placeholder={search.placeholder || 'Search...'}
          />
        ) : null}

        {filters.map((filter) => (
          <select
            key={filter.key}
            className="select"
            value={filter.value}
            onChange={(event) => filter.onChange(event.target.value)}
          >
            {filter.options.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        ))}
      </div>
      {actions ? <div className="search-filter-bar__right">{actions}</div> : null}
    </div>
  )
}

function TablePagination({
  currentPage,
  totalPages,
  onPageChange,
  pageSize,
  onPageSizeChange,
  pageSizeOptions = [5, 10, 15, 20],
}) {
  if (totalPages <= 1 && !onPageSizeChange) return null

  return (
    <div className="pagination">
      <div className="pagination__size">
        {onPageSizeChange ? (
          <>
            <span>Rows per page:</span>
            <select
              className="select select--small"
              value={pageSize}
              onChange={(event) => onPageSizeChange(Number(event.target.value))}
            >
              {pageSizeOptions.map((option) => (
                <option key={option} value={option}>
                  {option}
                </option>
              ))}
            </select>
          </>
        ) : null}
      </div>

      <div className="pagination__controls">
        <button
          type="button"
          className="button button--ghost button--small"
          onClick={() => onPageChange(currentPage - 1)}
          disabled={currentPage === 1}
        >
          Previous
        </button>
        <span>
          Page {currentPage} of {totalPages}
        </span>
        <button
          type="button"
          className="button button--ghost button--small"
          onClick={() => onPageChange(currentPage + 1)}
          disabled={currentPage === totalPages}
        >
          Next
        </button>
      </div>
    </div>
  )
}

export default function Table({
  columns,
  rows,
  rowKey = 'id',
  emptyTitle = 'No records found',
  emptyDescription = 'Try adjusting filters or adding new records.',
  emptyAction,
  search,
  filters,
  actions,
  pagination,
}) {
  return (
    <>
      <TableToolbar search={search} filters={filters} actions={actions} />

      {rows.length ? (
        <div className="table-wrapper">
          <table className="data-table">
            <thead>
              <tr>
                {columns.map((column) => (
                  <th key={column.key} style={column.width ? { width: column.width } : undefined}>
                    {column.header}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {rows.map((row) => (
                <tr key={String(row[rowKey] ?? `${rowKey}-missing`)}>
                  {columns.map((column) => (
                    <td key={`${String(row[rowKey] ?? `${rowKey}-missing`)}-${column.key}`}>
                      {column.render ? column.render(row) : row[column.key]}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <EmptyState title={emptyTitle} description={emptyDescription} action={emptyAction} />
      )}

      {pagination ? <TablePagination {...pagination} /> : null}
    </>
  )
}
