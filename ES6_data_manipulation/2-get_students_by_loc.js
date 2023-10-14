/* enlist-disable */
export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }

  const filter = students.filter((filteredObj) => filteredObj.location === city);
  return filter;
}
