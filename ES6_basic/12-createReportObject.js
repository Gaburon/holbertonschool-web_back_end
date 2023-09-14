export default function createReportObject(employeesList) {
  const retObject = {
    allEmployees: employeesList,
    getNumberOfDepartments(object) {
      return Object.keys(object).length;
    },
  };
  return retObject;
}
