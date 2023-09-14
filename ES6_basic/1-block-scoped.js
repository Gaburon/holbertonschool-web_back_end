// Task 1:  modify the variables inside the function taskBlock
// so that the variables aren’t overwritten inside the conditional block.

export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;
  
    if (trueOrFalse) {
      /* eslint-disable */
          const task = true;
          const task2 = false;
      }
  
      return [task, task2];
  }
