import { useEffect } from 'react'
import { createPortal } from 'react-dom'

export default function ModalSystem({
  title,
  isOpen,
  onClose,
  children,
  size = 'medium',
  mode = 'content',
  message = '',
  confirmLabel = 'Delete',
  cancelLabel = 'Cancel',
  onConfirm,
}) {
  useEffect(() => {
    if (!isOpen) return

    const onKeyDown = (event) => {
      if (event.key === 'Escape') {
        onClose()
      }
    }

    document.body.style.overflow = 'hidden'
    window.addEventListener('keydown', onKeyDown)

    return () => {
      document.body.style.overflow = ''
      window.removeEventListener('keydown', onKeyDown)
    }
  }, [isOpen, onClose])

  if (!isOpen) return null

  return createPortal(
    <div className="modal-overlay" onClick={onClose} role="presentation">
      <section
        className={`modal modal--${size}`}
        onClick={(event) => event.stopPropagation()}
        role="dialog"
        aria-modal="true"
        aria-label={title}
      >
        <header className="modal__header">
          <h2>{title}</h2>
          <button
            className="button button--ghost button--small"
            onClick={onClose}
            type="button"
          >
            Close
          </button>
        </header>
        <div className="modal__body">
          {mode === 'confirm' ? (
            <>
              <p className="confirm-dialog__message">{message}</p>
              <div className="confirm-dialog__actions">
                <button type="button" className="button button--ghost" onClick={onClose}>
                  {cancelLabel}
                </button>
                <button type="button" className="button button--danger" onClick={onConfirm}>
                  {confirmLabel}
                </button>
              </div>
            </>
          ) : (
            children
          )}
        </div>
      </section>
    </div>,
    document.body,
  )
}
