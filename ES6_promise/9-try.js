export default function guardrail(mathFunction) {
  const queue = [];
  let value;

  try {
    value = mathFunction();
  } catch (err) {
    queue.push(`Error: ${err.message}`);
  }

  queue.push(value);
  queue.push('Guardrail was processed');

  return queue;
}
