export default function FormField({
  label,
  name,
  type = 'text',
  value,
  onChange,
  error,
  options,
  min,
  step,
  placeholder,
}) {
  const inputProps = {
    id: name,
    name,
    value,
    onChange: (event) => onChange(name, event.target.value),
  }

  return (
    <div className="form-field">
      <label htmlFor={name}>{label}</label>
      {type === 'select' ? (
        <select {...inputProps} className={`select ${error ? 'input--error' : ''}`}>
          {options?.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      ) : (
        <input
          {...inputProps}
          type={type}
          className={`input ${error ? 'input--error' : ''}`}
          min={min}
          step={step}
          placeholder={placeholder}
        />
      )}
      {error ? <p className="form-field__error">{error}</p> : null}
    </div>
  )
}
